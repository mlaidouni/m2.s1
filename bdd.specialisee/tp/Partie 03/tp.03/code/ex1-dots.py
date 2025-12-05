#!/bin/python3


from cassandra.cluster import Cluster


def init_dots(session) :
    session.execute('drop table dots')
    session.execute('drop table dotsord')

    #
    #'not null' not available in CQL
    #
    #session.execute('create table dots(id int, color text, primary key (id)) with comment=\'boring table and no double thinking about it.\'')


    # Not a good solution,
    # clustering order takes places __per partition__
    #
    session.execute('create table dots(id int, color text, primary key (id, color)) with clustering order by (color desc)')


    session.execute('create table dotsORD(id int, color text, primary key (color, id)) with clustering order by (id asc)')
    #session.execute('create table dots(id int, color text, primary key (color, id))')

    c = ['white','black']
    for i in range(0,10):
            session.execute('insert into dots(id, color) values (%s,%s);', (i, c[i % 2]))
            session.execute('insert into dotsORD(id, color) values (%s,%s);', (i, c[i % 2]))


if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute('use demo')
    init_dots(session)

    print("\n====================================")

    #
    # Rows are apparently not ordered at all if no order by is given the table definition
    #
    #rows = session.execute('select * from dots')
    #rows = session.execute('select * from dots limit 5')
    
    #
    # If no options are given, rows are ordered __by token__
    #
    #rows = session.execute('select token(id),id,color from dots')


    # ORDER BY
    #rows = session.execute('select * from dots order by id desc')
    #rows = session.execute('select * from dots where id >= 0 and id <= 6 order by id desc')
    #rows = session.execute('select * from dots where id in (0,2,3,4,5,6,7,8,9) order by id desc')


    ## change data model!

    # ODER BY AND PAGING
    # In python work is needed to disable PAGING (easy in cqlsh: PAGING OFF)  
    # There was also a bug on this: https://datastax-oss.atlassian.net/browse/PYTHON-93
    #
    #rows = session.execute('select * from dots where color=\'black\' order by id desc')
    #rows = session.execute('select * from dots where color in (\'black\',\'white\') order by id desc')


    #rowsord = session.execute('select * from dotsord')
    rowsord = session.execute('select * from dotsord where color=\'black\' order by id desc')
    #rowsord = session.execute('select * from dotsord where color in (\'black\') order by id desc')
    #rowsord = session.execute('select * from dotsord where color in (\'black\',\'white\') order by id desc')
    for r in rowsord:    
        print(r[0], r[1])#, r[2])


    # WHERE and ALLOW FILTERING 
    # Try query with naïve definition of dots (where 'color' is a clustering key)
    # rows = session.execute('select * from dots where color=\'black\'')

    for r in rows:    
        print(r[0], r[1])#, r[2])


    cluster.shutdown()
