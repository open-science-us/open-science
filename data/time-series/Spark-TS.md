## [Spark-TS](https://github.com/cloudera/spark-timeseries)

### Building Spark-TS package
~~~
# Downloading the whole packge from GitHub to /work/spark-TS/

$ cd /work/spark-TS/spark-timeseries-master

$ mvn package
~~~

### Examples
~~~
bin/spark-shell --master spark://localhost:7077 \
--packages com.databricks:spark-csv_2.10:1.3.0 --packages joda-time:joda-time:2.9.2 \
--jars /work/spark-TS/spark-timeseries-master/target/sparkts-0.3.0-SNAPSHOT-jar-with-dependencies.jar \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer


import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel

val rawRDD = sc.textFile("/work/R/example/stocks/GSPC.csv")

rawRDD.take(10).foreach(println)

Date,Open,High,Low,Close,Volume,Adj Close
2016-02-10,1857.099976,1881.599976,1850.319946,1851.859985,4471170000,1851.859985
2016-02-09,1848.459961,1868.25,1834.939941,1852.209961,5183220000,1852.209961
2016-02-08,1873.25,1873.25,1828.459961,1853.439941,5636460000,1853.439941
2016-02-05,1913.069946,1913.069946,1872.650024,1880.050049,4929940000,1880.050049
2016-02-04,1911.670044,1927.349976,1900.52002,1915.449951,5193320000,1915.449951
2016-02-03,1907.069946,1918.01001,1872.22998,1912.530029,5172950000,1912.530029
2016-02-02,1935.26001,1935.26001,1897.290039,1903.030029,4463190000,1903.030029
2016-02-01,1936.939941,1947.199951,1920.300049,1939.380005,4322530000,1939.380005
2016-01-29,1894.00,1940.23999,1894.00,1940.23999,5497570000,1940.23999


val noHeaderRDD = rawRDD.mapPartitionsWithIndex { (idx, iter) => if (idx == 0) iter.drop(1) else iter }

case class YahooStockPrice(date: String, open: Float, high: Float, low: Float, close: Float, volume: Long, adjClose: Float)

val df = noHeaderRDD.map(_.split(",")).map(row => YahooStockPrice(row(0), row(1).trim.toFloat, row(2).trim.toFloat, row(3).trim.toFloat, row(4).trim.toFloat, row(5).trim.toLong, row(6).trim.toFloat)).toDF()

df.cache()

df.show()

+----------+-------+-------+-------+-------+----------+--------+
|      date|   open|   high|    low|  close|    volume|adjClose|
+----------+-------+-------+-------+-------+----------+--------+
|2016-02-10| 1857.1| 1881.6|1850.32|1851.86|4471170000| 1851.86|
|2016-02-09|1848.46|1868.25|1834.94|1852.21|5183220000| 1852.21|
|2016-02-08|1873.25|1873.25|1828.46|1853.44|5636460000| 1853.44|
|2016-02-05|1913.07|1913.07|1872.65|1880.05|4929940000| 1880.05|
|2016-02-04|1911.67|1927.35|1900.52|1915.45|5193320000| 1915.45|
|2016-02-03|1907.07|1918.01|1872.23|1912.53|5172950000| 1912.53|
|2016-02-02|1935.26|1935.26|1897.29|1903.03|4463190000| 1903.03|
|2016-02-01|1936.94| 1947.2| 1920.3|1939.38|4322530000| 1939.38|
|2016-01-29| 1894.0|1940.24| 1894.0|1940.24|5497570000| 1940.24|
|2016-01-28|1885.22|1902.96|1873.65|1893.36|4693010000| 1893.36|
|2016-01-27|1902.52|1916.99| 1872.7|1882.95|4754040000| 1882.95|
|2016-01-26|1878.79|1906.73|1878.79|1903.63|4357940000| 1903.63|
|2016-01-25|1906.28|1906.28|1875.97|1877.08|4401380000| 1877.08|
|2016-01-22| 1877.4|1908.85| 1877.4| 1906.9|4901760000|  1906.9|
|2016-01-21|1861.46|1889.85|1848.98|1868.99|5078810000| 1868.99|
|2016-01-20|1876.18|1876.18|1812.29|1859.33|6416070000| 1859.33|
|2016-01-19|1888.66|1901.44| 1864.6|1881.33|4928350000| 1881.33|
|2016-01-15|1916.68|1916.68|1857.83|1880.33|5468460000| 1880.33|
|2016-01-14|1891.68|1934.47|1878.93|1921.84|5241110000| 1921.84|
|2016-01-13|1940.34|1950.33|1886.41|1890.28|5087030000| 1890.28|
+----------+-------+-------+-------+-------+----------+--------+


df.printSchema()

root
 |-- date: string (nullable = true)
 |-- open: float (nullable = false)
 |-- high: float (nullable = false)
 |-- low: float (nullable = false)
 |-- close: float (nullable = false)
 |-- volume: long (nullable = false)
 |-- adjClose: float (nullable = false)

df.registerTempTable("gspc")

sqlContext.sql("SELECT count(*) FROM gspc").show()
+-----+
|  _c0|
+-----+
|16634|
+-----+


import java.time._
import java.time.format._
import org.joda.time.DateTime
import com.cloudera.sparkts.DateTimeIndex
import com.cloudera.sparkts.BusinessDayFrequency

val UTC = ZoneId.of("Z")

val dtIndex = uniform(ZonedDateTime.of(1950, 1, 3, 0, 0, 0, 0, UTC), 16634, new BusinessDayFrequency(1))

dtIndex.last

java.time.ZonedDateTime = 2013-10-04T00:00Z
~~~



