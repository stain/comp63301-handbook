+++
title = "Query languages"
weight = 2
+++

Query languages are subset of _domain-specific languages_, which are intended for expressing the data question independent of the particular programming language or data storage mechanism that is used. A typical query language will contain elements of:

Focus
: From a connected data source, one of its list of entities are focused on, e.g. a table or entity type

Relations
: Expanding the focus by adding nested or referenced entities, e.g. by matching foreign keys to primary keys in other tables

Filtering
: Restricting the entities based on boolean criteria over their attributes, e.g. `age > 20`

Selection
: Returning a subset of attributes from the filtered entities

Query languages come with their own syntacic rules, and are typically submitted to the database as a formatted string, but may also be interpreted by an object-relational mapper (ORM).


## SQL

Structured Query Language (SQL; pronounced “sequel”) is an [established standard](https://blog.ansi.org/ansi/sql-standard-iso-iec-9075-2023-ansi-x3-135/) for querying relational databases. The language has evolved gradually since the 1970s, and is supported by current relational database management systems (RDMS), e.g. [Microsoft SQL Server](https://www.microsoft.com/sql-server), [Oracle Database](https://www.oracle.com/database/), [PostgreSQL](https://www.postgresql.org/), [MySQL](https://www.mysql.com/)/[MariaDB](https://mariadb.org/), [SQLite](https://www.sqlite.org/).

While setting up and connecting to an SQL database varies largely, SQL allows the _query_ to be expressed in a standard way, although with some variations that mainly affect database creation and modifications, e.g. datatype support for date ranges.

For instance, in SQL, the previous [programmatic query](programmatic.md) can be expressed as:

```sql
SELECT email
FROM customers
WHERE total_sales > 1000;
```

The keywords `SELECT` tells us which attributes to extract, `FROM` which tables to focus on, and `WHERE` which boolean filters to apply on the rows. The output of a SQL query is a new table with only the columns given in `SELECT`, returned to the calling program row by row. 

> [!TIP]
> A very simple, yet common query for exploring a SQL database is `SELECT * FROM customers` which would return the whole table with all columns. 

### Merging tables

A powerful feature of SQL is that multiple tables can be "merged" on the fly, typically using the `JOIN` operator combined with filtering on relational attributes:

```sql
SELECT
  email, 
  SUM(orders.amount) AS total_sales
FROM customers
INNER JOIN orders on orders.customer_id = customers.id;
GROUP BY
  customers.id
```

The above example relates in the `orders` table by matching its foreign key back to the customers primary key. This query also uses the `SUM` function to aggregate the `amount` numbers to a single sum for each customer (`GROUP BY`), rather than returning one row for each order for each customer.
 

> [!NOTE]
> SQL can be a very powerful tool for data querying, analysis and transformation, however care must be taken as to balancing what should be part of the SQL query, and what is easier done programmatically on the returned value.   While SQL allows database servers to optimise data access internally and reduce network traffic, being "too clever" in SQL may harm application performance or cause the database servers to carry the full cost of analytical computations. For instance, the above query is not able to return any calculated sums to the caller before it is certain there are no further orders for any of the customers.


See the [W3School SQL tutorial](https://www.w3schools.com/sql/) or [SQLite tutorial](https://www.sqlitetutorial.net/) for further details on using SQL.

### JPQL

Java Persistence Query Language

## GraphQL

## MongoDB queries

