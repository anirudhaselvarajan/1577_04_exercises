/* --------------------------------------------------- Module 1 - Basic Statements ---------------------------------------------------*/

-- 1.	Create a database named training.

CREATE DATABASE training;
USE training;

-- 2.	Create a table ‘demography’ with the following columns inside training database
CREATE TABLE demography (
    custid INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    age INTEGER,
    gender VARCHAR(1),
    KEY (custid)
);

-- Cross check for table
SHOW TABLES;

-- 3.	Insert the following values into the table ‘demography’
	-- a.	Name=’John’, Age=25, Gender=’M’
    
INSERT INTO demography (custid, name, age, gender)
	VALUES (null, 'John', 25, 'M');

-- 4.	Insert the following values into the table ‘demography’ using a single query
	-- a.	Name = ’Pawan’, Age = 26, Gender=’M’
	-- b.	Name = ‘Hema’, Age=31, Gender=’F’
INSERT INTO demography (custid, name, age, gender)
	VALUES (null, 'Pawan', 26, 'M');
INSERT INTO demography (custid, name, age, gender)
	VALUES (null, 'Hema', 31, 'F');
    
-- Cross check for the results 
DESC demography;
SELECT 
    *
FROM
    demography;

-- 5.	Insert the following value into the table ‘demography’
-- a.	Name = ‘Rekha’, Gender=’F’
insert into demography (custid, name, gender)
	values (null, 'Rekha','F');

-- 6.	Retrieve all  rows and columns from table ‘demography’
SELECT 
    *
FROM
    demography;

-- 7.	Update the age to NULL for Name = ‘John’. Note that the NULL used here is MySQL NULL and not string NULL.
UPDATE demography 
SET 
    age = NULL
WHERE
    name = 'John';

-- 8.	Retrieve all the rows from table ‘demography’ where Age is NULL.
SELECT 
    *
FROM
    demography
WHERE
    age IS NULL;

-- 9.	Delete all the rows from the table ‘demography’.

DELETE FROM demography;

-- 10.	Drop the table ‘demography’

DROP TABLE demography;

/* ---------------------------------------------------Module -2 Where Clause -----------------------------------------------------------------*/
-- 1.	Retrieve the account ID, customer ID, and available balance for all accounts whose status equals 'ACTIVE' and whose available balance is greater than $2,500.

SELECT 
    account_id, cust_id, avail_balance
FROM
    account
WHERE
    status LIKE 'ACTIVE'
        AND avail_balance > 2500;

-- 2.	Construct a query that retrieves all accounts opened in 2002.

SELECT 
    *
FROM
    account
WHERE
    YEAR(open_date) = '2002';

-- 3.	Retrieve the account ID, available balance and pending balance for all accounts where available balance is not equal to pending balance.

SELECT 
    account_id, avail_balance, pending_balance
FROM
    account
WHERE
    avail_balance = pending_balance;

-- 4.	Retrieve account ID, Product code for the account ID’s 1,10,23,27

SELECT 
    account_id, product_cd
FROM
    account
WHERE
    account_id IN (1 , 10, 23, 27);

-- 5.	Retrieve account ID, available balance from all those accounts whose available balance is in between 100 and 200.

SELECT 
    account_id, avail_balance
FROM
    account
WHERE
    avail_balance BETWEEN 100 AND 200;


/* ---------------------------------------------------Module -3 - Operators and Functions -----------------------------------------------------------------*/

SELECT 
    COUNT(account_id)
FROM
    account;

-- 2.	Retrieve the first two rows from account table

SELECT 
    *
FROM
    account
LIMIT 2;

-- 3.	Retrieve the third and fourth row from account table.

SELECT 
    *
FROM
    account
LIMIT 2 , 2;

-- 4.	retrieve year of birth, month of birth, day of birth, weekday of birth for all the individuals from the table individual

SELECT 
    YEAR(birth_date),
    MONTH(birth_date),
    DAY(birth_date),
    WEEKDAY(birth_date)
FROM
    individual;

-- 5.	Write a query that returns the 17th through 25th characters of the string 'Please find the substring in this string'.

SELECT 
    SUBSTR('Please find the substring in this string',
        17,
        9);

-- 6.	Write a query that returns the absolute value and sign (-1, 0, or 1) of the number -25.76823.Also return the number rounded to the nearest hundredth.

SELECT 
    ABS(- 25.76823),
    SIGN(- 25.76823),
    ROUND(- 25.76823 / 100) * 100;

-- 7.	Write a query that adds 30 days to the current date.

SELECT DATE_ADD(CURDATE(), INTERVAL 30 DAY);

-- 8.	Retrieve the first three letters of first name and last three letters of last name from the table individual.

SELECT 
    LEFT(fname, 3), RIGHT(lname, 3)
FROM
    individual;

-- 9.	Retrieve the first names in Upper case from individual whose first name consists of five characters.

SELECT 
    UPPER(fname)
FROM
    individual
WHERE
    LENGTH(fname) = 5;

-- 10.	Retrieve the maximum balance and average balance from the account table for customer ID = 1.

SELECT 
    MAX(avail_balance), AVG(avail_balance)
FROM
    account
WHERE
    cust_id = 1;

/* ---------------------------------------------------Module -4 – Group by -----------------------------------------------------------------*/

-- 1.	Construct a query to count the number of accounts held by each customer. Show the customer ID and the number of accounts for each customer.

SELECT 
    cust_id, COUNT(cust_id) AS number_accounts
FROM
    account
GROUP BY cust_id;

-- 2.	Modify the previous query to fetch only those customers who has more than two accounts.

SELECT 
    cust_id, COUNT(cust_id) AS number_accounts
FROM
    account
GROUP BY cust_id
HAVING COUNT(cust_id) > 2;

-- 3.	Retrieve first name and date of birth from individual and sort them from youngest to oldest.

SELECT 
    fname, birth_date
FROM
    individual
ORDER BY birth_date DESC;

-- 4.	From the account table, retrieve the year of account opening (year part of open_date) and average 

SELECT 
    YEAR(open_date), AVG(avail_balance)
FROM
    account
GROUP BY YEAR(open_date)
HAVING AVG(avail_balance) > 200
ORDER BY YEAR(open_date);

-- 5.	Retrieve the product code and maximum pending balance for the product codes (CHK, SAV, CD)  present in account table. 

SELECT 
    product_cd, MAX(pending_balance)
FROM
    account
GROUP BY product_cd
HAVING product_cd IN ('CHK' , 'SAV', 'CD');

/* ---------------------------------------------------Module -5 – Joins and sub-query -----------------------------------------------------------------*/

-- 1.	Retrieve first name, title and department name by joining tables employee and department using department id.

SELECT 
    e.fname, e.title, d.name
FROM
    employee AS e
        INNER JOIN
    department AS d ON e.dept_id = d.dept_id;

-- 2.	Left join table product with table product_type (product_type left join product) to retrieve product_type.name and product.name from the tables.

SELECT 
    product_type.name, product.name
FROM
    product_type
        LEFT JOIN
    product ON product.product_type_cd = product_type.product_type_cd;

-- 3.	Using inner join, Retrieve the full employee name (fname followed by a space and then lname), Superior name (using superior_emp_id) from the employee table.

SELECT 
CONCAT(e.fname, ' ', e.lname) AS employee_name,
s.fname AS superior_name
FROM
    employee AS e,
    employee AS s
WHERE
    e.superior_emp_id = s.emp_id;

-- 4.	Using subquery, retrieve the fname and lname of the employees whose superior is ‘Susan Hawthorne’ from employee

SELECT 
    fname, lname
FROM
    employee
WHERE
    superior_emp_id IN (SELECT 
            emp_id
        FROM
            employee
        WHERE
            CONCAT(fname, ' ', lname) = 'Susan Hawthorne');

-- 5.	In employee table, retrieve the superior names (fname and lname) present in department 1. A person is superior if he/she is 

SELECT 
    CONCAT(fname, ' ', lname)
FROM
    employee
WHERE
    emp_id IN (SELECT 
            superior_emp_id
        FROM
            employee
        GROUP BY dept_id , superior_emp_id
        HAVING COUNT(superior_emp_id) > 1
            AND dept_id = 1);