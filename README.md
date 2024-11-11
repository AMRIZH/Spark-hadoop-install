# Installing Apache Spark with Hadoop on Windows

Follow these steps to set up Apache Spark with Hadoop on a Windows system.

## Prerequisites

1. **Install Python**  
   - Download and install the latest version from the [Python website](https://www.python.org/).

2. **Install Java 11 (x64)**  
   - Download and install Java 11 (x64) from [Adoptium](https://adoptium.net/temurin/releases/?os=windows&arch=x64&package=jdk&version=11).

## Setup

3. **Download and Set Up Apache Spark (v3.5.3)**  
   - Download from [Apache Spark Downloads](https://spark.apache.org/downloads.html).
   - Extract the folder, move it to `C:/`, and rename it to `spark`.

4. **Download and Set Up Apache Hadoop (v3.4)**  
   - Download the binary version from [Hadoop Downloads](https://hadoop.apache.org/releases.html).
   - Extract the folder, move it to `C:/`, and rename it to `hadoop`.

5. **Download Winutils**  
   - Download `winutils.exe` (version 3.3 or later) from [kontext-tech/winutils on GitHub](https://github.com/kontext-tech/winutils).
   - Place `winutils.exe` in `C:\hadoop\bin`.

## Configure Environment Variables

6. Set the following environment variables:

   | Variable      | Value                                                      |
   |---------------|------------------------------------------------------------|
   | `JAVA_HOME`   | `C:\Program Files\Eclipse Adoptium\jdk-11.0.25.9-hotspot`  |
   | `HADOOP_HOME` | `C:\hadoop`                                                |
   | `SPARK_HOME`  | `C:\spark`                                                 |

   Add `%SPARK_HOME%\bin`, `%HADOOP_HOME%\bin`, and `%JAVA_HOME%\bin` to the system PATH.

## Verifying Installation

7. **Verify Spark Installation**  
   - Open Command Prompt and run:

     ```cmd
     spark-shell
     ```

     To specify the master node:

     ```cmd
     spark-shell --master local[*]
     ```

   - Access the Spark UI at `http://169.254.83.107:4040`.

8. **Verify Hadoop Installation**  
   - Run the following in Command Prompt:

     ```cmd
     hadoop version
     ```

   - Start HDFS and YARN:

     ```cmd
     start-dfs.cmd
     start-yarn.cmd
     ```

## Using Spark with a Dataset

9. **Download the Online Retail Dataset**  
   - Download from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).

10. **Convert Dataset from `.xlsx` to `.csv`**  
    - Use the provided script, [xlsxToCsv.py](xlsxToCsv.py), to convert the `.xlsx` file to `.csv`.

11. **Load the Dataset into Spark**  
    - In `spark-shell`, run:

      ```scala
      val data = spark.read.option("header", "true").csv("C:/Amri/HadoopSpark/Spark-hadoop-install/Online Retail.csv")
      ```

12. **Process the Data**  
    - Define a variable for counting items by `InvoiceNo`:

      ```scala
      val itemCounts = data.groupBy("InvoiceNo").count()
      ```

13. **Preview the Results**  
    - View the results in the `itemCounts` variable:

      ```scala
      itemCounts.show()
      ```

14. **Export the Results as CSV**  
    - Save the results to a `.csv` file:

      ```scala
      itemCounts.write.option("header", "true").csv("C:/Amri/HadoopSpark/Spark-hadoop-install/output")
      ```