# Bronze Layer - Ingest raw CSV to Delta

raw_path = "/mnt/raw/orders_sample.csv"
bronze_path = "/mnt/bronze/orders"

df_raw = (spark.read
          .format("csv")
          .option("header", "true")
          .load(raw_path))

df_raw.write.format("delta").mode("overwrite").save(bronze_path)

print("Bronze table created:", bronze_path)
