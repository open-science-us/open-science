## Exploratory Data Analysis

### Overall
~~~
> import org.apache.spark.rdd.RDD
> import org.apache.spark.storage.StorageLevel

> import org.apache.spark.mllib.linalg.{Vector, Vectors}
> import org.apache.spark.sql.Row

> val rawDF = sqlContext.load("com.databricks.spark.csv", Map("path" -> "/home/ec2-user/data/airline/*.csv.bz2", "header" -> "true"))

> rawDF.show()

+----+-----+----------+---------+-------+----------+-------+----------+-------------+---------+-------+-----------------+--------------+-------+--------+--------+------+----+--------+------+-------+---------+----------------+--------+------------+------------+--------+-------------+-----------------+
|Year|Month|DayofMonth|DayOfWeek|DepTime|CRSDepTime|ArrTime|CRSArrTime|UniqueCarrier|FlightNum|TailNum|ActualElapsedTime|CRSElapsedTime|AirTime|ArrDelay|DepDelay|Origin|Dest|Distance|TaxiIn|TaxiOut|Cancelled|CancellationCode|Diverted|CarrierDelay|WeatherDelay|NASDelay|SecurityDelay|LateAircraftDelay|
+----+-----+----------+---------+-------+----------+-------+----------+-------------+---------+-------+-----------------+--------------+-------+--------+--------+------+----+--------+------+-------+---------+----------------+--------+------------+------------+--------+-------------+-----------------+
|1987|   10|        14|        3|    741|       730|    912|       849|           PS|     1451|     NA|               91|            79|     NA|      23|      11|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        15|        4|    729|       730|    903|       849|           PS|     1451|     NA|               94|            79|     NA|      14|      -1|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        17|        6|    741|       730|    918|       849|           PS|     1451|     NA|               97|            79|     NA|      29|      11|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        18|        7|    729|       730|    847|       849|           PS|     1451|     NA|               78|            79|     NA|      -2|      -1|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        19|        1|    749|       730|    922|       849|           PS|     1451|     NA|               93|            79|     NA|      33|      19|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        21|        3|    728|       730|    848|       849|           PS|     1451|     NA|               80|            79|     NA|      -1|      -2|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        22|        4|    728|       730|    852|       849|           PS|     1451|     NA|               84|            79|     NA|       3|      -2|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        23|        5|    731|       730|    902|       849|           PS|     1451|     NA|               91|            79|     NA|      13|       1|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        24|        6|    744|       730|    908|       849|           PS|     1451|     NA|               84|            79|     NA|      19|      14|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        25|        7|    729|       730|    851|       849|           PS|     1451|     NA|               82|            79|     NA|       2|      -1|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        26|        1|    735|       730|    904|       849|           PS|     1451|     NA|               89|            79|     NA|      15|       5|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        28|        3|    741|       725|    919|       855|           PS|     1451|     NA|               98|            90|     NA|      24|      16|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        29|        4|    742|       725|    906|       855|           PS|     1451|     NA|               84|            90|     NA|      11|      17|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|        31|        6|    726|       725|    848|       855|           PS|     1451|     NA|               82|            90|     NA|      -7|       1|   SAN| SFO|     447|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|         1|        4|    936|       915|   1035|      1001|           PS|     1451|     NA|               59|            46|     NA|      34|      21|   SFO| RNO|     192|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|         2|        5|    918|       915|   1017|      1001|           PS|     1451|     NA|               59|            46|     NA|      16|       3|   SFO| RNO|     192|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|         3|        6|    928|       915|   1037|      1001|           PS|     1451|     NA|               69|            46|     NA|      36|      13|   SFO| RNO|     192|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|         4|        7|    914|       915|   1003|      1001|           PS|     1451|     NA|               49|            46|     NA|       2|      -1|   SFO| RNO|     192|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|         5|        1|   1042|       915|   1129|      1001|           PS|     1451|     NA|               47|            46|     NA|      88|      87|   SFO| RNO|     192|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
|1987|   10|         6|        2|    934|       915|   1024|      1001|           PS|     1451|     NA|               50|            46|     NA|      23|      19|   SFO| RNO|     192|    NA|     NA|        0|              NA|       0|          NA|          NA|      NA|           NA|               NA|
+----+-----+----------+---------+-------+----------+-------+----------+-------------+---------+-------+-----------------+--------------+-------+--------+--------+------+----+--------+------+-------+---------+----------------+--------+------------+------------+--------+-------------+-----------------+

> rawDF.count

123,534,969


> rawDF.filter(rawDF("TailNum").isNotNull).count

123,534,969

> rawDF.filter(rawDF("TailNum") === "NA").count

37,245,646


> rawDF.filter(rawDF("ArrDelay").isNotNull).count

7,009,728

> rawDF.filter(rawDF("DepDelay").isNotNull).count

7,009,728

> rawDF.filter(rawDF("Distance").isNotNull).count

7,009,728



val delayDF = rawDF.select("TailNum", "ArrDelay", "DepDelay", "Distance")

delayDF.show()

+-------+--------+--------+--------+
|TailNum|ArrDelay|DepDelay|Distance|
+-------+--------+--------+--------+
|     NA|      23|      11|     447|
|     NA|      14|      -1|     447|
|     NA|      29|      11|     447|
|     NA|      -2|      -1|     447|
|     NA|      33|      19|     447|
|     NA|      -1|      -2|     447|
|     NA|       3|      -2|     447|
|     NA|      13|       1|     447|
|     NA|      19|      14|     447|
|     NA|       2|      -1|     447|
|     NA|      15|       5|     447|
|     NA|      24|      16|     447|
|     NA|      11|      17|     447|
|     NA|      -7|       1|     447|
|     NA|      34|      21|     192|
|     NA|      16|       3|     192|
|     NA|      36|      13|     192|
|     NA|       2|      -1|     192|
|     NA|      88|      87|     192|
|     NA|      23|      19|     192|
+-------+--------+--------+--------+

val rawPlaneDF = sqlContext.load("com.databricks.spark.csv", Map("path" -> "/home/ec2-user/data/airline/plane-data.csv","header" -> "true"))

rawPlaneDF.show()

+-------+----+------------+----------+-----+------+-------------+-----------+----+
|tailnum|type|manufacturer|issue_date|model|status|aircraft_type|engine_type|year|
+-------+----+------------+----------+-----+------+-------------+-----------+----+
| N050AA|null|        null|      null| null|  null|         null|       null|null|
| N051AA|null|        null|      null| null|  null|         null|       null|null|
| N052AA|null|        null|      null| null|  null|         null|       null|null|
| N054AA|null|        null|      null| null|  null|         null|       null|null|
| N055AA|null|        null|      null| null|  null|         null|       null|null|
| N056AA|null|        null|      null| null|  null|         null|       null|null|
| N057AA|null|        null|      null| null|  null|         null|       null|null|
| N058AA|null|        null|      null| null|  null|         null|       null|null|
| N059AA|null|        null|      null| null|  null|         null|       null|null|
| N060AA|null|        null|      null| null|  null|         null|       null|null|
| N061AA|null|        null|      null| null|  null|         null|       null|null|
| N062AA|null|        null|      null| null|  null|         null|       null|null|
| N063AA|null|        null|      null| null|  null|         null|       null|null|
| N064AA|null|        null|      null| null|  null|         null|       null|null|
| N065AA|null|        null|      null| null|  null|         null|       null|null|
| N066AA|null|        null|      null| null|  null|         null|       null|null|
| N067AA|null|        null|      null| null|  null|         null|       null|null|
| N068AA|null|        null|      null| null|  null|         null|       null|null|
| N069AA|null|        null|      null| null|  null|         null|       null|null|
| N070AA|null|        null|      null| null|  null|         null|       null|null|
+-------+----+------------+----------+-----+------+-------------+-----------+----+


> rawPlaneDF.count

5029

> rawPlaneDF.filter(rawPlaneDF("tailnum").isNotNull).count

5029

> rawPlaneDF.filter(rawPlaneDF("aircraft_type").isNotNull).count

4480

> val planeDF = rawPlaneDF.filter(rawPlaneDF("aircraft_type").isNotNull).select("tailnum", "aircraft_type")

> planeDF.show()

+-------+--------------------+
|tailnum|       aircraft_type|
+-------+--------------------+
| N10156|Fixed Wing Multi-...|
| N102UW|Fixed Wing Multi-...|
| N10323|Fixed Wing Multi-...|
| N103US|Fixed Wing Multi-...|
| N104UA|Fixed Wing Multi-...|
| N104UW|Fixed Wing Multi-...|
| N10575|Fixed Wing Multi-...|
| N105UA|Fixed Wing Multi-...|
| N105UW|Fixed Wing Multi-...|
| N106US|Fixed Wing Multi-...|
| N107UA|Fixed Wing Multi-...|
| N107US|Fixed Wing Multi-...|
| N108UW|Fixed Wing Multi-...|
| N109UW|Fixed Wing Multi-...|
| N110UW|Fixed Wing Multi-...|
| N11106|Fixed Wing Multi-...|
| N11107|Fixed Wing Multi-...|
| N11109|Fixed Wing Multi-...|
| N11113|Fixed Wing Multi-...|
| N11119|Fixed Wing Multi-...|
+-------+--------------------+

> planeDF.count

4480

> planeDF.select("aircraft_type").distinct.show()      

+--------------------+                                                          
|       aircraft_type|
+--------------------+
|          Rotorcraft|
|Fixed Wing Single...|
|             Balloon|
|Fixed Wing Multi-...|
+--------------------+

> val joinedDF = delayDF.join(planeDF, delayDF("TailNum") <=> planeDF("tailnum")).select("ArrDelay", "DepDelay", "Distance", "aircraft_type")

> joinedDF.show()

+--------+--------+--------+--------------------+                               
|ArrDelay|DepDelay|Distance|       aircraft_type|
+--------+--------+--------+--------------------+
|      -5|      -4|    1092|Fixed Wing Multi-...|
|      20|     -10|     194|Fixed Wing Multi-...|
|      49|      37|     956|Fixed Wing Multi-...|
|     102|     103|     644|Fixed Wing Multi-...|
|       0|      -3|     872|Fixed Wing Multi-...|
|     -13|      -6|     317|Fixed Wing Multi-...|
|     -17|      -3|     845|Fixed Wing Multi-...|
|       3|     -10|    1195|Fixed Wing Multi-...|
|      64|      54|     946|Fixed Wing Multi-...|
|     -11|      -6|     668|Fixed Wing Multi-...|
|      25|      17|     744|Fixed Wing Multi-...|
|     126|      91|    1201|Fixed Wing Multi-...|
|      -2|      -2|     872|Fixed Wing Multi-...|
|       8|      -8|     927|Fixed Wing Multi-...|
|      26|      10|     199|Fixed Wing Multi-...|
|      85|      91|     936|Fixed Wing Multi-...|
|     -13|      -4|     927|Fixed Wing Multi-...|
|      94|     105|    1201|Fixed Wing Multi-...|
|      64|      63|     809|Fixed Wing Multi-...|
|     -16|       0|    1008|Fixed Wing Multi-...|
+--------+--------+--------+--------------------+


> joinedDF.count

44,781,242       


> joinedDF.printSchema()

root
 |-- ArrDelay: string (nullable = true)
 |-- DepDelay: string (nullable = true)
 |-- Distance: string (nullable = true)
 |-- aircraft_type: string (nullable = true)


> val castedDF = joinedDF.selectExpr("cast(ArrDelay as double) as ArrDelay", "cast(DepDelay as double) as DepDelay", "cast(Distance as int) as Distance", "aircraft_type")

> castedDF.cache()

> castedDF.printSchema()

root
 |-- ArrDelay: double (nullable = true)
 |-- DepDelay: double (nullable = true)
 |-- Distance: integer (nullable = true)
 |-- aircraft_type: string (nullable = true)


> castedDF.count

44,781,242

> castedDF.filter(castedDF("ArrDelay").isNull).count

435,177

> castedDF.filter(castedDF("DepDelay").isNull).count

335,572

> castedDF.filter(castedDF("Distance").isNull).count

1,435

> castedDF.filter(castedDF("aircraft_type").isNull).count

0


> val goodDF = castedDF.filter(castedDF("ArrDelay").isNotNull).filter(castedDF("DepDelay").isNotNull).filter(castedDF("Distance").isNotNull)

> goodDF.count

44,344,658


> goodDF.filter(goodDF("ArrDelay").isNull).count
0
> goodDF.filter(goodDF("DepDelay").isNull).count
0
> goodDF.filter(goodDF("Distance").isNull).count
0


> goodDF.groupBy("aircraft_type").count().show()

+--------------------+--------+                                                 
|       aircraft_type|   count|
+--------------------+--------+
|          Rotorcraft|   30388|
|Fixed Wing Single...|  325642|
|             Balloon|   50450|
|Fixed Wing Multi-...|43938178|
+--------------------+--------+

> goodDF.groupBy("aircraft_type").agg(avg("ArrDelay"), avg("DepDelay")).show()

+--------------------+------------------+-----------------+                     
|       aircraft_type|     avg(ArrDelay)|    avg(DepDelay)|
+--------------------+------------------+-----------------+
|          Rotorcraft| 6.827069896011584| 9.08565881268922|
|Fixed Wing Single...|7.1810485133981485|8.684478660615031|
|             Balloon| 7.089415262636273|8.137561942517344|
|Fixed Wing Multi-...| 7.763177162239181|8.907016854454001|
+--------------------+------------------+-----------------+
~~~


