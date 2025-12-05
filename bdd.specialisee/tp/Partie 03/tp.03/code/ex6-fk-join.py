#!/bin/python3

import psycopg 

with psycopg.connect("user=tito", dbname="demo") as conn: 
    with conn.cursor() as cur:
        cur.execute("""drop table if exists artists cascade""")
        cur.execute("""drop table if exists songs cascade""")
        cur.execute("""create table artists(id int, name text, surname text, place text, primary key (id))""")
        cur.execute("""create table songs(title text, band_id int, url text, PRIMARY KEY (title, band_id), FOREIGN KEY (band_id) REFERENCES artists(id))""")


        data = [[0, "The Cat Empire", None, "Melbourne"],
            [1, "Chicha Libre", None, "New York"],
            [2, "The Gaslamp Killer", None, "New York"],
            [3, "Terakaft", None, "Mali/Algeria"],
            [4, "Jacques", "Brel",  "Schaarbeek/Brussels"],
            [5, "The Budos Band", None, "New York"]]


        for d in data:
            cur.execute("""insert into artists (id, name , surname, place) values (%s,%s,%s,%s);""", d)


        data = [["The Chariot", 0, "gg84LWWJIck"], 
                ["Primavera En La Selva", 1, "F0ktaNsBmAg"], 
                ["El Borrachito", 1, "P5XeR3fZuNg"], 
                ["Nissim", 2, "Xt2IcK78NOw"],
                ["Ammazagh", 3, "tNmWUqVbCBo"],
                ["Gun Metal Gray", 5, "8zeWL-7DALs"]]

        for d in data:
            cur.execute('insert into songs(title,band_id,url) values (%s,%s,%s);', d)        

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

    conn.commit()
