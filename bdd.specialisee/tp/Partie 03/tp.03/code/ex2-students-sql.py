#!/bin/python3

from psycopg2 import connect, extensions, sql


def initDBs() :
    conn = connect("user=tito")

    #Make sure we are not into a transaction
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    #    conn.set_isolation_level( extensions.ISOLATION_LEVEL_SERIALIZABLE )

    cur  = conn.cursor()
    cur.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier("students")))

    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("students")))
    cur.close()
    conn.close()


if __name__== "__main__":
    initDBs()

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

    conn = connect("dbname=students user=tito")
    cur  = conn.cursor()
    cur.execute(sql.SQL("CREATE TABLE students (sid int PRIMARY KEY, uni text, surname text, name text)"))

    for s in students:
        cur.execute("INSERT INTO students(sid,uni,surname,name) values (%s, %s, %s, %s)", (s[0], s[1], s[2], s[3]))


    cur.execute(sql.SQL("select * from students where uni='P5'"))
    rows = cur.fetchall()
    for r in rows:
        print(str(r[0]) +", "+ r[1] +", "+ r[2] +", "+r[3])
    
    conn.commit()
    cur.close()
    conn.close()

    
