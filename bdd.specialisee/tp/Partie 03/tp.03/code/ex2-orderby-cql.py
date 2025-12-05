#!/bin/python3


from cassandra.cluster import Cluster


def init_dots(session) :
    # All the queries take place within the keyspace 'demo'

    session.execute('drop table if exists dots')
    session.execute('drop table if exists dots2')


    # Not a good data model:
    #
    # Clustering order takes places __per partition__ 
    # using the values in the clustering colums, that is
    # the part of the primary key that is not the partition key.
    # 
    # Here we have only _one row per partition_ !
    #
    session.execute(
        'create 
        table dots(id int, color text, primary key (id, color)) 
        with clustering order by (color desc)')

    c = ['white','black']
    for i in range(0,10):
            session.execute('insert into dots(id, color) values (%s,%s);', (i, c[i % 2]))


if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute('use demo')
    init_dots(session)

    #
    # Rows are apparently not ordered at all if no order by is given in the table definition
    #
    #rows = session.execute('select * from dots where color='black'')

    #
    # In passing note that we can limit the output
    #
    #rows = session.execute('select * from dots limit 6')
    #
    # In reality if no options are given, rows are ordered __by token__
    #
    #rows = session.execute('select token(id), id, color from dots')
    #
    # NOTE: the function 'token' cannot be applied if we select '*',
    # for instance the following select does _not_ work,
    #
    #rows = session.execute('select token(id),* from dots')


    # ORDER BY
    # 
    # All sorts of troubles, due the CQL semantics and the data model.
    #
    #rows = session.execute('select * from dots order by id desc')
    #rows = session.execute('select * from dots where id >= 0 and id <= 6 order by id desc')
    #rows = session.execute('select * from dots where id in (0,2,3,4,5,6,7,8,9) order by id desc')
    #
    #
    #
    # ORDER BY AND PAGING
    # In python some work is needed to disable PAGING,
    # while it is easy to disable it in cqlsh (PAGING OFF).
    # There was also a bug on this: https://datastax-oss.atlassian.net/browse/PYTHON-93
    #
    rows = session.execute('select * from dots where id in (0,2,3,4,5,6,7,8,9) order by color desc')
    #
    # The last query above sorks, but in practice is it rubbish.


    print("dots ====================================")
    print("=========================================")
    for r in rows:    
        print(r[0], r[1])#, r[2])


    cluster.shutdown()

    ## Essentially we are stuck, because of the data model
    ## (i.e. the keyspace schema), which forces our read queries
    ## to go against cassandra performances.
