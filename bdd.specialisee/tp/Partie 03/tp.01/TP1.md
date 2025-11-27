TP1 Bases de données spécialisées
2025 - 2026


# LITERATURE


## Cables

Find _two_ non academic articles about unsersea cables
that are _not_ already mentioned in the slides.
Give their references and outlined why do you think that
the articles you selected are worth reading.


## Eventual consistency

Which are the most recent academic articles 
and blog posts on eventual consistency ?

## Society

Find one article not mentioned in the slides
that presentes / discusses some actual impact
of distributed systems on society.



# WARM UP

## Install the Postgres server on your machine.
Which are the steps to do to install it ?
Have you had any problem to install and run it ?


## Configure a Postgres server.
Use an isolation level weaker than SERIALIZABLE.
Can you execute one of the write skew examples in

	https://wiki.postgresql.org/wiki/SSI
		
Which example have you chosen ? __Why__ ?
Can you come up with an example of write skew __of your own__ ?
 

## Configure the Postgres server.
Use the isolation level SERIALIZABLE 
and run again the same example.
Did everything work as expected ?
What does "work as expected" means ?


## Last question on PostgreSQL.
Which isolation levels in Postgres allow the write skew anomaly ?



# A LITTLE TWIST

## Install MySQL server on your machine.
Which are the steps to do to install it ?
Have you had any problem to install and run it ?


## Can you generate anomalies (lost update, write skew, ...)
   on a MySQL DB ?
   If yes, on which isolation levels ?
   Using which SQL code ?
   If not, why not ?


# REAL WORLD CODE

## Clone the BenchBase repository using the following instructions
  in your BASH,

  git clone --depth 1 https://github.com/cmu-db/benchbase.git


## To build the project it should be enough to run the instructions

  $ cd benchbase
  $ ./mvnw clean package

  Do they work ?
  If not, why not ?
  How have you solved the problems (if any) ?


## Now focus on the benchmark code in the directory

  benchbase/src/main/java/com/oltpbenchmark/benchmarks/tpcc

  Can you make the code compile and run on your PostgreSQL server ?
  If yes, why and how ?
  If not, why not ?

	
# TEAMS

Form a group with three other students (i.e. no more than 4 students
per group, and no less than 3).
   
Send to the addr "gio X irif.fr" an e-mail with subject
   
   [bds-2526] group: group_name

where `group_name` is the name of your group.
The e-mail must have in attachment a csv file 
containing the details about the group members,
in the following format:

   student number1;surname1;name1
   student number2;surname2;name2

One e-mail per group suffices.
The format of the subject and of the csv file __must__ be respected
(-1 point in the final note for any mistake).

THE EMAILS MUST BE RECEVIED AT THE LATEST BY

November the 26th, 23:59.
