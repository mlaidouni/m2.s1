#!/bin/bash

function query() {
    echo $1
    sudo -u postgres psql -d sidemo -c "$1"
}

query "DROP TABLE dots"

query "create table dots (id int not null primary key, color text not null);"

query "insert into dots with x(id) as (select generate_series(1,10)) select id, case when id % 2 = 1 then 'black' else 'white' end from x;"

query "SELECT * FROM dots ORDER BY id DESC;"
