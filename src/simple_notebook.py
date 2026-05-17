print("Hello from Databricks CI/CD pipeline!")

df = spark.createDataFrame(
    [("min", 1), ("Databricks", 2), ("Pipeline", 3)],
    ["name", "id"]
)

df.show()

df2 = df.withColumn("id_plus_one", df.id + 1)
df2.show()

assert df2.count() == 3
