#!/bin/python3

from cassandra.cluster import Cluster

def init_music(session):
    session.execute('drop table if exists songs')
    session.execute('drop table if exists artists')

    session.execute('create table songs(title text, band_name text, youtubeid text, primary key (title, band_name)) with clustering order by (band_name asc)')
    session.execute('create table artists(id int, name text, surname text, place text, primary key (id))')

    data = [["The Chariot", "The Cat Empire", "gg84LWWJIck"], 
            ["Primavera En La Selva", "Chicha Libre", "F0ktaNsBmAg"], 
            ["El Borrachito", "Chicha Libre", "P5XeR3fZuNg"], 
            ["Nissim", "The Gaslamp Killer", "Xt2IcK78NOw"],
            ["Ammazagh", "Terakaft", "tNmWUqVbCBo"],
            ["Gun Metal Grey", "The Budos Band", "8zeWL-7DALs"],
            ["Inquiry In Orient pt. 1", "Franco Bonfanti", "KZLhPfBEPho"],
            ["Full speed", "Claude Bolling", "xpOrBz5Yy0E"],
            ["Sospesi Nel Traffico", "Gianni Mazza",  "-55HkGzUMRA"],
            ["Asterix", "Gallowstreet","vNGWepH1Bwo"],
            ["Wa Tu Wa Zui","CHARLES KYNARD","sV0fHQlLwz0"],
            ["Disco Ulysses (Instrumental)","Vulfpeck","F7nCDrf90V8"],
            ["Lustful","Amedeo Minghi","TuX3jUf5KNI"],
            ["Guilty","Nicole Monique Wray","1B-nf_kbz20"],
            ["Shadow Boxing","Al Michels Affair","bBqZf_7fhEE"],
            ["Stormvogel","Jungle by Night","-D8P1821qmM"],
            ["Mustang (feat. Budos Band horns)","Blundetto","CEWysVLCf8Q"],
            ["Blam Blam Fever","The Valentines","ptARHBDU6dg"]
    ]

    for d in data:
        session.execute('insert into songs(title,band_name,youtubeid) values (%s,%s,%s);', d)
        

    data = [[0, "The Cat Empire", None, "Melbourne"],
            [1, "Chicha Libre", None, "New York"],
            [2, "The Gaslamp Killer", None, "New York"],
            [3, "Terakaft", None, "Mali/Algeria"],
            [4, "The Budos Band", None, "New York"],
            [5, "Franco", "Bonfanti", None],
            [6, "Gianni", "Mazza", "Rome"],
            [7, "Gallowstreet", None, "Amsterdam"],
            [8, "Charles", "Kynard", "St. Louis"],
            [9, "Vulfpeck", None, "Ann Arbor"],
            [10, "Amedeo", "Minghi", "Rome"],
            [11, "Nicole Monique", "Wray", "Salinas"],
            [12, "El Michels Affair", None, "New York"],
            [13, "Jungle by Night", None, "Amsterdam"],
            [13, "Blundetto", None, "Dijon"],
            [14,"The Valentines",None,"Kingston"]
            ]
    for d in data:
        session.execute('insert into artists (id, name , surname, place) values (%s,%s,%s,%s);', d)


def concat(a,b):
    if b == None:
        return a
    else:
        return (a + " " + b)


if __name__== "__main__":
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute('use demo')
    init_music(session)
        

    print("\n====================================")
    rowsS = session.execute('SELECT * FROM songs')
    for r in rowsS:
        print(r.title + " \t| \t " + r.band_name +  "\t | \t" + r.youtubeid)

    print("\n====================================")
    rowsA = session.execute('SELECT * FROM artists')
    for (a, b, c, d) in rowsA:    
        print(a, b, c, d)

    ## No CQLSH query to perform a join!
    ## We will have to code it explicitly via python.

    rowsS = session.execute('SELECT * FROM songs')
    print("\n====================================")
    for rs in rowsS:
        rowsA = session.execute('SELECT * FROM artists')
        for (a, name, place, surname) in rowsA:
             n = concat(name, surname)             
             if (rs.band_name == n and place != None):
                 print(rs.title + " \t| \t " + rs.band_name +  "\t | \t" + place + "\t | \t" + rs.youtubeid)

    cluster.shutdown()
