# Silver Layer - Clean & Transform

bronze_path = "/mnt/bronze/orders"
silver_path = "/mnt/silver/orders_clean"

from pyspark.sql.functions import col

df_bronze = spark.read.format("delta").load(bronze_path)

df_clean = (df_bronze
            .withColumn("amount", col("amount").cast("double"))
            .withColumn("order_id", col("order_id").cast("int"))
            .withColumn("customer_id", col("customer_id").cast("int"))
           )

df_clean.write.format("delta").mode("overwrite").save(silver_path)

print("Silver table created:", silver_path)
