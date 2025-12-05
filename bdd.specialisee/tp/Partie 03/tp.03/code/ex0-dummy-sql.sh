#!/bin/bash

function query() {
    echo $1
    psql -U tito -d demo -c "$1"
}


query "DROP TABLE IF EXISTS dummy"
query "CREATE TABLE DUMMY (id int primary key, num int)"

for i in $(seq 10); do

    query "insert into dummy(id,num) values ("$i","$(($i % 2))");"

done

# SQL SEMANTICS: referential integrity
# ERROR, duplicate primary key 
query "insert into dummy(id,num) values (1,1053);"
