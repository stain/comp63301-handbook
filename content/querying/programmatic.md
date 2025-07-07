+++
title = "Programmatic queries"
weight = 1
+++


In its simplest form, a _query_ can be considered a programmatic iteration over the data, with some conditionals to _filter_, and a _selection_ of attributes to return.

```python
import corp.database as db
for customer in db.customers:
  if customer.total_sales > 1000:
    print(customer.email)
```

The code above examplifies querying for high value customers for promotion purposes. The `for` block loops over the database `customers`, with each rows filtered by the attribute `total_sales` above the threshold of £1000. The attribute `email` is selected and printed on screen. 

While it is possible to write queries programmatically as above, this will require the dataset to be accessible as objects in memory. For instance, in a single-process consumption of a small CSV file of less than a million rows, this can seem perfectly reasonable, and may even be more efficient than following the Data Engineering Lifecycle covered by this handbook. 

In reality, however, data engineering is seldom as simple as in the above code. For instance, the organisation may have **multiple sources** of customers (e.g. covering UK and Ireland). The total sales may not be **pre-calculated**, but needs to be **aggregated** as a sum of transactions within a given time period. Discounts and refunds may need to be **excluded**, and amounts  **transformed** from different currencies.  Finally, when **selecting** the contact address, customers will have given preferences for email vs. text message vs. phone call vs. no contact at all.

Data engineering frameworks can be used to emulate memory access of data objects, allowing programmatic queries to be coded almost as in this basic example.


## Object–relational mapping

An Object-Relational Mapping (ORM) is a common mechanism for accessing relational databases in object-oriented programming languages, as if each database table correspond to a class of objects which attributes correspond to the table columns. 

For instance, using the [Jakarta Persistence API](https://projects.eclipse.org/projects/ee4j.jpa) (JPA) for Java, commonly used a class `Customer` can be defined to map the table `customers` in a relational database:

```java
@Entity
@Table(name = "customers")
public class Customer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "total_sales")
    private int total_sales;

    @Column(name = "email")
    private String email;
}
```

With the addition of the connection details to the database, this will allow programmatic queries where the database rows are mapped into object instances and the columns to attributes on the object:

```java
for (Customer customer : customerRepository.findAll()) {
  if (customer.total_sales > 1000) {
    System.out.println(customer.email);
  }
}
```

However, it is worth noting that using the ORM framework's support for queries will be much more efficient than the above code, which in effect will always transfer the whole table from the database to the program. For instance, in JPA, a query to look up from a table given a particular attribute can be added, allowing the database to only transfer the matching rows. 

```java
public interface CustomerRepository extends Repository<Customer, Long> {

  List<Customer> findByEmail(String email);
}
```

Common ORMs for Python include [SQLAlchemy](https://www.sqlalchemy.org/), [Django ORM](https://docs.djangoproject.com/en/5.2/topics/db/queries/), [Peewee](https://docs.peewee-orm.com/).

> [!info]
> As the job of an ORM is to make relational databases behave more like in-memory data structures, there can be large variations in how the same database is represented in different programming languages and across different ORMs. ORMs typically assume they are used also to define a database schema and to populate the database -- acting as a persistence layer. Therefore a given ORM may not be suitable for querying any relational database.


## Pandas 

In Python, the [pandas](https://pandas.pydata.org/) framework uses the concept of _Data frames_ to allow programmatic queries on tabular datasets, presenting them as list-like structures, even if data is loaded on demand.

A data frame can be loaded from multiple data sources, including CSV files, 

See the [Getting started with pandas tutorial](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html) and [chapter 5 in Python for data analysis](https://wesmckinney.com/book/pandas-basics) for a step-wise introduction to using pandas data frames.


