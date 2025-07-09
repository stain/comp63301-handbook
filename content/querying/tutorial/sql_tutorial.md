

This tutorial is based on the [Library Carpentry SQL tutorial](https://librarycarpentry.github.io/lc-sql/), licensed under [CC-BY 4.0](https://librarycarpentry.github.io/lc-sql/LICENSE.html).

You can run this Jupyter notebook in [Google Colab](https://colab.research.google.com/) or on your local installation.

**Note**: In Colab, if the notebook is View Only, remember to make a copy, so that you can modify it:

* _File --> Save a copy in Drive_.


### Attribution

Jordan Perdersen (Ed.), Kristin Lee (Ed.), Christopher Erdmann (Ed.), Lise Doucette (Ed.), Elaine Wong (Ed.), Janice Chan (Ed.), James Baker, Fernando Rios, Tim Dennis, Belinda Weaver, … orobecca. (2019, July). **LibraryCarpentry/lc-sql: Library Carpentry: Introduction to SQL, June 2019** (Version v2019.06.1). _Zenodo_. http://doi.org/10.5281/zenodo.3266102

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3266102.svg)](https://doi.org/10.5281/zenodo.3266102)

#### Modifications

Extracts modified to Jupyter notebook use by Stian Soiland-Reyes <https://orcid.org/0000-0001-9842-9718>.

#### References

* <https://pythonspot.com/sqlite-database-with-pandas/>
* <https://pythoncourses.gumroad.com/l/KmxqY>
* <https://www.sqlitetutorial.net/>
* <https://wesmckinney.com/book/pandas-basics>


## Data ingestion

In this tutorial we assume data has already been ingested and cleaned. We'll retrieve the already prepared SQLite database.

[SQLite](https://sqlite.org/) is a miniature relational database that can be used without a server installation, for instance by directly importing the SQLite library in Python and "connecting" it to a local file. It is worth noting that this means only a single process can access the file at a time (in this case our Jupyter notebook).

### Download SQLite database

The Zenodo deposit <https://doi.org/10.5281/zenodo.8360812> contains a ZIP file with the pre-populated database in SQLite format. As this tutorial is not showing "proper" data ingestion, we'll just download and unzip using Linux shell commands:


```shell
wget https://zenodo.org/records/8360812/files/doaj-article-sample-db.zip && unzip doaj-article-sample-db.zip
```

    --2025-07-08 15:12:03--  https://zenodo.org/records/8360812/files/doaj-article-sample-db.zip
    Resolving zenodo.org (zenodo.org)... 188.185.45.92, 188.185.48.194, 188.185.43.25, ...
    Connecting to zenodo.org (zenodo.org)|188.185.45.92|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 947007 (925K) [application/octet-stream]
    Saving to: ‘doaj-article-sample-db.zip’
    
    doaj-article-sample 100%[===================>] 924.81K   499KB/s    in 1.9s    
    
    2025-07-08 15:12:06 (499 KB/s) - ‘doaj-article-sample-db.zip’ saved [947007/947007]
    
    Archive:  doaj-article-sample-db.zip
      inflating: doaj-article-sample.db  
      inflating: doaj-article-sample.db.sql  


Now let's connect to this database from within Python using the [sqlite3](https://docs.python.org/3/library/sqlite3.html) library, and see which tables are included. In SQLite this can be done by inspecting the `sqlite_master` table, using the `SELECT *` query . We'll use [pandas](https://pandas.pydata.org/) as a helper to better view the SQL results in Jupyter Notebook.




```python
import sqlite3
import pandas as pd

db = sqlite3.connect("doaj-article-sample.db")
pd.read_sql_query("SELECT * FROM sqlite_master", db)
```





  <div id="df-3791cbcf-e3e6-4f4e-bc29-d05b5fa4542f" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>tbl_name</th>
      <th>rootpage</th>
      <th>sql</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>table</td>
      <td>sqlite_sequence</td>
      <td>sqlite_sequence</td>
      <td>275</td>
      <td>CREATE TABLE sqlite_sequence(name,seq)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>table</td>
      <td>languages</td>
      <td>languages</td>
      <td>408</td>
      <td>CREATE TABLE "languages" (\n  "id" INTEGER NOT...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>table</td>
      <td>publishers</td>
      <td>publishers</td>
      <td>679</td>
      <td>CREATE TABLE "publishers" (\n  "id" INTEGER NO...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>table</td>
      <td>licences</td>
      <td>licences</td>
      <td>2</td>
      <td>CREATE TABLE "licences" (\n  "id" INTEGER NOT ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>table</td>
      <td>journals</td>
      <td>journals</td>
      <td>3</td>
      <td>CREATE TABLE "journals" (\n  "id" INTEGER NOT ...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>table</td>
      <td>articles</td>
      <td>articles</td>
      <td>5</td>
      <td>CREATE TABLE "articles" (\n  "id" INTEGER NOT ...</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-3791cbcf-e3e6-4f4e-bc29-d05b5fa4542f')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-3791cbcf-e3e6-4f4e-bc29-d05b5fa4542f button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-3791cbcf-e3e6-4f4e-bc29-d05b5fa4542f');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-a4a083db-5743-4731-b418-6b0dd6a2a4be">
      <button class="colab-df-quickchart" onclick="quickchart('df-a4a083db-5743-4731-b418-6b0dd6a2a4be')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-a4a083db-5743-4731-b418-6b0dd6a2a4be button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>




## Introduction to SQL

In this tutorial we'll follow the Library Carpentry guide, but run the queries from within Python instead of the DB Browser.  

* Read through [Section 1: Introduction to SQL](https://librarycarpentry.github.io/lc-sql/01-introduction.html)  (ignoring the _DB Browser_ subsection).



## Selecting and querying data

Next, follow the [Section 2: Selecting and sorting data](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html). Use Python's `"""` strings to support multiple lines.

Note that you don't need to use `print()`, as Jupyter Notebook will output the result of the last line, which with Panda becomes a HTML table:


```python
pd.read_sql_query("""
SELECT title
FROM articles
""", db)
```





  <div id="df-c63fceed-a32b-4946-baa7-bdc458dc1884" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Fisher Thermodynamics of Quasi-Probabilities</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aflatoxin Contamination of the Milk Supply: A ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Metagenomic Analysis of Upwelling-Affected Bra...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Synthesis and Reactivity of a Cerium(III) Scor...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Performance and Uncertainty Evaluation of Snow...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>996</th>
      <td>Crystal structure of [3-(1H-benzimidazol-2-yl)...</td>
    </tr>
    <tr>
      <th>997</th>
      <td>Crystal structure of bis(3-bromopyridine-κN)bi...</td>
    </tr>
    <tr>
      <th>998</th>
      <td>Crystal structure of 4,4′-(ethane-1,2-diyl)bis...</td>
    </tr>
    <tr>
      <th>999</th>
      <td>Crystal structure of (Z)-4-[1-(4-acetylanilino...</td>
    </tr>
    <tr>
      <th>1000</th>
      <td>Metagenomic Analysis of Upwelling-Affected Bra...</td>
    </tr>
  </tbody>
</table>
<p>1001 rows × 1 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-c63fceed-a32b-4946-baa7-bdc458dc1884')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-c63fceed-a32b-4946-baa7-bdc458dc1884 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-c63fceed-a32b-4946-baa7-bdc458dc1884');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-a72c178e-4ee3-4af8-998c-6c7751398193">
      <button class="colab-df-quickchart" onclick="quickchart('df-a72c178e-4ee3-4af8-998c-6c7751398193')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-a72c178e-4ee3-4af8-998c-6c7751398193 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>




### SQL results in Python

Above, Pandas' DataFrame is rendered in Juyter Notebook, skipping most of the 1001 rows. Alternatively we can inspect the table returned in Python. This is beneficial in case you need to do further processing in code.

**Note**: You do _not_ have to use Panda dataframes for accessing SQL databases from Python, see also the [SQLite Python tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial) for accessing the database directly.

Below, the method `.head()` is used to only select the first couple lines of the dataframe, while `.itertuples()` iterates over each row in the SQL result.  See the [Getting started with pandas](https://wesmckinney.com/book/pandas-basics) for further guidance on dataframes.

**Warning**: While SQL is generally case-insensitive, the database's spelling of the column name will be returned, which in this case is `Title` (instead of `title` as in the query) -- this matters below as Python code is case-sensitive.



```python
articles = pd.read_sql_query("""
SELECT Title
FROM articles
""", db)
for article in articles.head().itertuples():
  print(article.Title)

```

    The Fisher Thermodynamics of Quasi-Probabilities
    Aflatoxin Contamination of the Milk Supply: A Pakistan Perspective
    Metagenomic Analysis of Upwelling-Affected Brazilian Coastal Seawater Reveals Sequence Domains of Type I PKS and Modular NRPS
    Synthesis and Reactivity of a Cerium(III) Scorpionate Complex Containing a Redox Non-Innocent 2,2′-Bipyridine Ligand
    Performance and Uncertainty Evaluation of Snow Models on Snowmelt Flow Simulations over a Nordic Catchment (Mistassibi, Canada)



**Tip**: You can modify the code of Jupyter notebook, and click each cell's ▶️ button to run them. Use the [+ Code] button in Colab to add further code blocks. Use one code block per output.




### Errors

Before we continue, let's look quickly at different errors in the SQL, which will cause a Python exception.

#### Syntax error

The Python code is valid, but the SQL inside has a typo (`SELET` instead of `SELECT`):


```python
pd.read_sql_query("""
SELET title
FROM articles
""", db)
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in execute(self, sql, params)
       2673         try:
    -> 2674             cur.execute(sql, *args)
       2675             return cur


    OperationalError: near "SELET": syntax error

    
    The above exception was the direct cause of the following exception:


    DatabaseError                             Traceback (most recent call last)

    /tmp/ipython-input-22-3013307109.py in <cell line: 0>()
    ----> 1 pd.read_sql_query("""
          2 SELET title
          3 FROM articles
          4 """, db)


    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in read_sql_query(sql, con, index_col, coerce_float, params, parse_dates, chunksize, dtype, dtype_backend)
        524 
        525     with pandasSQL_builder(con) as pandas_sql:
    --> 526         return pandas_sql.read_query(
        527             sql,
        528             index_col=index_col,


    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize, dtype, dtype_backend)
       2736         dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",
       2737     ) -> DataFrame | Iterator[DataFrame]:
    -> 2738         cursor = self.execute(sql, params)
       2739         columns = [col_desc[0] for col_desc in cursor.description]
       2740 


    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in execute(self, sql, params)
       2684 
       2685             ex = DatabaseError(f"Execution failed on sql '{sql}': {exc}")
    -> 2686             raise ex from exc
       2687 
       2688     @staticmethod


    DatabaseError: Execution failed on sql '
    SELET title
    FROM articles
    ': near "SELET": syntax error


#### Semantic error

Here the query is correct syntactically, but it's referencing a column that does not exist:


```python

```


```python
pd.read_sql_query("""
SELECT wrongColumn
FROM articles
""", db)
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in execute(self, sql, params)
       2673         try:
    -> 2674             cur.execute(sql, *args)
       2675             return cur


    OperationalError: no such column: wrongColumn

    
    The above exception was the direct cause of the following exception:


    DatabaseError                             Traceback (most recent call last)

    /tmp/ipython-input-23-818033597.py in <cell line: 0>()
    ----> 1 pd.read_sql_query("""
          2 SELECT wrongColumn
          3 FROM articles
          4 """, db)


    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in read_sql_query(sql, con, index_col, coerce_float, params, parse_dates, chunksize, dtype, dtype_backend)
        524 
        525     with pandasSQL_builder(con) as pandas_sql:
    --> 526         return pandas_sql.read_query(
        527             sql,
        528             index_col=index_col,


    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize, dtype, dtype_backend)
       2736         dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",
       2737     ) -> DataFrame | Iterator[DataFrame]:
    -> 2738         cursor = self.execute(sql, params)
       2739         columns = [col_desc[0] for col_desc in cursor.description]
       2740 


    /usr/local/lib/python3.11/dist-packages/pandas/io/sql.py in execute(self, sql, params)
       2684 
       2685             ex = DatabaseError(f"Execution failed on sql '{sql}': {exc}")
    -> 2686             raise ex from exc
       2687 
       2688     @staticmethod


    DatabaseError: Execution failed on sql '
    SELECT wrongColumn
    FROM articles
    ': no such column: wrongColumn


* First, try to correct the errors above, then re-execute the cells.

Next, follow the [rest of section 2](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#capitalization-and-good-style) onwards to the remaining SQL selection exercises.


### Capitalization and good style

_Follow exercise on [good style](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#capitalization-and-good-style) below:_


```python
pd.read_sql_query("""
SELECT ...
""", db)
```




```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```

### Unique values

_Follow exercise on [unique values](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#unique-values)_


```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```

### Sorting

_Follow exercise on [sorting](https://librarycarpentry.github.io/lc-sql/02-selecting-sorting-data.html#sorting)_



```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```

## Filtering

_Follow exercies on [filtering](https://librarycarpentry.github.io/lc-sql/03-filtering.html)_


```python
pd.read_sql_query("""
SELECT *
FROM articles
WHERE ISSNs = '2056-9890'
""", db).head()
```





  <div id="df-a4ac4d90-026d-4ab4-8bd5-661f0267494f" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Title</th>
      <th>Authors</th>
      <th>DOI</th>
      <th>URL</th>
      <th>Subjects</th>
      <th>ISSNs</th>
      <th>Citation</th>
      <th>LanguageId</th>
      <th>LicenceId</th>
      <th>Author_Count</th>
      <th>First_Author</th>
      <th>Citation_Count</th>
      <th>Day</th>
      <th>Month</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>142</td>
      <td>Crystal structure of 7-isopropyl-1,4a,N-trimet...</td>
      <td>Li Liu|Xin-Yan Yan|Xiao-Ping Rao</td>
      <td>10.1107/S2056989015017648</td>
      <td>https://doaj.org/article/69bfe1351c864bc8a6b38...</td>
      <td>crystal structure|dihydroabietic acid derivati...</td>
      <td>2056-9890</td>
      <td>Acta Crystallographica Section E: Crystallogra...</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>Li Liu</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>143</td>
      <td>Crystal structure of 2-(2,4-diphenyl-3-azabicy...</td>
      <td>K. Priya|K. Saravanan|S. Kabilan|S. Selvanayagam</td>
      <td>10.1107/S2056989015017740</td>
      <td>https://doaj.org/article/ce085e7ac3bd43e49a122...</td>
      <td>crystal structure|3-azabicyclononane derivativ...</td>
      <td>2056-9890</td>
      <td>Acta Crystallographica Section E: Crystallogra...</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>K. Priya</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>144</td>
      <td>Crystal structure of 2-[2-(hydroxyimino)-1-phe...</td>
      <td>Brian J. Anderson|Michael B. Freedman|Sean P. ...</td>
      <td>10.1107/S2056989015017739</td>
      <td>https://doaj.org/article/4dd1a69aaefa478b8d2bb...</td>
      <td>crystal structure|thiosemicarbazone|weak inter...</td>
      <td>2056-9890</td>
      <td>Acta Crystallographica Section E: Crystallogra...</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>Brian J. Anderson</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>145</td>
      <td>Crystal structure of 1-methoxy-5-methyl-N-phen...</td>
      <td>Inna S. Khazhieva|Tatiana V. Glukhareva|Pavel ...</td>
      <td>10.1107/S2056989015017776</td>
      <td>https://doaj.org/article/8c3bd9d71ba642f5b28d0...</td>
      <td>crystal structure|1,2,3-triazole|rearrangement...</td>
      <td>2056-9890</td>
      <td>Acta Crystallographica Section E: Crystallogra...</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>Inna S. Khazhieva</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>146</td>
      <td>Redetermined structure of 4,4′-bipyridine–1,4-...</td>
      <td>Rima Paul|Sanchay Jyoti Bora</td>
      <td>10.1107/S2056989015017569</td>
      <td>https://doaj.org/article/b2d1ca2bb6fb4ba48c11e...</td>
      <td>crystal structure|co-crystal|supramolecular in...</td>
      <td>2056-9890</td>
      <td>Acta Crystallographica Section E: Crystallogra...</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>Rima Paul</td>
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-a4ac4d90-026d-4ab4-8bd5-661f0267494f')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-a4ac4d90-026d-4ab4-8bd5-661f0267494f button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-a4ac4d90-026d-4ab4-8bd5-661f0267494f');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-5dd89063-7d5e-4264-ba63-1e15eb246e39">
      <button class="colab-df-quickchart" onclick="quickchart('df-5dd89063-7d5e-4264-ba63-1e15eb246e39')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-5dd89063-7d5e-4264-ba63-1e15eb246e39 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>




Note that in SQL, value comparisons is done with a _single_ equal sign  `=`, unlike Python and other programing languagues typical use of `==` or `.equals`


```python
pd.read_sql_query("""
SELECT ...
""", db).head()
```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()
```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()
```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()
```

## Ordering and commenting

_Follow exercises on [Ordering and commenting](https://librarycarpentry.github.io/lc-sql/04-ordering-commenting.html)_






```python
pd.read_sql_query("""
SELECT Title, Authors
FROM articles
WHERE ISSNs = '2067-2764|2247-6202'
ORDER BY First_Author ASC;
""", db)
```





  <div id="df-989afc81-007e-48c0-b381-b9bb9e3da7b8" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Authors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Zweier I-Convergent Double Sequence Spaces Def...</td>
      <td>A. Khan Vakeel| Khan Nazneen|Yasmeen</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New Čebyšev Type Inequalities for Functions wh...</td>
      <td>B. Meftah|K. Boukerrioua</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Initial Maclaurin Coecients Bounds for New Sub...</td>
      <td>Basem Aref Frasin|Tariq Al-Hawary</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Measure of Tessellation Quality of Voronoï Meshes</td>
      <td>E. A-iyeh|J.F. Peters</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Applicability of $-Calculus to Solve Some ...</td>
      <td>Eugene Eberbach</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Some Families of q-Series Identities and Assoc...</td>
      <td>H. M. Srivastava|S. N. Singh|S. P. Singh</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Lp - Approximation of Analytic Functions on Co...</td>
      <td>Kumar Devendra|Jain Vandna</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A Mixed Integer Linear Programming Formulation...</td>
      <td>Marija Ivanović</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Properties of Stabilizing Computations</td>
      <td>Mark Burgin</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Primality Testing and Factorization by using F...</td>
      <td>Musha Takaaki</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Luhn Prime Numbers</td>
      <td>Octavian Cira|Florentin Smarandache</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hadamard Product of Certain Harmonic Univalent...</td>
      <td>R. M. El-Ashwah|B. A. Frasin</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Second Hankel Determinant for Generalized Saka...</td>
      <td>S. P. Vijayalakshmi|T. V. Sudharsan</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Some Perturbed Ostrowski Type Inequalities for...</td>
      <td>S. S. Dragomir</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Katsaras’s Type Fuzzy Norm under Triangular Norms</td>
      <td>Sorin Nădăban|Tudor Bînzar|Flavius Pater|Carme...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>On BVσ I-convergent Sequence Spaces Defined by...</td>
      <td>Vakeel A. Khan|Mohd Shafiq|Rami Kamel Ahmad Ra...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Coupled Systems of Fractional Integro-Differen...</td>
      <td>Zoubir Dahmani|Mohamed Amin Abdellaoui|Mohamed...</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-989afc81-007e-48c0-b381-b9bb9e3da7b8')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-989afc81-007e-48c0-b381-b9bb9e3da7b8 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-989afc81-007e-48c0-b381-b9bb9e3da7b8');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-53ff91c1-3022-4570-9def-5a3d29d94804">
      <button class="colab-df-quickchart" onclick="quickchart('df-53ff91c1-3022-4570-9def-5a3d29d94804')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-53ff91c1-3022-4570-9def-5a3d29d94804 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>





```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```

## Aggregating values

_Follow exercise on [Aggregating and calculating values](https://librarycarpentry.github.io/lc-sql/05-aggregating-calculating.html)_





```python
pd.read_sql_query("""
SELECT ISSNs, AVG(Citation_Count)
FROM articles
GROUP BY ISSNs;
""", db)
```





  <div id="df-936e5f0e-83dc-4350-95ac-676a9f90e53e" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ISSNs</th>
      <th>AVG(Citation_Count)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0367-0449|1988-3250</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1099-4300</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1420-3049</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1422-0067</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1424-8220</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1660-3397</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1660-4601</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1996-1944</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1999-4907</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1999-4915</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2056-9890</td>
      <td>9.593240</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2067-2764|2247-6202</td>
      <td>8.647059</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2071-1050</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2072-4292</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2072-6643</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2072-6651</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2072-6694</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2073-4344</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2073-4360</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2073-4395</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2073-4425</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2073-4441</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2073-8994</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2075-163X</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2075-1702</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2075-4418</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2075-4442</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2075-4701</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2075-5309</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2076-0787</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2076-2615</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2076-3417</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2076-3905</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2076-393X</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2077-0375</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2077-0472</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2077-1444</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2078-1547</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2079-6374</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2079-7737</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>40</th>
      <td>2079-8954</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>41</th>
      <td>2079-9268</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>42</th>
      <td>2220-9964</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>43</th>
      <td>2227-9717</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2250-1177</td>
      <td>7.000000</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2278-4748|2278-4802</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>46</th>
      <td>2304-6740</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>47</th>
      <td>2304-6767</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2305-6304</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2306-5338</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2306-5354</td>
      <td>5.000000</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-936e5f0e-83dc-4350-95ac-676a9f90e53e')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-936e5f0e-83dc-4350-95ac-676a9f90e53e button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-936e5f0e-83dc-4350-95ac-676a9f90e53e');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-3aaa5445-8856-4b3f-b181-fb9e1d00d079">
      <button class="colab-df-quickchart" onclick="quickchart('df-3aaa5445-8856-4b3f-b181-fb9e1d00d079')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-3aaa5445-8856-4b3f-b181-fb9e1d00d079 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>





```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```


```python
pd.read_sql_query("""
SELECT ...
""", db)
```

## Joins and aliases

_Follow exercises on [Joins and aliases](https://librarycarpentry.github.io/lc-sql/06-joins-aliases.html)_




```python
pd.read_sql_query("""
SELECT *
FROM articles
JOIN journals
ON articles.ISSNs = journals.ISSNs;
""", db).head()

```





  <div id="df-60735bb6-1a6d-439b-b62f-666ee79f515f" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Title</th>
      <th>Authors</th>
      <th>DOI</th>
      <th>URL</th>
      <th>Subjects</th>
      <th>ISSNs</th>
      <th>Citation</th>
      <th>LanguageId</th>
      <th>LicenceId</th>
      <th>...</th>
      <th>First_Author</th>
      <th>Citation_Count</th>
      <th>Day</th>
      <th>Month</th>
      <th>Year</th>
      <th>id</th>
      <th>ISSN-L</th>
      <th>ISSNs</th>
      <th>PublisherId</th>
      <th>Journal_Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>The Fisher Thermodynamics of Quasi-Probabilities</td>
      <td>Flavia Pennini|Angelo Plastino</td>
      <td>10.3390/e17127853</td>
      <td>https://doaj.org/article/b75e8d5cca3f46cbbd63e...</td>
      <td>Fisher information|quasi-probabilities|complem...</td>
      <td>1099-4300</td>
      <td>Entropy, Vol 17, Iss 12, Pp 7848-7858 (2015)</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Flavia Pennini</td>
      <td>4</td>
      <td>1</td>
      <td>11</td>
      <td>2015</td>
      <td>14</td>
      <td>1099-4300</td>
      <td>1099-4300</td>
      <td>2</td>
      <td>Entropy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Aflatoxin Contamination of the Milk Supply: A ...</td>
      <td>Naveed Aslam|Peter C. Wynn</td>
      <td>10.3390/agriculture5041172</td>
      <td>https://doaj.org/article/0edc5af6672641c0bd456...</td>
      <td>aflatoxins|AFM1|AFB1|milk marketing chains|hep...</td>
      <td>2077-0472</td>
      <td>Agriculture (Basel), Vol 5, Iss 4, Pp 1172-118...</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Naveed Aslam</td>
      <td>5</td>
      <td>1</td>
      <td>11</td>
      <td>2015</td>
      <td>1</td>
      <td>2077-0472</td>
      <td>2077-0472</td>
      <td>2</td>
      <td>Agriculture</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Metagenomic Analysis of Upwelling-Affected Bra...</td>
      <td>Rafael R. C. Cuadrat|Juliano C. Cury|Alberto M...</td>
      <td>10.3390/ijms161226101</td>
      <td>https://doaj.org/article/d9fe469f75a0442382b84...</td>
      <td>PKS|NRPS|metagenomics|environmental genomics|u...</td>
      <td>1422-0067</td>
      <td>International Journal of Molecular Sciences, V...</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Rafael R. C. Cuadrat</td>
      <td>8</td>
      <td>1</td>
      <td>11</td>
      <td>2015</td>
      <td>22</td>
      <td>1422-0067</td>
      <td>1422-0067</td>
      <td>2</td>
      <td>International Journal of Molecular Sciences</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Synthesis and Reactivity of a Cerium(III) Scor...</td>
      <td>Fabrizio Ortu|Hao Zhu|Marie-Emmanuelle Boulon|...</td>
      <td>10.3390/inorganics3040534</td>
      <td>https://doaj.org/article/95606ed39deb4f43b96f7...</td>
      <td>lanthanide|cerium|scorpionate|tris(pyrazolyl)b...</td>
      <td>2304-6740</td>
      <td>Inorganics (Basel), Vol 3, Iss 4, Pp 534-553 (...</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Fabrizio Ortu</td>
      <td>5</td>
      <td>1</td>
      <td>11</td>
      <td>2015</td>
      <td>20</td>
      <td>2304-6740</td>
      <td>2304-6740</td>
      <td>2</td>
      <td>Inorganics</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Performance and Uncertainty Evaluation of Snow...</td>
      <td>Magali Troin|Richard Arsenault|François Brissette</td>
      <td>10.3390/hydrology2040289</td>
      <td>https://doaj.org/article/18b1d70730d44573ab5c2...</td>
      <td>snow models|hydrological models|snowmelt|uncer...</td>
      <td>2306-5338</td>
      <td>Hydrology, Vol 2, Iss 4, Pp 289-317 (2015)</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>Magali Troin</td>
      <td>4</td>
      <td>1</td>
      <td>11</td>
      <td>2015</td>
      <td>19</td>
      <td>2306-5338</td>
      <td>2306-5338</td>
      <td>2</td>
      <td>Hydrology</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-60735bb6-1a6d-439b-b62f-666ee79f515f')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-60735bb6-1a6d-439b-b62f-666ee79f515f button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-60735bb6-1a6d-439b-b62f-666ee79f515f');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    <div id="df-cab7ed2c-399b-43bf-acf2-a950c6da1c08">
      <button class="colab-df-quickchart" onclick="quickchart('df-cab7ed2c-399b-43bf-acf2-a950c6da1c08')"
                title="Suggest charts"
                style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
      </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

      <script>
        async function quickchart(key) {
          const quickchartButtonEl =
            document.querySelector('#' + key + ' button');
          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
          quickchartButtonEl.classList.add('colab-df-spinner');
          try {
            const charts = await google.colab.kernel.invokeFunction(
                'suggestCharts', [key], {});
          } catch (error) {
            console.error('Error during call to suggestCharts:', error);
          }
          quickchartButtonEl.classList.remove('colab-df-spinner');
          quickchartButtonEl.classList.add('colab-df-quickchart-complete');
        }
        (() => {
          let quickchartButtonEl =
            document.querySelector('#df-cab7ed2c-399b-43bf-acf2-a950c6da1c08 button');
          quickchartButtonEl.style.display =
            google.colab.kernel.accessAllowed ? 'block' : 'none';
        })();
      </script>
    </div>

    </div>
  </div>





```python
pd.read_sql_query("""
SELECT ...
""", db).head()

```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()

```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()

```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()

```

### Aliases

_Follow exercises on [aliases](https://librarycarpentry.github.io/lc-sql/06-joins-aliases.html#aliases)_


```python
pd.read_sql_query("""
SELECT ...
""", db).head()

```

## Saving queries

_Follow exercise of [Saving queries](https://librarycarpentry.github.io/lc-sql/07-saving-queries.html)_

**Note**: As `DROP VIEW` and `CREATE VIEW` do not return any result, below we have to use `db.execute` directly rather than `pd.read_sql_query`.


```python
db.execute("DROP VIEW IF EXISTS journal_counts")

db.execute("""
CREATE VIEW ...

""")
```


```python
pd.read_sql_query("""
SELECT ...
""", db).head()
```

Remember that a view is not stored as a separate table, but is a pre-canned query that can then itself be queries. That means updates to the tables will modify the views! SQL Views typically cannot themselves be modified with `INSERT`.

Nevertheless, if a view was temporary, we may want to delete it so it does clutter our database:


```python
db.execute("DROP VIEW journal_counts")
```

## Additional reading

The remaining sections of Library Carpentry SQL relates to creating databases before they can be queried.


* [Database design](https://librarycarpentry.github.io/lc-sql/08-database-design.html)
* [Creating tables](https://librarycarpentry.github.io/lc-sql/09-create.html)
* [Extra challenges](https://librarycarpentry.github.io/lc-sql/11-extra-challenges.html)
* [Good SQL style](https://librarycarpentry.github.io/lc-sql/Bonus_GoodStyle.html)

**Tip**: Sometimes knowing what kind of queries are needed will influence the design at earlier data engineering phases, e.g. reducing the need for complex `JOIN`s.
