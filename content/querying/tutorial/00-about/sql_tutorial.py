#!/usr/bin/env python
# coding: utf-8

# This tutorial is based on the [Library Carpentry SQL tutorial](https://librarycarpentry.github.io/lc-sql/), licensed under [CC-BY 4.0](https://librarycarpentry.github.io/lc-sql/LICENSE.html).
# 
# You can run this Jupyter notebook in [Google Colab](https://colab.research.google.com/) or on your local installation.
# 
# **Note**: In Colab, if the notebook is View Only, remember to make a copy, so that you can modify it:
# 
# * _File --> Save a copy in Drive_.
# 
# 
# ## Attribution
# 
# Jordan Perdersen (Ed.), Kristin Lee (Ed.), Christopher Erdmann (Ed.), Lise Doucette (Ed.), Elaine Wong (Ed.), Janice Chan (Ed.), James Baker, Fernando Rios, Tim Dennis, Belinda Weaver, … orobecca. (2019, July). **LibraryCarpentry/lc-sql: Library Carpentry: Introduction to SQL, June 2019** (Version v2019.06.1). _Zenodo_. http://doi.org/10.5281/zenodo.3266102
# 
# [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3266102.svg)](https://doi.org/10.5281/zenodo.3266102)
# 
# ### Modifications
# 
# Extracts modified to Jupyter notebook use by Stian Soiland-Reyes <https://orcid.org/0000-0001-9842-9718>.
# 
# ### References
# 
# * <https://pythonspot.com/sqlite-database-with-pandas/>
# * <https://pythoncourses.gumroad.com/l/KmxqY>
# * <https://www.sqlitetutorial.net/>
# * <https://wesmckinney.com/book/pandas-basics>


import os


# # Data ingestion
# 
# In this tutorial we assume data has already been ingested and cleaned. We'll retrieve the already prepared SQLite database.
# 
# [SQLite](https://sqlite.org/) is a miniature relational database that can be used without a server installation, for instance by directly importing the SQLite library in Python and "connecting" it to a local file. It is worth noting that this means only a single process can access the file at a time (in this case our Jupyter notebook).
# 
# ## Download SQLite database
# 
# The Zenodo deposit <https://doi.org/10.5281/zenodo.8360812> contains a ZIP file with the pre-populated database in SQLite format. As this tutorial is not showing "proper" data ingestion, we'll just download and unzip using Linux shell commands:
# 
# 

# In[ ]:


os.system('wget https://zenodo.org/records/8360812/files/doaj-article-sample-db.zip && unzip doaj-article-sample-db.zip')


# Now let's connect to this database from within Python using the [sqlite3](https://docs.python.org/3/library/sqlite3.html) library, and see which tables are included. In SQLite this can be done by inspecting the `sqlite_master` table, using the `SELECT *` query . We'll use [pandas](https://pandas.pydata.org/) as a helper to better view the SQL results in Jupyter Notebook.
# 
# 

# In[ ]:


import sqlite3
import pandas as pd

db = sqlite3.connect("doaj-article-sample.db")
pd.read_sql_query("SELECT * FROM sqlite_master", db)


# # Introduction to SQL
# 
# In this tutorial we'll follow the Library Carpentry guide, but run the queries from within Python instead of the DB Browser.  
# 
# * Read through [Section 1: Introduction to SQL](https://librarycarpentry.github.io/lc-sql/01-introduction.html)  (ignoring the _DB Browser_ subsection).
# 

# 
# # Selecting and querying data
# 
# Next, follow the [Section 2: Selecting and sorting data](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html). Use Python's `"""` strings to support multiple lines.
# 
# Note that you don't need to use `print()`, as Jupyter Notebook will output the result of the last line, which with Panda becomes a HTML table:

# In[ ]:

print(
pd.read_sql_query("""
SELECT title
FROM articles
""", db))


# ## SQL results in Python
# 
# Above, Pandas' DataFrame is rendered in Juyter Notebook, skipping most of the 1001 rows. Alternatively we can inspect the table returned in Python. This is beneficial in case you need to do further processing in code.
# 
# **Note**: You do _not_ have to use Panda dataframes for accessing SQL databases from Python, see also the [SQLite Python tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial) for accessing the database directly.
# 
# Below, the method `.head()` is used to only select the first couple lines of the dataframe, while `.itertuples()` iterates over each row in the SQL result.  See the [Getting started with pandas](https://wesmckinney.com/book/pandas-basics) for further guidance on dataframes.
# 
# **Warning**: While SQL is generally case-insensitive, the database's spelling of the column name will be returned, which in this case is `Title` (instead of `title` as in the query) -- this matters below as Python code is case-sensitive.
# 

# In[ ]:


articles = pd.read_sql_query("""
SELECT Title
FROM articles
""", db)
for article in articles.head().itertuples():
  print(article.Title)


# 
# **Tip**: You can modify the code of Jupyter notebook, and click each cell's ▶️ button to run them. Use the [+ Code] button in Colab to add further code blocks. Use one code block per output.
# 
# 
# 

# ## Errors
# 
# Before we continue, let's look quickly at different errors in the SQL, which will cause a Python exception.

# ### Syntax error
# 
# The Python code is valid, but the SQL inside has a typo (`SELET` instead of `SELECT`):

# In[ ]:

print(
pd.read_sql_query("""
SELET title
FROM articles
""", db)
)

# ### Semantic error
# 
# Here the query is correct syntactically, but it's referencing a column that does not exist:

# In[ ]:





# In[ ]:
pd.read_sql_query("""
SELECT wrongColumn
FROM articles
""", db)


# * First, try to correct the errors above, then re-execute the cells.
# 
# Next, follow the [rest of section 2](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#capitalization-and-good-style) onwards to the remaining SQL selection exercises.
# 
# 
# ## Capitalization and good style
# 
# _Follow exercise on [good style](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#capitalization-and-good-style) below:_

# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# 

# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# ## Unique values
# 
# _Follow exercise on [unique values](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#unique-values)_

# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# ## Sorting
# 
# _Follow exercise on [sorting](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#sorting)_
# 

# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# # Filtering
# 
# _Follow exercies on [filtering](https://librarycarpentry.github.io/lc-sql/03-filtering.html)_

# In[ ]:


pd.read_sql_query("""
SELECT *
FROM articles
WHERE ISSNs = '2056-9890'
""", db).head()


# Note that in SQL, value comparisons is done with a _single_ equal sign  `=`, unlike Python and other programing languagues typical use of `==` or `.equals`

# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# # Ordering and commenting
# 
# _Follow exercises on [Ordering and commenting](https://librarycarpentry.github.io/lc-sql/04-ordering-commenting.html)_
# 
# 
# 
# 

# In[ ]:


pd.read_sql_query("""
SELECT Title, Authors
FROM articles
WHERE ISSNs = '2067-2764|2247-6202'
ORDER BY First_Author ASC;
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# # Aggregating values
# 
# _Follow exercise on [Aggregating and calculating values](https://librarycarpentry.github.io/lc-sql/05-aggregating-calculating.html)_
# 
# 
# 

# In[ ]:


pd.read_sql_query("""
SELECT ISSNs, AVG(Citation_Count)
FROM articles
GROUP BY ISSNs;
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db)


# # Joins and aliases
# 
# _Follow exercises on [Joins and aliases](https://librarycarpentry.github.io/lc-sql/06-joins-aliases.html)_
# 
# 

# In[ ]:


pd.read_sql_query("""
SELECT *
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs;
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# ## Aliases
# 
# _Follow exercises on [aliases](https://librarycarpentry.github.io/lc-sql/06-joins-aliases.html#aliases)_

# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# # Saving queries
# 
# _Follow exercise of [Saving queries](https://librarycarpentry.github.io/lc-sql/07-saving-queries.html)_
# 
# **Note**: As `DROP VIEW` and `CREATE VIEW` do not return any result, below we have to use `db.execute` directly rather than `pd.read_sql_query`.

# In[ ]:


db.execute("DROP VIEW IF EXISTS journal_counts")

db.execute("""
CREATE VIEW ...

""")


# In[ ]:


pd.read_sql_query("""
SELECT ...
""", db).head()


# Remember that a view is not stored as a separate table, but is a pre-canned query that can then itself be queries. That means updates to the tables will modify the views! SQL Views typically cannot themselves be modified with `INSERT`.
# 
# Nevertheless, if a view was temporary, we may want to delete it so it does clutter our database:

# In[ ]:


db.execute("DROP VIEW journal_counts")


# # Additional reading
# 
# The remaining sections of Library Carpentry SQL relates to creating databases before they can be queried.
# 
# 
# * [Database design](https://librarycarpentry.github.io/lc-sql/08-database-design.html)
# * [Creating tables](https://librarycarpentry.github.io/lc-sql/09-create.html)
# * [Extra challenges](https://librarycarpentry.github.io/lc-sql/11-extra-challenges.html)
# * [Good SQL style](https://librarycarpentry.github.io/lc-sql/Bonus_GoodStyle.html)
# 
# **Tip**: Sometimes knowing what kind of queries are needed will influence the design at earlier data engineering phases, e.g. reducing the need for complex `JOIN`s.
