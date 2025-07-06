+++
title = "Data Acquisition and Reduction"
type = "chapter"
weight = 1

[params]
  menuPre = '<i class="fa-solid fa-download"></i> '
+++

In our first quest of data engineering, we will consider the task of acquiring data into our local environment before it can be further processed. 

```mermaid {align="center" zoom="true"}
graph LR;
  classDef highlight stroke:#000,stroke-width:4px
  direction LR
  Generation:::highlight
  subgraph S [ ]
    Ingestion:::highlight
    Transformation
    Serving
    Ingestion --> Transformation
    Transformation --> Serving
    Storage@{ shape: lin-cyl }
  end
  Generation --> Ingestion
  Serving --> Analytics
  Serving --> ML(Machine Learning)
  Serving --> RETL(Reverse ETL)
```


```mermaid {align="center" zoom="true"}
graph LR;
  classDef UC fill:#fff,stroke:#555
  classDef highlight stroke:#000,stroke-width:4px,fill:#fff,stroke:#555
  subgraph Undercurrents
    direction TB
    Security:::UC
    DM(Data management):::highlight
    DataOps:::UC
    DA(Data Architecture):::UC
    Orchestration:::UC
    SE(Software Engineering):::UC
    style Undercurrents fill:#eee,stroke:#000
  end
```

https://www.data.gov.uk/dataset/81cbf1a0-6304-470c-ade8-60272be0d219/sites-of-biological-importance-sbi-in-greater-manchester

