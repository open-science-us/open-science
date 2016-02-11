## [Spark-TS](https://github.com/cloudera/spark-timeseries)

### Building
~~~
cd /work/spark-TS/spark-timeseries-master

mvn package

# Building jar: /work/spark-TS/spark-timeseries-master/target/sparkts-0.3.0-SNAPSHOT-javadoc.jar
~~~

### 
~~~
bin/spark-shell --master spark://localhost:7077 --packages com.databricks:spark-csv_2.10:1.3.0 --jars /work/spark-TS/spark-timeseries-master/target/sparkts-0.3.0-SNAPSHOT-jar-with-dependencies.jar --conf spark.serializer=org.apache.spark.serializer.KryoSerializer
~~~
