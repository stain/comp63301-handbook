+++
title = "Data Modelling and Storage"
type = "chapter"
weight = 3

[params]
  menuPre = '<i class="fa-solid fa-database"></i> '
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
    Storage:::highlight
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
    DM(Data management):::UC
    DataOps:::UC
    DA(Data Architecture):::highlight
    Orchestration:::UC
    SE(Software Engineering):::UC
    style Undercurrents fill:#eee,stroke:#000
  end
```


{{% children sort="weight" %}}

