## Exploratory Data Analysis

### Using R and xts
~~~
> head(GSPC)

            Open  High   Low Close   Volume AdjClose
1970-01-02 92.06 93.54 91.79 93.00  8050000    93.00
1970-01-05 93.00 94.25 92.53 93.46 11490000    93.46
1970-01-06 93.46 93.81 92.13 92.82 11460000    92.82
1970-01-07 92.82 93.38 91.93 92.63 10010000    92.63
1970-01-08 92.63 93.47 91.99 92.68 10670000    92.68
1970-01-09 92.68 93.25 91.82 92.40  9380000    92.40

> tail(GSPC)

              Open    High     Low   Close     Volume AdjClose
2016-02-03 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53
2016-02-04 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86

> nrow(GSPC)
[1] 11634

# All Adjusted Close prices are equal to Close prices

> nrow(GSPC[GSPC$Close != GSPC$AdjClose,])
[1] 0

# All Adjusted Close prices are equal to Close prices so it is not necessary to use Adjusted Close prices to calculate average prices

> avgPrice <- function(p) apply(p[,c("High","Low","Close")], 1, mean)

> GSPC$HLC <- avgPrice(GSPC)

> tail(GSPC)

              Open    High     Low   Close     Volume AdjClose      HLC
2016-02-03 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53 1900.923
2016-02-04 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45 1914.440
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05 1888.590
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44 1851.717
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21 1851.800
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86 1861.260


# Indicator of the tendency, related to the confidence whether the target margin is attainable, in the next k days

# T.ind is directly copied from the book "Data Mining with R"

T.ind <- function(quotes, tgt.margin = 0.025, n.days = 10) {
  v <- apply(HLC(quotes), 1, mean)
  r <- matrix(NA, ncol = n.days, nrow = NROW(quotes))
  for (x in 1:n.days) r[, x] <- Next(Delt(v, k = x), x)
  x <- apply(r, 1, function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x, time(quotes))
  else x
}

# T.ind2 is the corrected one, derivated from formulas in the book "Data Mining with R"

T.ind2 <- function(quotes, tgt.margin = 0.025, n.days = 10) {
  r <- matrix(NA, ncol = n.days, nrow = NROW(quotes))
  for (x in 1:n.days) r[, x] <- Next(Delt(quotes[, "HLC"], quotes[, "Close"], k = x), x)
  x <- apply(r, 1, function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x, time(quotes))
  else x
}

> setwd("/work/R/example/stocks")
> png(file = "GSPC_3m.png", width = 960, height = 720, bg = "transparent")

> candleChart(last(GSPC, "3 months"), theme = "white", TA = NULL)

> addAvgPrice <- newTA(FUN = avgPrice, col = 1, legend = "AvgPrice")
> addAvgPrice(on = 1)

> addT.ind <- newTA(FUN = T.ind, col = "blue", legend = "tgtRet")
> addT.ind()

> addT.ind2 <- newTA(FUN = T.ind2, col = "red", legend = "tgtRet2")
> addT.ind2()

dev.off()
~~~
![GSPC_3m](images/GSPC_3m.png)


### Using Spark and Spark-TS
~~~
bin/spark-shell --master spark://localhost:7077 \
--packages com.databricks:spark-csv_2.10:1.3.0 \
// --packages joda-time:joda-time:2.9.2 \
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


import java.sql.Timestamp
import java.time.ZonedDateTime

case class Ticker(date: Timestamp, symbol: String, open: Double, high: Double, low: Double, close: Double, volume: Long, adjClose: Double)

val UTC = ZoneId.of("Z")

val tickerDF = noHeaderRDD.map(_.split(",")).map {row => 
  val tokens = row(0).split('-')
  val dt = ZonedDateTime.of(tokens(0).toInt, tokens(1).toInt, tokens(2).toInt, 0, 0, 0, 0, UTC)
  Ticker(Timestamp.from(dt.toInstant), "GSPC", row(1).trim.toDouble, row(2).trim.toDouble, row(3).trim.toDouble, row(4).trim.toDouble, row(5).trim.toLong, row(6).trim.toDouble)
}.toDF()

tickerDF.cache()

tickerDF.show()

+--------------------+------+-----------+-----------+-----------+-----------+----------+-----------+
|                date|symbol|       open|       high|        low|      close|    volume|   adjClose|
+--------------------+------+-----------+-----------+-----------+-----------+----------+-----------+
|2016-02-09 19:00:...|  GSPC|1857.099976|1881.599976|1850.319946|1851.859985|4471170000|1851.859985|
|2016-02-08 19:00:...|  GSPC|1848.459961|    1868.25|1834.939941|1852.209961|5183220000|1852.209961|
|2016-02-07 19:00:...|  GSPC|    1873.25|    1873.25|1828.459961|1853.439941|5636460000|1853.439941|
|2016-02-04 19:00:...|  GSPC|1913.069946|1913.069946|1872.650024|1880.050049|4929940000|1880.050049|
|2016-02-03 19:00:...|  GSPC|1911.670044|1927.349976| 1900.52002|1915.449951|5193320000|1915.449951|
|2016-02-02 19:00:...|  GSPC|1907.069946| 1918.01001| 1872.22998|1912.530029|5172950000|1912.530029|
|2016-02-01 19:00:...|  GSPC| 1935.26001| 1935.26001|1897.290039|1903.030029|4463190000|1903.030029|
|2016-01-31 19:00:...|  GSPC|1936.939941|1947.199951|1920.300049|1939.380005|4322530000|1939.380005|
|2016-01-28 19:00:...|  GSPC|     1894.0| 1940.23999|     1894.0| 1940.23999|5497570000| 1940.23999|
|2016-01-27 19:00:...|  GSPC|1885.219971|1902.959961|1873.650024|1893.359985|4693010000|1893.359985|
|2016-01-26 19:00:...|  GSPC| 1902.52002| 1916.98999|1872.699951|1882.949951|4754040000|1882.949951|
|2016-01-25 19:00:...|  GSPC|1878.790039| 1906.72998|1878.790039|1903.630005|4357940000|1903.630005|
|2016-01-24 19:00:...|  GSPC|1906.280029|1906.280029|1875.969971|1877.079956|4401380000|1877.079956|
|2016-01-21 19:00:...|  GSPC|1877.400024|1908.849976|1877.400024|1906.900024|4901760000|1906.900024|
|2016-01-20 19:00:...|  GSPC|1861.459961|1889.849976| 1848.97998| 1868.98999|5078810000| 1868.98999|
|2016-01-19 19:00:...|  GSPC|1876.180054|1876.180054|1812.290039|1859.329956|6416070000|1859.329956|
|2016-01-18 19:00:...|  GSPC|1888.660034|1901.439941|1864.599976|1881.329956|4928350000|1881.329956|
|2016-01-14 19:00:...|  GSPC|1916.680054|1916.680054|1857.829956|1880.329956|5468460000|1880.329956|
|2016-01-13 19:00:...|  GSPC|1891.680054|1934.469971|1878.930054|1921.839966|5241110000|1921.839966|
|2016-01-12 19:00:...|  GSPC|1940.339966|1950.329956|1886.410034|1890.280029|5087030000|1890.280029|
+--------------------+------+-----------+-----------+-----------+-----------+----------+-----------+

tickerDF.printSchema()

root
 |-- date: timestamp (nullable = true)
 |-- symbol: string (nullable = true)
 |-- open: double (nullable = false)
 |-- high: double (nullable = false)
 |-- low: double (nullable = false)
 |-- close: double (nullable = false)
 |-- volume: long (nullable = false)
 |-- adjClose: double (nullable = false)

tickerDF.registerTempTable("gspc")

sqlContext.sql("SELECT count(*) FROM gspc").show()

+-----+
|  _c0|
+-----+
|16634|
+-----+


import java.time._
import java.time.format._
// import org.joda.time.DateTime
import com.cloudera.sparkts.DateTimeIndex
import com.cloudera.sparkts.DateTimeIndex._
import com.cloudera.sparkts.BusinessDayFrequency
import com.cloudera.sparkts._


TimeSeriesKryoRegistrator.registerKryoClasses(sc.getConf)

val dtIndex = uniformFromInterval(ZonedDateTime.of(1950, 1, 3, 0, 0, 0, 0, UTC), ZonedDateTime.of(2016, 2, 10, 0, 0, 0, 0, UTC), new BusinessDayFrequency(1))

dtIndex.first
java.time.ZonedDateTime = 1950-01-03T00:00Z

dtIndex.last
java.time.ZonedDateTime = 2016-02-10T00:00Z

dtIndex.size
Int = 17247

val tickerTS = TimeSeriesRDD.timeSeriesRDDFromObservations(dtIndex, tickerDF, "date", "symbol", "close")

// Count the number of series (number of symbols)

tickerTS.count
Long = 1
~~~

