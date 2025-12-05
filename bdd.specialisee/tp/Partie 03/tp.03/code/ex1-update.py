#!/usr/bin/python3

from cassandra.cluster import Cluster


if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute('use demo')


    print("\nBEFORE THE UPDATES===================")
    print("=====================================\n")

    rows = session.execute('select * from dummy')
    for (a,b) in rows:
        print(a,b)


    # SQL semantics: UPDATE modifies __an existing__ given row
    session.execute('update dummy set num=54 where id=9')
    session.execute('update dummy set num=null where id=3')


    # CQL semantics: UPDATE acts as an INSERT ...
    session.execute('update dummy set num=1 where id=33')

    # CQL semantics: ... but only if at least one column 
    # outside the primary key is not null ...
    #
    # See https://issues.apache.org/jira/browse/CASSANDRA-11805
    #
    session.execute('update dummy set num=null where id=99')
    session.execute('insert into dummy(id,num) values (73,null);')



    print("\nAFTER THE UPDATES===================")
    print("====================================\n")
    rows = session.execute('select * from dummy')
    for (a,b) in rows:
        print(a,b)


    cluster.shutdown()
