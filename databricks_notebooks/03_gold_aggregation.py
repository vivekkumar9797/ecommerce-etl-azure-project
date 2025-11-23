# Gold Layer - Daily Sales Aggregation

from pyspark.sql.functions import to_date, sum

silver_path = "/mnt/silver/orders_clean"
gold_path = "/mnt/gold/daily_sales"

df = spark.read.format("delta").load(silver_path)

df_daily = (df.groupBy(to_date("timestamp").alias("date"))
              .agg(sum("amount").alias("total_sales"))
           )

df_daily.write.format("delta").mode("overwrite").save(gold_path)

print("Gold table created:", gold_path)
