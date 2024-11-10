# Install Spark-Hadoop on Windows

Follow these steps to install and set up Apache Spark with Hadoop on Windows:

### 1. Install Python (latest version)
Download and install the latest version of Python from [here](https://www.python.org/).

### 2. Install Java 11 (x64 for Windows)
Download and install Java 11 (x64) from [AdoptOpenJDK](https://adoptium.net/temurin/releases/?os=windows&arch=x64&package=jdk&version=11).

### 3. Download Apache Spark (version 3.5.3)
Download Apache Spark from [Apache Spark Downloads](https://spark.apache.org/downloads.html).

### 4. Download Winutils (version 3.3 / bin)
Download the necessary `winutils` from [kontext-tech/winutils GitHub](https://github.com/kontext-tech/winutils).

### 5. Place Apache Spark Folder
Place the Apache Spark folder in `C:/` and rename it to `spark`.

### 6. Place Winutils Folder
Place the `winutils` folder (version 3.3) in `C:/` and rename it to `hadoop`.

### 7. Set Environment Variables
Set the following environment variables:

- `JAVA_HOME` : `C:\Program Files\Eclipse Adoptium\jdk-11.0.25.9-hotspot`
- `HADOOP_HOME` : `C:\hadoop`
- `SPARK_HOME` : `C:\spark`

### 8. Add to System PATH
Add the following to your system PATH variable:

- `%SPARK_HOME%\bin`
- `%HADOOP_HOME%\bin`
- `%JAVA_HOME%\bin`

### 9. Verify Installation
- Open a Command Prompt (CMD) and run the following command:
  
  ```bash
  spark-shell
  ```

### 10. Download the Online Retail Dataset
Download the dataset from [UCI Machine Learning Repository: Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail).

### 11. Convert Dataset from `.xlsx` to `.csv`
Convert the downloaded `.xlsx` file to `.csv` format.

### 12. Load the Dataset into Spark
In `spark-shell`, load the `.csv` file using the following command:

```scala
val data = spark.read.option("header", "true").csv("C:/AMRI/Kuliah/Data science/spark program/Online Retail.csv")
```

### 13. Define a Variable for Item Counts
Group the data by `InvoiceNo` (or another relevant column) and count the occurrences:

```scala
val itemCounts = data.groupBy("InvoiceNo").count()
```

### 14. Preview the Results
Preview the `itemCounts` variable:

```scala
itemCounts.show()
```

### 15. Export the Results as CSV
Export the results to a CSV file:

```scala
itemCounts.write.option("header", "true").csv("C:/AMRI/Kuliah/Data science/spark program/output")
```
