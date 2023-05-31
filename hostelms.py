Q1. What is the difference between SQL and MySQL
SQL vs MySQL

SQL	MySQL
SQL is a standard language which stands for Structured Query Language based on the English language	MySQL is a database management system.
SQL is the core of the relational database which is used for accessing and managing database	
MySQL is an RDMS (Relational Database Management System) such as SQL Server, Informix etc.

Q2. What are the different subsets of SQL
Data Definition Language (DDL) – It allows you to perform various operations on the database such as CREATE, ALTER, and DELETE objects.
Data Manipulation Language(DML) – It allows you to access and manipulate data. It helps you to insert, update, delete and retrieve data from the database.
Data Control Language(DCL) – It allows you to control access to the database. Example – Grant, Revoke access permissions.
Q3. What do you mean by DBMS What are its different types
Database - SQL Interview Questions - EdurekaA Database Management System (DBMS) is a  software application that interacts with the user, applications, and the database itself to capture and analyze data. A database is a structured collection of data. 

A DBMS allows a user to interact with the database. The data stored in the database can be modified, retrieved and deleted and can be of any type like strings, numbers, images, etc.

There are two types of DBMS:

Relational Database Management System: The data is stored in relations (tables). Example – MySQL.
Non-Relational Database Management System: There is no concept of relations, tuples and attributes.  Example – MongoDB
Lets move to the next question in this SQL Interview Questions.

Q4. What is RDBMS How is it different from DBMS
A relational database management system (RDBMS) is a set of applications and features that allow IT professionals and others to develop, edit, administer, and interact with relational databases. Most commercial relational database management systems use Structured Query Language (SQL) to access the database, which is stored in the form of tables.
The RDBMS is the most widely used database system in businesses all over the world. It offers a stable means of storing and retrieving massive amounts of data.

Databases, in general, hold collections of data that may be accessed and used in other applications. The development, administration, and use of database platforms are all supported by a database management system.

A relational database management system (RDBMS) is a type of database management system (DBMS) that stores data in a row-based table structure that links related data components. An RDBMS contains functions that ensure the datas security, accuracy, integrity, and consistency. This is not the same as the file storage utilized by a database management system.

The following are some further distinctions between database management systems and relational database management systems:

The number of users who are permitted to utilise the system
A DBMS can only handle one user at a time, whereas an RDBMS can handle numerous users.
Hardware and software specifications
In comparison to an RDBMS, a DBMS requires fewer software and hardware.
Amount of information
RDBMSes can handle any quantity of data, from tiny to enormous, whereas DBMSes are limited to small amounts.
The structure of the database
Data is stored in a hierarchical format in a DBMS, whereas an RDBMS uses a table with headers that serve as column names and rows that hold the associated values.
Implementation of the ACID principle
The atomicity, consistency, isolation, and durability (ACID) concept is not used by DBMSs for data storage. RDBMSes, on the other hand, use the ACID model to organize their data and assure consistency.
Databases that are distributed
A DBMS will not provide complete support for distributed databases, whereas an RDBMS will.
Programs that are managed
A DBMS focuses on keeping databases that are present within the computer network and system hard discs, whereas an RDBMS helps manage relationships between its incorporated tables of data.
Normalization of databases is supported
A RDBMS can be normalized , but a DBMS cannot be normalized.

Q5. What is a Self-Join
A self-join is a type of join that can be used to connect two tables. As a result, it is a unary relationship. Each row of the table is attached to itself and all other rows of the same table in a self-join. As a result, a self-join is mostly used to combine and compare rows from the same database table.

Q6. What is the SELECT statement
A SELECT command gets zero or more rows from one or more database tables or views. The most frequent data manipulation language (DML) command is SELECT in most applications. SELECT queries define a result set, but not how to calculate it, because SQL is a declarative programming language.

Q7. What are some common clauses used with SELECT query in SQL
The following are some frequent SQL clauses used in conjunction with a SELECT query:

WHERE clause: In SQL, the WHERE clause is used to filter records that are required depending on certain criteria.
ORDER BY clause: The ORDER BY clause in SQL is used to sort data in ascending (ASC) or descending (DESC) order depending on specified field(s) (DESC).
GROUP BY clause: GROUP BY clause in SQL is used to group entries with identical data and may be used with aggregation methods to obtain summarised database results.
HAVING clause in SQL is used to filter records in combination with the GROUP BY clause. It is different from WHERE, since the WHERE clause cannot filter aggregated records.

Q8. What are UNION, MINUS and INTERSECT commands
The UNION operator is used to combine the results of two tables while also removing duplicate entries.
The MINUS operator is used to return rows from the first query but not from the second query.
The INTERSECT operator is used to combine the results of both queries into a single row.
Before running either of the above SQL statements, certain requirements must be satisfied 
Within the clause, each SELECT query must have the same amount of columns.
The data types in the columns must also be comparable.
In each SELECT statement, the columns must be in the same order.

Q9. What is Cursor How to use a Cursor
After any variable declaration, DECLARE a cursor. A SELECT Statement must always be coupled with the cursor definition.

To start the result set, move the cursor over it. Before obtaining rows from the result set, the OPEN statement must be executed.

To retrieve and go to the next row in the result set, use the FETCH command.

To disable the cursor, use the CLOSE command.

Finally, use the DEALLOCATE command to remove the cursor definition and free up the resources connected with it.

Q10. List the different types of relationships in SQL.
There are different types of relations in the database:

One-to-One – This is a connection between two tables in which each record in one table corresponds to the maximum of one record in the other.

One-to-Many and Many-to-One – This is the most frequent connection, in which a record in one table is linked to several records in another.

Many-to-Many – This is used when defining a relationship that requires several instances on each sides.

Self-Referencing Relationships – When a table has to declare a connection with itself, this is the method to employ.

Q12. What is OLTP?
OLTP, or online transactional processing, allows huge groups of people to execute massive amounts of database transactions in real time, usually via the internet. A database transaction occurs when data in a database is changed, inserted, deleted, or queried.

Q13. What are the differences between OLTP and OLAP?
OLTP stands for online transaction processing, whereas OLAP stands for online analytical processing. OLTP is an online database modification system, whereas OLAP is an online database query response system.

Q14. How to create empty tables with the same structure as another table?
To create empty tables:
Using the INTO operator to fetch the records of one table into a new table while setting a WHERE clause to false for all entries, it is possible to create empty tables with the same structure. As a result, SQL creates a new table with a duplicate structure to accept the fetched entries, but nothing is stored into the new table since the WHERE clause is active.

Q15. What is PostgreSQL?
In 1986, a team lead by Computer Science Professor Michael Stonebraker created PostgreSQL under the name Postgres. It was created to aid developers in the development of enterprise-level applications by ensuring data integrity and fault tolerance in systems. PostgreSQL is an enterprise-level, versatile, resilient, open-source, object-relational database management system that supports variable workloads and concurrent users. The international developer community has constantly backed it. PostgreSQL has achieved significant appeal among developers because to its fault-tolerant characteristics.
It’s a very reliable database management system, with more than two decades of community work to thank for its high levels of resiliency, integrity, and accuracy. Many online, mobile, geospatial, and analytics applications utilise PostgreSQL as their primary data storage or data warehouse.

Q16. What are SQL comments?
SQL Comments are used to clarify portions of SQL statements and to prevent SQL statements from being executed. Comments are quite important in many programming languages. The comments are not supported by a Microsoft Access database. As a result, the Microsoft Access database is used in the examples in Mozilla Firefox and Microsoft Edge.
Single Line Comments: It starts with two consecutive hyphens (–).
Multi-line Comments: It starts with /* and ends with */.

Q17. What is the usage of the NVL() function?
You may use the NVL function to replace null values with a default value. The function returns the value of the second parameter if the first parameter is null. If the first parameter is anything other than null, it is left alone.

This function is used in Oracle, not in SQL and MySQL. Instead of NVL() function, MySQL have IFNULL() and SQL Server have ISNULL() function.

Let’s move to the next question in this SQL Interview Questions.

Q18. Explain character-manipulation functions? Explains its different types in SQL.
Change, extract, and edit the character string using character manipulation routines. The function will do its action on the input strings and return the result when one or more characters and words are supplied into it.

The character manipulation functions in SQL are as follows:

A) CONCAT (joining two or more values): This function is used to join two or more values together. The second string is always appended to the end of the first string.

B) SUBSTR: This function returns a segment of a string from a given start point to a given endpoint.

C) LENGTH: This function returns the length of the string in numerical form, including blank spaces.

D) INSTR: This function calculates the precise numeric location of a character or word in a string.

E) LPAD: For right-justified values, it returns the padding of the left-side character value.

F) RPAD: For a left-justified value, it returns the padding of the right-side character value.

G) TRIM: This function removes all defined characters from the beginning, end, or both ends of a string. It also reduced the amount of wasted space.

H) REPLACE: This function replaces all instances of a word or a section of a string (substring) with the other string value specified.

Q19. Write the SQL query to get the third maximum salary of an employee from a table named employees.
Employee table

employee_name	salary
A	24000
C	34000
D	55000
E	75000
F	21000
G	40000
H	50000
 

SELECT * FROM(

SELECT employee_name, salary, DENSE_RANK() 

OVER(ORDER BY salary DESC)r FROM Employee) 

WHERE r=&n;

To find 3rd highest salary set n = 3

Q20. What is the difference between the RANK() and DENSE_RANK() functions?
The RANK() function in the result set defines the rank of each row within your ordered partition. If both rows have the same rank, the next number in the ranking will be the previous rank plus a number of duplicates. If we have three records at rank 4, for example, the next level indicated is 7.

The DENSE_RANK() function assigns a distinct rank to each row within a partition based on the provided column value, with no gaps. It always indicates a ranking in order of precedence. This function will assign the same rank to the two rows if they have the same rank, with the next rank being the next consecutive number. If we have three records at rank 4, for example, the next level indicated is 5.

Q21. What are Tables and Fields?

A table is a collection of data components organized in rows and columns in a relational database. A table can also be thought of as a useful representation of relationships. The most basic form of data storage is the table. An example of an Employee table is shown below.

ID	Name	Department	Salary
1	Rahul	Sales	24000
2	Rohini	Marketing	34000
3	Shylesh	Sales	24000
4	Tarun	Analytics	30000
 

A Record or Row is a single entry in a table. In a table, a record represents a collection of connected data. The Employee table, for example, has four records.

A table is made up of numerous records (rows), each of which can be split down into smaller units called Fields(columns). ID, Name, Department, and Salary are the four fields in the Employee table above.

Q22. What is a UNIQUE constraint?
The UNIQUE Constraint prevents identical values in a column from appearing in two records. The UNIQUE constraint guarantees that every value in a column is unique.

Q23. What is a Self-Join?
A self-join is a type of join that can be used to connect two tables. As a result, it is a unary relationship. Each row of the table is attached to itself and all other rows of the same table in a self-join. As a result, a self-join is mostly used to combine and compare rows from the same database table.

Q24. What is the SELECT statement?
A SELECT command gets zero or more rows from one or more database tables or views. The most frequent data manipulation language (DML) command is SELECT in most applications. SELECT queries define a result set, but not how to calculate it, because SQL is a declarative programming language.

Q25. What are some common clauses used with SELECT query in SQL?
The following are some frequent SQL clauses used in conjunction with a SELECT query:

Course Curriculum
Microsoft SQL Server Certification Course
WHERE clause: In SQL, the WHERE clause is used to filter records that are required depending on certain criteria.
ORDER BY clause: The ORDER BY clause in SQL is used to sort data in ascending (ASC) or descending (DESC) order depending on specified field(s) (DESC).
GROUP BY clause: GROUP BY clause in SQL is used to group entries with identical data and may be used with aggregation methods to obtain summarised database results.
HAVING clause in SQL is used to filter records in combination with the GROUP BY clause. It is different from WHERE, since the WHERE clause cannot filter aggregated records.

Q26. What are UNION, MINUS and INTERSECT commands?
The UNION operator is used to combine the results of two tables while also removing duplicate entries. 

The MINUS operator is used to return rows from the first query but not from the second query. 

The INTERSECT operator is used to combine the results of both queries into a single row.
Before running either of the above SQL statements, certain requirements must be satisfied –

Within the clause, each SELECT query must have the same amount of columns.

The data types in the columns must also be comparable.

In each SELECT statement, the columns must be in the same order.

Let’s move to the next question in this SQL Interview Questions.

Q27. What is Cursor? How to use a Cursor?
After any variable declaration, DECLARE a cursor. A SELECT Statement must always be coupled with the cursor definition.

To start the result set, move the cursor over it. Before obtaining rows from the result set, the OPEN statement must be executed.

To retrieve and go to the next row in the result set, use the FETCH command.

To disable the cursor, use the CLOSE command.

Finally, use the DEALLOCATE command to remove the cursor definition and free up the resources connected with it.

Q28. List the different types of relationships in SQL.
There are different types of relations in the database:
One-to-One – This is a connection between two tables in which each record in one table corresponds to the maximum of one record in the other.
One-to-Many and Many-to-One – This is the most frequent connection, in which a record in one table is linked to several records in another.
Many-to-Many – This is used when defining a relationship that requires several instances on each sides.
Self-Referencing Relationships – When a table has to declare a connection with itself, this is the method to employ.

Q29. What is SQL example?
SQL is a database query language that allows you to edit, remove, and request data from databases. The following statements are a few examples of SQL statements:

SELECT 
INSERT 
UPDATE
DELETE
CREATE DATABASE
ALTER DATABASE
Q30. What are basic SQL skills?
SQL skills aid data analysts in the creation, maintenance, and retrieval of data from relational databases, which divide data into columns and rows. It also enables users to efficiently retrieve, update, manipulate, insert, and alter data.

The most fundamental abilities that a SQL expert should possess are:

Database Management
Structuring a Database
Creating SQL clauses and statements
SQL System SKills like MYSQL, PostgreSQL
PHP expertise is useful.
Analyze SQL data
Using WAMP with SQL to create a database
OLAP Skills
Q31. What is schema in SQL Server?

A schema is a visual representation of the database that is logical. It builds and specifies the relationships among the database’s numerous entities. It refers to the several kinds of constraints that may be applied to a database. It also describes the various data kinds. It may also be used on Tables and Views.

Schemas come in a variety of shapes and sizes. Star schema and Snowflake schema are two of the most popular. The entities in a star schema are represented in a star form, whereas those in a snowflake schema are shown in a snowflake shape.
Any database architecture is built on the foundation of schemas.

Q32. How to create a temp table in SQL Server?
Temporary tables are created in TempDB and are erased automatically after the last connection is closed. We may use Temporary Tables to store and process interim results. When we need to store temporary data, temporary tables come in handy.

The following is the syntax for creating a Temporary Table:

CREATE TABLE #Employee (id INT, name VARCHAR(25))
INSERT INTO #Employee VALUES (01, ‘Ashish’), (02, ‘Atul’)

Let’s move to the next question in this SQL Interview Questions.


Q33. How to install SQL Server in Windows 11?

Install SQL Server Management Studio In Windows 11

Step 1: Click on SSMS, which will take you to the SQL Server Management Studio page.

Step 2: Moreover, click on the SQL Server Management Studio link and tap on Save File. 

Step 3: Save this file to your local drive and go to the folder.

Step 4: The setup window will appear, and here you can choose the location where you want to save the file.
Step 5: Click on Install.
Step 6: Close the window after the installation is complete.
Step 7: Furthermore, go back to your Start Menu and search for SQL server management studio.

Step 8: Furthermore, double-click on it, and the login page will appear once it shows up.

Step 9: You should be able to see your server name. However, if that’s not visible, click on the drop-down arrow on the server and tap on Browse.

Step 10: Choose your SQL server and click on Connect.

After that, the SQL server will connect, and Windows 11 will run good.

Q34. What is the case when in SQL Server?
The CASE statement is used to construct logic in which one column’s value is determined by the values of other columns.

At least one set of WHEN and THEN commands makes up the SQL Server CASE Statement. The condition to be tested is specified by the WHEN statement. If the WHEN condition returns TRUE, the THEN sentence explains what to do.

When none of the WHEN conditions return true, the ELSE statement is executed. The END keyword brings the CASE statement to a close.

1
2
3
4
5
6
CASE
WHEN condition1 THEN result1
WHEN condition2 THEN result2
WHEN conditionN THEN resultN
ELSE result
END;

Q35. NoSQL vs SQL

In summary, the following are the five major distinctions between SQL and NoSQL:

Relational databases are SQL, while non-relational databases are NoSQL.

SQL databases have a specified schema and employ structured query language. For unstructured data, NoSQL databases use dynamic schemas.

SQL databases scale vertically, but NoSQL databases scale horizontally.

NoSQL databases are document, key-value, graph, or wide-column stores, whereas SQL databases are table-based.

SQL databases excel in multi-row transactions, while NoSQL excels at unstructured data such as documents and JSON.

 

Q36. What is the difference between NOW() and CURRENT_DATE()?
NOW() returns a constant time that indicates the time at which the statement began to execute. (Within a stored function or trigger, NOW() returns the time at which the function or triggering statement began to execute.
The simple difference between NOW() and CURRENT_DATE() is that NOW() will fetch the current date and time both in format ‘YYYY-MM_DD HH:MM:SS’ while CURRENT_DATE() will fetch the date of the current day ‘YYYY-MM_DD’.

Let’s move to the next question in this SQL Interview Questions.

Q37. What is BLOB and TEXT in MySQL?

BLOB stands for Binary Huge Objects and can be used to store binary data, whereas TEXT may be used to store a large number of strings. BLOB may be used to store binary data, which includes images, movies, audio, and applications.
BLOB values function similarly to byte strings, and they lack a character set. As a result, bytes’ numeric values are completely dependent on comparison and sorting.
    TEXT values behave similarly to a character string or a non-binary string. The comparison/sorting of TEXT is completely dependent on the character set collection.

Q38. How to remove duplicate rows in SQL?

If the SQL table has duplicate rows, the duplicate rows must be removed.

Let’s assume the following table as our dataset:

 

ID	Name	Age
1	A	21
2	B	23
2	B	23
4	D	22
5	E	25
6	G	26
5	E	25
The following SQL query removes the duplicate ids from the  table:

DELETE FROM table WHERE ID IN (
SELECT 
ID, COUNT(ID) 
FROM   table
GROUP BY  ID
HAVING 
COUNT (ID) > 1); 

Q39. How to create a stored procedure using SQL Server?

A stored procedure is a piece of prepared SQL code that you can save and reuse again and over.
So, if you have a SQL query that you create frequently, save it as a stored procedure and then call it to run it.
You may also supply parameters to a stored procedure so that it can act based on the value(s) of the parameter(s) given.

Stored Procedure Syntax

CREATE PROCEDURE procedure_name

AS

sql_statement

GO;

Execute a Stored Procedure

EXEC procedure_name;


Q40. What is Database Black Box Testing?

Black Box Testing is a software testing approach that involves testing the functions of software applications without knowing the internal code structure, implementation details, or internal routes. Black Box Testing is a type of software testing that focuses on the input and output of software applications and is totally driven by software requirements and specifications. Behavioral testing is another name for it.

