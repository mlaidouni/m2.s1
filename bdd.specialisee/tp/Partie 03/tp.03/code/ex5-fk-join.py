#!/bin/python3

from psycopg2 import connect, extensions, sql

def initDBs() :
    conn = connect("user=tito")

    #Make sure we are not into a transaction
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    #    conn.set_isolation_level( extensions.ISOLATION_LEVEL_SERIALIZABLE )

    cur  = conn.cursor()
    cur.execute(sql.SQL("DROP DATABASE IF EXISTS  music"))
    cur.execute(sql.SQL("CREATE DATABASE music"))
    cur.close()
    conn.close()


if __name__== "__main__":
    initDBs()

    conn = connect("dbname=music user=tito")
    cur  = conn.cursor()


    cur.execute('create table artists(id int, name text, surname text, place text, primary key (id))')
    cur.execute('create table songs(title text, band_id int, url text, PRIMARY KEY (title, band_id), FOREIGN KEY (band_id) REFERENCES artists(id))')


    data = [[0, "The Cat Empire", None, "Melbourne"],
            [1, "Chicha Libre", None, "New York"],
            [2, "The Gaslamp Killer", None, "New York"],
            [3, "Terakaft", None, "Mali/Algeria"],
            [4, "Jacques", "Brel",  "Schaarbeek/Brussels"],
            [5, "The Budos Band", None, "New York"]]


    for d in data:
        cur.execute('insert into artists (id, name , surname, place) values (%s,%s,%s,%s);', d)


    data = [["The Chariot", 0, "gg84LWWJIck"], 
            ["Primavera En La Selva", 1, "F0ktaNsBmAg"], 
            ["El Borrachito", 1, "P5XeR3fZuNg"], 
            ["Nissim", 2, "Xt2IcK78NOw"],
            ["Ammazagh", 3, "tNmWUqVbCBo"],
            ["Gun Metal Gray", 5, "8zeWL-7DALs"]]

    for d in data:
        cur.execute('insert into songs(title,band_id,url) values (%s,%s,%s);', d)        



    conn.commit()

    cur.execute('SELECT * FROM songs')
    print("\n====================================")
    rows = cur.fetchall()
    for r in rows:
        print(r[0] + " \t| \t " + str(r[1]) +  "\t | \t" + r[2])

    cur.execute('SELECT * FROM artists')
    print("\n====================================")
    rows = cur.fetchall()
    for (a, b, c, d) in rows:    
        print(a, b, c, d)


    cur.execute('SELECT title,name,place,url FROM songs INNER JOIN artists ON (band_id = id)')
    print("\n====================================")
    rows = cur.fetchall()
    for r in rows:    
        print(r)

    cur.close()
    conn.close()
