+++
title = "Data Analytics & Machine Learning"
type = "chapter"
weight = 8

[params]
  menuPre = '<i class="fa-solid fa-magnifying-glass-chart"></i> '
+++


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
  Serving --> Analytics:::highlight
  Serving --> ML(Machine Learning):::highlight
  Serving --> RETL(Reverse ETL)
```

