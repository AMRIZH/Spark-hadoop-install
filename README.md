# Install Spark-Hadoop on Windows

Follow these steps to set up Apache Spark with Hadoop on a Windows system.

## Prerequisites

### 1. Install Python (latest version)
   - Download and install the latest version of Python from the [Python website](https://www.python.org/).

### 2. Install Java 11 (x64 for Windows)
   - Download and install Java 11 (x64) from [Adoptium](https://adoptium.net/temurin/releases/?os=windows&arch=x64&package=jdk&version=11).

## Setup

### 3. Download and Set Up Apache Spark (version 3.5.3)
   - Download Apache Spark from [Apache Spark Downloads](https://spark.apache.org/downloads.html).
   - Extract the Spark folder and move it to `C:/`. Rename this folder to `spark`.

### 4. Download and Set Up Apache Hadoop
   - Download Hadoop from [Hadoop Downloads](https://hadoop.apache.org/releases.html). Choose the binary version.
   - Extract the Hadoop folder and move it to `C:/`. Rename this folder to `hadoop`.

### 5. Download Winutils
   - Download the necessary `winutils` binaries from [kontext-tech/winutils GitHub](https://github.com/kontext-tech/winutils).
   - Place the `winutils.exe` file in `C:\hadoop\bin`.

## Environment Variables

### 6. Configure Environment Variables
   Set the following environment variables in your system:

   ```cmd
   set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-11.0.25.9-hotspot
   set SPARK_HOME=C:\spark
   set HADOOP_HOME=C:\hadoop

   set PATH=%PATH%;%JAVA_HOME%\bin
   set PATH=%PATH%;%SPARK_HOME%\bin;%SPARK_HOME%\sbin
   set PATH=%PATH%;%HADOOP_HOME%\bin;%HADOOP_HOME%\sbin
   ```

## Verifying Installation

### 7. Verify Apache Spark Installation
   - Open a Command Prompt and run the following command to start the Spark shell:

     ```cmd
     spark-shell
     ```

     Alternatively, you can specify the master node:

     ```cmd
     spark-shell --master local[*]
     ```

   - Access the Spark UI at `http://169.254.83.107:4040`.

### 8. Verify Hadoop Installation
   - In Command Prompt, check the Hadoop installation by running:

     ```cmd
     hadoop version
     ```

   - Start HDFS and YARN:

     ```cmd
     start-dfs.cmd
     start-yarn.cmd
     ```

## Using Spark with a Dataset

### 9. Download the Online Retail Dataset
   - Download the Online Retail dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).

### 10. Convert Dataset from `.xlsx` to `.csv`
   - Convert the downloaded `.xlsx` file to `.csv` format. You can use the provided script, [xlsxToCsv.py](xlsxToCsv.py), for this conversion.

### 11. Load the Dataset into Spark
   - In `spark-shell`, load the `.csv` file with the following command:

     ```scala
     val data = spark.read.option("header", "true").csv("C:/AMRI/Kuliah/Data science/spark program/Online Retail.csv")
     ```

### 12. Process the Data
   - Define a variable for counting items by `InvoiceNo`:

     ```scala
     val itemCounts = data.groupBy("InvoiceNo").count()
     ```

### 13. Preview the Results
   - View the results in the `itemCounts` variable:

     ```scala
     itemCounts.show()
     ```

### 14. Export the Results as CSV
   - Save the results to a `.csv` file:

     ```scala
     itemCounts.write.option("header", "true").csv("C:/AMRI/Kuliah/Data science/spark program/output")
     ```
