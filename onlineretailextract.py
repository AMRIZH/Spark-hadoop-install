from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Inisialisasi SparkSession
spark = SparkSession.builder \
    .appName("Item Count Program") \
    .getOrCreate()

# 2. Baca File Dataset onlineRetail.csv
# Menggunakan kolom 'item_id' dari file CSV hasil konversi
data = spark.read.option("header", "true").csv("Online Retail.csv")

# 3. Hitung Jumlah Kemunculan Setiap Item ID
item_count = data.groupBy("item_id").count()

# 4. Simpan Hasil ke File Output
item_count.write.mode("overwrite").csv("item_counts.csv")

# 5. Stop SparkSession
spark.stop()
