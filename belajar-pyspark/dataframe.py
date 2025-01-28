from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("latihan_1").getOrCreate()

iris_df = spark.read.option("inferSchema", "true").option("header", "true").csv("D:/coding/python/dicoding-ds-ml-submission/belajar-pyspark/iris.csv")

iris_df.show(10)
iris_df.printSchema()

# iris_df.select("sepal_length").show(5) # untuk 1 kolom
iris_df.select(["sepal_length", "variety"]).show(5)

iris_df.select(iris_df["sepal_length"]*10).show(5)

iris_df.describe().show()

iris_df.summary().show()

iris_df.sort("sepal_length", ascending=False).show(5)
#iris_df.orderBy("sepal_length", ascending=False).show(5)
