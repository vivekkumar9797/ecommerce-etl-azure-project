# ecommerce-etl-azure-project
End-to-end Azure Data Engineering project using ADF, ADLS, Databricks, Delta Lake
📦 E-Commerce ETL Pipeline — Azure Data Engineering Project

Tools: Azure Data Factory • ADLS Gen2 • Databricks • Delta Lake • Power BI
Architecture: Batch Ingestion → Bronze → Silver → Gold → Analytics

🧩 Project Overview

This project demonstrates a real-world batch ETL pipeline for an e-commerce company.
Daily order files are ingested using Azure Data Factory, stored in ADLS, processed using PySpark on Azure Databricks, and modeled into Bronze/Silver/Gold Delta Lake layers.
Power BI is used to visualize daily sales and customer insights.

🏗 Architecture Diagram

(Add your image later in the /architecture folder)

E-Commerce Files → ADF → ADLS Raw → Databricks Bronze/Silver/Gold
                                      ↓
                                  Power BI

⚙️ Technologies Used

Azure Data Factory (ADF)

Azure Data Lake Storage Gen2 (ADLS)

Azure Databricks (PySpark)

Delta Lake (Bronze/Silver/Gold)

Azure Synapse (optional)

Power BI

📁 Folder Structure
/
├── adf_pipelines/          # Contains ADF pipeline JSON exports
├── architecture/           # Architecture diagram(s)
├── databricks_notebooks/   # PySpark notebooks for ETL
├── powerbi/                # Power BI report files
├── sample_data/            # Sample raw data used for testing
├── screenshots/            # Architecture & pipeline screenshots
└── README.md               # Project documentation

🧪 Data Flow (Step-by-Step)
1️⃣ Ingestion (ADF → Raw Layer)

ADF pipeline copies daily CSV/JSON files from source to ADLS Gen2 raw/

Dynamic file path naming

Daily trigger enabled

2️⃣ Bronze Layer (Databricks)
df = spark.read.format("csv").option("header", "true").load("/mnt/raw/")
df.write.format("delta").mode("overwrite").save("/mnt/bronze/orders")

3️⃣ Silver Layer (Transformations)
df = spark.read.format("delta").load("/mnt/bronze/orders")
df_clean = df.withColumn("amount", df.amount.cast("double"))
df_clean.write.format("delta").mode("overwrite").save("/mnt/silver/orders")

4️⃣ Gold Layer (Aggregations)
from pyspark.sql.functions import *
df = spark.read.format("delta").load("/mnt/silver/orders")
daily = df.groupBy(to_date("timestamp")).agg(sum("amount").alias("total_sales"))
daily.write.format("delta").mode("overwrite").save("/mnt/gold/daily_sales")

📊 Power BI Analytics

Daily Sales Trend

Top Cities by Revenue

Payment Method Distribution

Power BI file is stored in /powerbi/.

🧠 Key Learnings

End-to-end Azure data pipeline design

Delta Lake optimization

Bronze–Silver–Gold modeling

Connecting Azure to Power BI for analytics

Scalable, production-style ETL development

🔗 Future Enhancements

Add CDC (Change Data Capture)

Add streaming ingestion via Event Hub

Add Databricks Job Scheduling

Implement CI/CD with Azure DevOps

✨ Created by: Vivek kumar upadhyay D
