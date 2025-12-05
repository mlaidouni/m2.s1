# TP3 Bases de données spécialisées
# 2025 - 2026


## Connect to your Cassandra cluster using cqlsh.

   Does `nodetool describecluster` work on all the nodes?
   If not, why not?
   What is the root cause of this apparently non-deterministic behaviour?


## Python

   Install python, the python driver for cassandra and
   run on your cluster suitable variants of the programs
   discussed during the lecture. 
   
   Have you encountered any difficulty?


## Describering

   Create a keyspace 'demo', compare the results of 
   executing the command lines
   
   nodetool describering demo
   nodetool describering system

   Why is there a difference in the outputs?
   Why is there such difference?
   

## Music DB

   The execution of the file `ex6-music.py` creates
   two small column families with data related to music. 

   1) Which queries to use these data are reasonable in
	a real world application?
   
   2) Does the data model fit the queries of part 1) above?
      If not, can you change the keyspace schema?
	  
   3) Perform a read query at different consistency levels,
	  and with a different number of nodes on-line.
	  Produce results that indeed show the
	  difference in consistency levels.


## Recall the code you used for the TP1 in 

  benchbase/src/main/java/com/oltpbenchmark/benchmarks/tpcc     
  
  Do you think it makes sense to adapt TPC-C to run
  on a cassandra cluster?
  
  If yes, can you adapt the code to run it on your cluster?
  If not, why not?
  And if you were forced to modify the code,
  what would you modify and why?




## EVALUATION

Prepare a talk (along with the slides !)
in which you present interesting facts and/or solutions
to problems related to the material we have discussed
during the lectures,

OR

you briefly expose the ideas behind the solutions
to problems hinted at during the lectures
(Why does the failure detection in Cassandra actually work?
Why does Paxos work?
How did the Dynamo database influence the design of Cassandra?
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

   bds-2526-GROUPNAME.pdf

where GROUPNAME is the name of your group.
   
The file containing the slides must be pushed
into your github repository __at the latest on__
   
   December the 10th, 15:00
   
Any file not accessible starting from that time
will give your group the note 0.
