CREATE OR REPLACE FUNCTION init()
RETURNS void as $$
BEGIN

drop table if exists dots;
create table dots
  (
    id int not null primary key,
    color text not null
  );


insert into dots
  with x(id) as (select generate_series(1,10))
  select id, case when id % 2 = 1 then 'black'
    else 'white' end from x;


-- commit;

/* The commit is commented out to avoid the 
*
* ERROR:  invalid transaction termination
*
* from within PSQL. See
* 
* https://stackoverflow.com/questions/53214740/error-invalid-transaction-termination-when-trying-to-execute-a-procedure-with
* 
*/

END;
$$ LANGUAGE 'plpgsql'
