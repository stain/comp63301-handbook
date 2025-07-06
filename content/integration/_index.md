+++
title = "Data Integration"
type = "chapter"
weight = 4

[params]
  menuPre = '<i class="fa-solid fa-code-fork"></i> '
+++


```mermaid {align="center" zoom="true"}
graph LR;
  classDef highlight stroke:#000,stroke-width:4px
  direction LR
  Generation
  subgraph S [ ]
    Ingestion:::highlight
    Transformation:::highlight
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