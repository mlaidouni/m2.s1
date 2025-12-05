# TP 2 - Réponses

## 1 - Installation de Cassandra

Lors de l’installation de Cassandra sur macOS, tout ne s’est pas déroulé correctement au premier essai.
Bien que l’installation via Homebrew se soit faite sans erreur, il était impossible de démarrer Cassandra car le système ne détectait aucun JDK compatible : la commande `java_home -V` renvoyait “Unable to locate a Java Runtime” et Cassandra échouait au démarrage avec une exception liée à Policy.setPolicy, due à l’utilisation d’une version de Java trop récente et incompatible.

Pour résoudre ces problèmes, j’ai installé un JDK 17 (`brew install openjdk@17`), puis je l’ai lié au système de manière à ce qu’il soit détecté par macOS (`sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk`). J’ai ensuite défini correctement JAVA_HOME et relancé Cassandra (`JAVA_HOME=$(/usr/libexec/java_home -v 17) /opt/homebrew/opt/cassandra/bin/cassandra -f`).

J’ai également arrêté le service Cassandra démarré automatiquement par Homebrew, vidé les répertoires de données (`/opt/homebrew/var/lib/cassandra/*`), puis effectué toutes les modifications de configuration avant le premier vrai démarrage, conformément aux instructions du cours : définition du nom du cluster, des seeds (valeur par défaut, 16), du datacenter et du rack (valeurs par défaut également).

Après ces corrections, Cassandra a démarré correctement, a exécuté son bootstrap d’un seul nœud, et les commandes `nodetool status` et `nodetool describecluster` ont confirmé que le noeud était en état UN (Up/Normal), avec la bonne configuration (dc1, rack1, BDS_M2_Cluster, Murmur3Partitioner, GossipingPropertyFileSnitch).

## 2 - Scripting BASH

Le script a été modifié pour afficher le nom du cluster et les options utilisées lors du démarrage du serveur. Voici les modifications apportées :

```bash
#!/bin/bash
CLUSTER_NAME=$(grep "^cluster_name:" /opt/homebrew/etc/cassandra/cassandra.yaml | awk '{print $2}' | tr -d "'")
echo "SCRIPT TO START CLUSTER: $CLUSTER_NAME"
echo "USING OPTIONS: $@"
exec "/opt/homebrew/Cellar/cassandra/5.0.6/libexec/bin/cassandra" "$@" # - Ligne déjà présente
```

## 3 - Understanding the source code of Cassandra

### Question A : In the file CassandraDaemon.java how the field instance defined? Which modifiers are used and why?

Le champs est définie comme `static`, `final` et visibilité `package-private`.

`static` : il n’y a qu’une seule instance de CassandraDaemon dans le processus JVM.
`final` : la variable `instance` ne peut jamais être réaffectée à un autre objet. Cela renforce l’idée de singleton (une seule instance contrôlée, créée une fois pour toutes).
`package-private` : l’accès direct à cette instance est limité aux classes du même package (`org.apache.cassandra.service`). On voit que, pour les tests, une méthode spécifique est fourni `@VisibleForTesting getInstanceForTesting()`.

### Question B

### Question C

## 4 - Minimal work with Java

### Question A-B : Which commands did you run to (re)compile cassandra? In the java code, which methods did you modify and how?

```zsh
cd cassandra/
# J'ai précisé la version de java à utiliser (que l'on trouve dans le build.xml)
JAVA_HOME=$(/usr/libexec/java_home -v 17) ant jar
```

Mais cela n'a pas fonctionné, car gradle utilisait openjdk 21.

J'ai donc supprimé le cache de gradle, puis fait un export

```zsh
rm -f ~/.gradle/gradle.properties
rm -rf ~/.gradle/caches
rm -rf ~/.gradle/jdks
```

```zsh
cd cassandra/
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
ant realclean # Purge les anciens fichiers compilés
ant jar
```

Et cette fois, la compilation a fonctionné.

Pour la question A, j'ai modifié la méthode `setup()` dans la classe `CassandraDaemon.java`, en ajoutant une ligne de log après la fin du bootstrap :

```java
// start server internals
StorageService.instance.registerDaemon(this);
try
{
    StorageService.instance.initServer();
}
catch (ConfigurationException e)
{
    System.err.println(e.getMessage() + "\nFatal configuration error; unable to start server.  See log for stacktrace.");
    exitOrFail(1, "Fatal configuration error", e);
}

logger.info("^^^^ Home brewed Cassandra server! ^^^^"); // ligne 397
```

Pour la question B, j'ai d'abord modifié la méthode `stop()` dans la même classe `CassandraDaemon.java`, en ajoutant des lignes de log au début de la méthode :

```java
public void stop()
{
    // On linux, this doesn't entirely shut down Cassandra, just the RPC server.
    // jsvc takes care of taking the rest down
    logger.info("Cassandra shutting down...");
	logger.info("^^^^ Bye bye bird  ^^^");
	logger.info("^^^^ Bird I'm gone ^^^");
    destroyClientTransports();
```

Mais ça ne fonctionnait pas, car la méthode `stop()` n'était pas appelée lors de l'arrêt via CTRL+C.

Puis, après avoir analysé les logs dans `System.log`, j'ai vu que c'était fait dans le thread dans `src/java/org/apache/cassandra/service/StorageService.java`, méthode `initServer()` :

```java
drainOnShutdown = NamedThreadFactory.createThread(new WrappedRunnable()
{
    @Override
    public void runMayThrow() throws InterruptedException, ExecutionException, IOException
    {
        drain(true);
        try
        {
            ExecutorUtils.shutdownNowAndWait(1, MINUTES, ScheduledExecutors.scheduledFastTasks);
            logger.info("Cassandra shutdown complete");
			// NOTE [MLA]: TP2 4-B
			logger.info("^^^^ Bye bye bird  ^^^");
			logger.info("^^^^ Bird I'm gone ^^^");
        }
        catch (Throwable t)
        {
            logger.warn("Unable to terminate fast tasks within 1 minute.", t);
        }
        finally
        {
            LoggingSupportFactory.getLoggingSupport().onShutdown();
        }
    }
}, "StorageServiceShutdownHook");
Runtime.getRuntime().addShutdownHook(drainOnShutdown);
```

### Question C : Consider the method fullCMSMembers in the file ClusterMetadata.java. What is the value computed by this method? What does it represent? What is it useful for?

La méthode `fullCMSMembers()` renvoie un `Set<InetAddressAndPort>`, c’est-à-dire l’ensemble des adresses des noeuds qui sont considérés comme “full members” du Cluster Metadata Service (CMS).

Concrètement, elle :

- récupère, via `placements.get(ReplicationParams.meta(this))`, la stratégie de réplication utilisée pour les métadonnées du cluster (la “meta” keyspace, là où sont stockées les infos de TCM / CMS) ;
- prend la vue de lecture reads,
- regarde la table `byEndpoint()`,
- et renvoie l’ensemble des clés de cette map (`keySet()`), c’est-à-dire tous les endpoints qui participent aux lectures de ces métadonnées.

Donc la valeur calculée est l’ensemble des nœuds qui stockent et servent les métadonnées du cluster pour la réplication “meta” : ce sont les nœuds membres à part entière du CMS (par opposition à de simples observateurs).

Ce que ça représente :

- la liste des membres “complets” du CMS dans l’état courant de ClusterMetadata;
- autrement dit, les nœuds qui détiennent une copie cohérente et répliquée de l’état global du cluster (topologie, placements, etc.) et qui sont pris en compte pour les lectures des métadonnées.

À quoi c’est utile :

- à savoir sur quels nœuds envoyer les opérations de métadonnées (lecture/écriture de l’état TCM/CMS) ;
- à calculer des quorums CMS (par ex. combien de ces nœuds doivent répondre pour valider une mise à jour de métadonnées) ;
- à vérifier rapidement si un nœud donné est membre du CMS via isCMSMember(endpoint) et à dériver d’autres vues comme les identifiants (fullCMSMemberIds()) ou les replicas (fullCMSMembersAsReplicas()).
