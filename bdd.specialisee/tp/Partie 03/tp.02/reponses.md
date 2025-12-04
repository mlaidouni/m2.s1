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
