# TP3 Bases de données spécialisées
# 2024 - 2025


## Connect to your Cassandra cluster using cqlsh.

   Does `nodetool describecluster` work on all the nodes ?
   If not, why not ?
   What is the root cause of this apparently non-deterministic behaviour ?
   

## Install python, the python driver for cassandra and
   run on your cluster all the programs seen during the 
   lecture. 
   
   Have you encountered any difficulty that
   we have not seen during the lecture ?


## After having created a keyspace 'demo',
   compare the results of executing the command lines
   
   nodetool describering demo
   nodetool describering system

   Why is there a difference in the outputs ?
   Why is there such difference ?
   

## The file ex6-music.py can create two small keyspaces
   with data related to music. Can you 
   1) think of queries to use these data ?
   
   2) does the data model fit your queries ?
      If not, can you change the keyspace schema ?
	  
   3) Perform a read query at different consistency levels,
	  and with a different number of machine turned on.
	  Produce results that indeed show the
	  difference in consistency levels.


## Recall the code you used for the TP1 in 

  benchbase/src/main/java/com/oltpbenchmark/benchmarks/tpcc     
  
  Do you think it makes sense to adapt TPC-C to run
  on a cassandra cluster ?
  
  If yes, can you adapt the code to run it on your cluster ?
  If not, why not ?
  And if you were forced to modify the code,
  what would you modify and why ?




## EVALUATION

Prepare a talk (along with the slides !)
in which you summarise all the answers to 
questions asked in the exercises for the TPs

OR

you briefly expose the ideas behind the solutions
to problems hinted at during the lectures
(Why does the failure detection in Cassandra ctually work ?
Why does Paxos work ?
How did the Dynamo database influence the deisng of Cassandra ?
...)

If all the exercises were easy, you are free
to study any technical paper on cassandra
and explain a technical subject that we
have not had the time to discuss.

Some ideas or facts may be trifles, some may be
very very interesting.
It's up to you to decide what to talk about.

The talk must be at most __8min__ long.

The file containing the slides must be in 
   
   __pdf format__ 
   
and its name must have the form

   bds-2425-GROUPNAME.pdf

where GROUPNAME is the name of your group.
   
The file containing the slides must be sent
to the addres 
   
   gio XYZ irif.fr 
   
and correctly received __before__
   
   15:00 December the 10th
   
The subject of the e-mail must have the format
   
   [bds-2425] slides: GROUPNAME
   
where GROUP_NAME is the name of your group.
Any dely or error in following the above instructions
will be taken into account in the evaluation.
