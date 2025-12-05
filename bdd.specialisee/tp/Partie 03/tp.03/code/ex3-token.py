#!/bin/python3


from cassandra.cluster import Cluster


def init_students(session) :
    session.execute('drop table students_tkn')

    #
    # Better definition, conceived with a view to optimising performances.
    #
    session.execute('create table students_tkn(sid int, uni text, surname text, name text, PRIMARY KEY ((uni, sid), surname))')

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
            session.execute('insert into students_tkn(sid,uni,surname,name) values (%s, %s, %s, %s)', (s[0], s[1], s[2], s[3]))


if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute('use demo')
    init_students(session)

    print("\n====================================")


    #rows = session.execute('select token(sid) from students_tkn')
    #rows = session.execute('select token(uid) from students_tkn')


    ## correct one
    # 
    # Arity matches the number of elements in the partition key of the table
    #
    rows = session.execute('select token(uni,sid) from students_tkn')
    
    

    for r in rows:    
        print(r[0])
    


    print("\n====================================")

    # WHERE clauses
    # 
    # The token function can be used in WHERE clauses. If it is the case
    # then all the comparisons in which it is used must involve only
    # token (i.e. values that can results from the application of the token function).

    rows0 = session.execute('select * from students_tkn where token(uni, sid) >= token(\'P7\', 1160220)')
    for r in rows0:
            print(r[0],r[1],r[2],r[3])



    print("\n====================================")

    # A limit on the number of produced rows can be handy ...
    #
    rows1 = session.execute('select * from students_tkn where token(uni, sid) > -4253202912485959508 limit 5')
    rows2 = session.execute('select * from students_tkn where token(uni, sid) >= 955255311006301821 limit 5')
    rows3 = session.execute('select * from students_tkn where token(uni, sid) >= 4719684253738045816 limit 5')
    
    # The use of limit give us a way to access a table
    # by indipendent chunks, and letting the server know
    # which are the nodes to contact.
    # This has one clear advantages: we can massively parallelise these queries.

    
    for rr in [rows1,rows2,rows3]:
        for r in rr:    
            print(r[0],r[1],r[2],r[3])


    cluster.shutdown()
