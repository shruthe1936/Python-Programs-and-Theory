
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("Optimization") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

data = [
    (1, "Arun", 80),
    (2, "Priya", 90),
    (3, "Ravi", 75)
]

df = spark.createDataFrame(data, ["ID", "Name", "Marks"])

result = df.select("Name", "Marks").filter("Marks > 80")

print("Optimized Data:")
result.show()

spark.stop()
