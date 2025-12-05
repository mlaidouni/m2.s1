#!/usr/bin/python3

from cassandra.cluster import Cluster

if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute('DROP KEYSPACE IF EXISTS  demo')
    #     # If you run a __single node__ cluster the
    #     #
    #     # NetworkTopologyStrategy 
    #     #
    #     # might lead to a "NoHostAvailable" error at insertion time.
    #     # When playing on a single machine it is easier to use "SimpleStretegy".
    #     #
    #     # To solve the issue we alter the replication strategy of the keyspace
    #     #
    session.execute('CREATE KEYSPACE demo WITH replication = {\'class\': \'NetworkTopologyStrategy\', \'replication_factor\': 3}');

    session.execute('use demo')

    # Create a table to 
    # (1) force an error if the proper replication strategy is not used.
    #     See comment above.
    #
    # (2) Discuss INSERT and duplicate primary keys.
    #
    session.execute('create table dummy(id int primary key, num int)')

    for i in range(0,10):
        session.execute('insert into dummy(id,num) values (%s,%s);', (i, i % 2))


    ## EXAMPLE TO BE DISCUSSED WHEN TALKING ABOUT SEMANTICS OF INSERT
    # CQL semantics:
    # - overwrite row
    # - no referential integrity
    session.execute('insert into dummy(id,num) values (%s,%s);', (0,1053))

    cluster.shutdown()
