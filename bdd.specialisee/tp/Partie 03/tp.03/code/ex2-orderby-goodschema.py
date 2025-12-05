#!/bin/python3


from cassandra.cluster import Cluster


def init_dots(session) :
    session.execute('drop table if exists dotsgood')

    # Good data model:
    #
    # The clustering keys are indeed disctint within the partitions,
    # and can be used to sort data efficiently.
    # Crucially, every partition contains more than one row.
    #
    session.execute('create table dotsgood(id int, color text, primary key (color, id)) with clustering order by (id asc)')

    c = ['white','black']
    for i in range(0,10):
            session.execute('insert into dotsgood(id, color) values (%s,%s);', (i, c[i % 2]))



if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute('use demo')
    init_dots(session)

    print("\ndotsord ====================================")
    print("============================================")

    #rowsord = session.execute('select * from dotsgood')
    # 
    # Note that the order of ids is specified per partition in the table definition.
    #

    #rowsord = session.execute('select * from dotsgood where color=\'white\' order by id desc')
    #rowsord = session.execute('select * from dotsgood where color in (\'black\') order by id desc')
    #rowsord = session.execute('select * from dotsgood where color in (\'black\',\'white\') order by id desc')
    for r in rowsord:    
        print(r[0], r[1])

    cluster.shutdown()
