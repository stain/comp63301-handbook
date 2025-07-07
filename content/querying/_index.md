+++
title = "Data Querying"
type = "chapter"
weight = 7

[params]
  menuPre = '<i class="fa-solid fa-magnifying-glass"></i> '
+++


```mermaid {align="center" zoom="true"}
graph LR;
  classDef highlight stroke:#000,stroke-width:4px
  direction LR
  Generation
  subgraph S [ ]
    Ingestion
    Transformation:::highlight
    Serving:::highlight
    Ingestion --> Transformation
    Transformation --> Serving
    Storage@{ shape: lin-cyl }
  end
  Generation --> Ingestion
  Serving --> Analytics:::highlight
  Serving --> ML(Machine Learning)
  Serving --> RETL(Reverse ETL)
```

In this chapter we'll consider ways to query our consolidated data. A **query** is a way to ask questions to the data, to select a subset based on some filter, for instance particular attribute criteria must be met. 


## Sections

{{% children sort="weight" %}}

