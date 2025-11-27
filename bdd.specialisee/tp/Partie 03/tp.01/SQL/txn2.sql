CREATE OR REPLACE FUNCTION txn2()
RETURNS void as $$
BEGIN


update dots set color = 'white' where color = 'black';


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
