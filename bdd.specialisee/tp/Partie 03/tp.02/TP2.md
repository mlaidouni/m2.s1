# TP2 Bases de données spécialisées
# 2025 - 2026
 
# Install and run Cassandra on your machine.
Did everything work fine ?
If not, what were the problems and how did you solve them ?

# Scripting BASH
The directory containing the executable files (for instance `/usr/sbin/`)
contains the file `cassandra`.
Modify that file so that when executed it prints to
the standard output

SCRIPT TO START CLUSTER: name of your cluster
USING OPTIONS: options   
   
where "options" is the list of options given in 
the command line used to start the server.
   
Which parts of the script did you modify, and how?


# Source code

Download the sources of Cassandra via git:

git clone https://github.com/apache/cassandra.git


## Understanding the code
### A
In the file `CassandraDaemon.java` how the field `instance` defined?
Which modifiers are used and why?

### B
Which method(s) compute the heartbeat of a node that
is mentioned in slide 56 of the slides?
Does the code implement the algorithm outlined in the slide?
If yes, why yes? If not, why not?
	
### C
Which methods are executed to manage a read request
received by a server?
In which order are are they executed and what does each
method do?


## Minimal work with Java

Modify the __java code__ and recompile it so that

### A
when you start your ad-hoc server, after having finished
the bootstrap, it __logs__ a line containing

   ^^^^ Home brewed Cassandra server! ^^^

### B
when you shut down your ad-hoc server 
via CTRL+C in the terminal, it __logs__ lines containing

   ^^^^ Bye bye bird  ^^^
   ^^^^ Bird I'm gone ^^^   

Which commands did you run to (re)compile cassandra?
In the java code, which methods did you modify and how?

### C

Consider the method `fullCMSMembers` in the file `ClusterMetadata.java`.
What is the value computed by this method?
What does it represent?
What is it useful for?



# Using a Cassandra cluster

The cluster must comprise all the machines of your group (at least three).

## A

Which difficulties did you encounter setting up the cluster ?
If any, how  did you deal with them?

## B
Can you configure your cluster to make at one node stop the
execution of Cassandra signalling the error message

"
Token allocation failed: the number of racks X in datacenter Y is lower than its replication factor Z.
Fatal configuration error; unable to start server.  See log for stacktrace.
"

where X, Y, Z are variables.

Which code generates this error message ?
