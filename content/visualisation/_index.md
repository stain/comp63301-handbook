+++
title = "Data Visualisation and Serving"
type = "chapter"
weight = 9

[params]
  menuPre = '<i class="fa-solid fa-chart-simple"></i> '
+++



```mermaid {align="center" zoom="true"}
graph LR;
  classDef highlight stroke:#000,stroke-width:4px
  direction LR
  Generation
  subgraph S [ ]
    Ingestion
    Transformation
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
