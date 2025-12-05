#!/bin/python3


from cassandra.cluster import Cluster


def init_students(session) :
    session.execute('drop table students')
    session.execute('drop table students_good')

    #
    # Naîve defiinition of a student table. Not satisfactory vis à vis performances.
    #
    session.execute('create table students(sid int PRIMARY KEY, uni text, surname text, name text)')


    #
    # Better definition, conceived with a view to optimising performances.
    #
    session.execute('create table students_good(sid int, uni text, surname text, name text, PRIMARY KEY ((uni), sid)) with clustering order by (sid desc)')

    students =  [[4201568,"P7","ABED","AMIR"],
                 [3202036,"P7","AIT MIMOUN","YASMINE"],
                 [1405644,"P7","AMARI","NABIL"],
                 [5531070,"P7","AMOURA","KARIM"],
                 [9496738,"P7","AU","PASCAL"],
                 [6160633,"P7","AYAD","BRAHAM"],
                 [5141851,"P7","BAI","YUCHEN"],
                 [9150123,"P7","BANNOUT","MARC"],
                 [8201751,"P7","BEN SALEM","KHOULOUD"],
                 [1160220,"P7","BETEND","MARIE"],
                 [1164220,"P7","BERNARDI","GIOVANNI"],
                 [5160249,"P5","TORDJMAN","GREG"],
                 [6170397,"P5","TRAORE","PAUL"],
                 [2996317,"P5","WANG","QI"],
                 [2199064,"P5","WANG","SHIYING"],
                 [3195735,"P5","XU","CHEN"],
                 [5160584,"P5","XU","STEPHANE"],
                 [4201750,"P5","YAKER","AMINE"],
                 [6160679,"P5","YVON","CONSTANCE"],
                 [6201049,"P5","ZAIDI","MOHAND AMEZIANE"],
                 [9156031,"P5","ZALAGH","HASSAN"]]

    for s in students:
            session.execute('insert into students(sid,uni,surname,name) values (%s, %s, %s, %s)', (s[0], s[1], s[2], s[3]))

            session.execute('insert into students_good(sid,uni,surname,name) values (%s, %s, %s, %s)', (s[0], s[1], s[2], s[3]))


if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute('use demo')
    init_students(session)

    print("\n====================================")


    # In general __do not__ ALLOW FILTERING !
    #
    # It might have a bad impact on performances: think of all servers
    # sending some thousands of rows, only 0.1% of which satisfy the 'WHERE' clause.
    #
    #rows = session.execute('select * from students where uni=\'P5\'')

    # Change the data model! 
    #
    rows = session.execute('select * from students_good where uni=\'P5\'')
    rows = session.execute('select * from students_good where uni=\'P7\'')
    
    # The right data modelling allow us to split queries into
    # smaller __ but possibly concurrent __ ones, with a further
    # advantage in performances.

    for r in rows:    
        print(r[0], r[1], r[2], r[3])


    cluster.shutdown()
