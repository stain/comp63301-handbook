+++
title = "Introduction"
weight = -1
+++

This handbook closely follows the Data Engineering Lifecycle from the text book [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/):

<figure>

```mermaid {align="center" zoom="true"}
graph LR;
  classDef highlight stroke:#000,stroke-width:4px
  direction LR
  Generation
  subgraph S [ ]
    Ingestion
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
  classDef highlight stroke:#000,stroke-width:4px
  subgraph Undercurrents
    direction TB
    Security:::UC
    DM(Data management):::UC
    DataOps:::UC
    DA(Data Architecture):::UC
    Orchestration:::UC
    SE(Software Engineering):::UC
    style Undercurrents fill:#eee,stroke:#000
  end
```
  
  <figcaption>
  
  **Figure 1**: Data Engineering Lifecycle, adapted from Figure 1.1 in [Reis & Housley 2022].
  
  </figcaption>
</figure> 

