# [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)


## [Apache Commons Math 3.6 API](https://commons.apache.org/proper/commons-math/apidocs/org/apache/commons/math3/stat/inference/KolmogorovSmirnovTest.html)

## [KolmogorovSmirnovTest.java](https://commons.apache.org/proper/commons-math/jacoco/org.apache.commons.math3.stat.inference/KolmogorovSmirnovTest.java.html)


## Case One:  Fraud Detection

Carry out Kolmogorov-Smirnov test to compare the two distributions of unit prices in sales data for fraud detection.


**Method 1 estimation method:** Call bootstrap to search for top N products for each of the products that has less than 20 transactions. 

**Method 2 kolmogorovSmirnovTest method:** Call kolmogorovSmirnovTest against top N products to find the one with the highest p-value for each of the products that has less than 20 transactions. 
 


*** Scala Code
~~~
import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel

import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.sql.Row


// Pre-Processing

val rawRDD = sc.textFile("/work/R/example/salesClean.csv")

val noHeaderRDD = rawRDD.mapPartitionsWithIndex { (idx, iter) => if (idx == 0) iter.drop(1) else iter }


val parsedRDD = noHeaderRDD.map { line =>
  val parts = line.split(',')
  (parts(2).substring(1, parts(2).length-1), parts(6).toDouble, parts(5).substring(1, parts(5).length-1))
}

val uPriceRDD = parsedRDD.map(t => (t._1, t._2, t._3))

uPriceRDD.persist(StorageLevel.MEMORY_ONLY_SER)


val smallRDD = uPriceRDD.map(t => (t._1, t._2)).groupByKey().filter(t => t._2.size < 20)

val smalls = smallRDD.collect()

val bigRDD = uPriceRDD.map(t => (t._1, (t._2, t._3))).groupByKey().filter(t => t._2.size >= 20).map {t => 
  (t._1, t._2.filter(t2 => t2._2 != "fraud").map(t2 => t2._1))
}


// Kolmogorov-Smirnov test

var i: Int = 0
var j: Int = 0

var result = new Array[(String, Option[(Double, String)])](smalls.size)

val start0 = System.currentTimeMillis
var start = start0
var period = start

for (i <- 0 to (smalls.size - 1)) {
  val s = sc.broadcast(smalls(i)._2)

  val es = bigRDD.map {t =>
    (new KolmogorovSmirnovTest().bootstrap(t._2.toArray, s.value.toArray, 30), t._1)
  }.top(15)

  val top = sc.broadcast(es.map(t => t._2))

  val ks = bigRDD.filter(t => top.value.contains(t._1)).map {t =>
    (new KolmogorovSmirnovTest().kolmogorovSmirnovTest(t._2.toArray, s.value.toArray), t._1)
  }

  var tmp = System.currentTimeMillis
  period = (tmp - start) / 1000
  start = tmp

  println("i: " + i + "\ttakes " + period)

  if ((i+1) % 100 == 0) println("i: " + i + "\t totally takes " + ((start - start0) / 1000))

  result(i) = (smalls(i)._1, ks.top(1).lift(0))
}

println("total takes " + ((start - start0) / 1000))



// Saving results in files

import java.io._

val pw = new PrintWriter(new File("/work/R/example/similars.txt"))

result.foreach(pw.println)

pw.close


val pw9 = new PrintWriter(new File("/work/R/example/similars-0.9.txt"))

result.filter(t => t._2.get._1 >= 0.9).foreach(pw9.println)

pw9.close
~~~







