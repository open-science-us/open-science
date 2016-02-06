## [Local Outlier Factor](https://en.wikipedia.org/wiki/Local_outlier_factor)

### Ranking with R
~~~
> install.packages('Rlof')

> library('Rlof')


> setwd("/work/R/example")
 
> load('salesClean.rdata')
 
> attach(sales)

> prodGroup <- split(Uprice, Prod)


> lofs <- numeric()

# Testing,  for (prod in c('p1', 'p2', 'p3')) {
> for (prod in levels(Prod)) {
+   lofp <- lof(prodGroup[[prod]], 3)
+   lofs <- c(lofs, lofp)
+   print(prod)
+ }

> length(which(is.nan(lofs)))
[1] 53461

> length(which(is.infinite(lofs)))
[1] 28742

> fivenum(lofs[which(!is.infinite(lofs) & !is.nan(lofs))])
[1] 6.984415e-01 1.000000e+00 1.051868e+00 1.386961e+00 3.936752e+14

# NaN and Infinite numbers are from duplicated Uprice

> lofs <- numeric()

> for (prod in levels(Prod)) {
+   u <- unique(prodGroup[[prod]])
+    
+   if (length(u) <= 3) {
+     for (p in prodGroup[[prod]]) {
+        lofs <- c(lofs, 1.0)
+     }
+   } else {
+     lofs <- c(lofs, lof(u, 3))
+   }
+    
+   print(prod)
+ }

> length(which(is.nan(lofs) | is.infinite(lofs)))
[1] 0

> fivenum(lofs)
[1] 7.015293e-01 9.777819e-01 1.065522e+00 1.265046e+00 7.313760e+04


> lof1 <- lof(unique(prodGroup[['p1']]), 3)

> cl <- cbind(prodGroup[['p1']], lof1)
~~~


### Ranking with Spark
~~~
bin/spark-shell --master spark://localhost:7077 --packages com.databricks:spark-csv_2.10:1.3.0 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer

import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel

val rawRDD = sc.textFile("/work/R/example/salesClean.csv")
val noHeaderRDD = rawRDD.mapPartitionsWithIndex { (idx, iter) => if (idx == 0) iter.drop(1) else iter }

val parsedRDD = noHeaderRDD.map { line =>
  val parts = line.split(',')
  (parts(2).substring(1, parts(2).length-1), parts(6).toDouble, parts(5).substring(1, parts(5).length-1), parts(1).substring(1, parts(1).length-1))
}
parsedRDD.persist(StorageLevel.MEMORY_ONLY_SER)

parsedRDD.take(10).foreach(println)

(p1,9.14835164835165,unkn,v1)
(p1,2.85807291666667,unkn,v2)
(p1,3.7753150590889,unkn,v3)
(p1,9.82142857142857,unkn,v4)
(p1,3.28682673588579,unkn,v3)
(p2,11.1057692307692,unkn,v5)
(p2,16.2285714285714,unkn,v6)
(p2,20.05,unkn,v7)
(p2,12.2532188841202,unkn,v8)
(p2,9.95762711864407,unkn,v9)

// val nfRDD = parsedRDD.filter(t => t._4 != "fraud")
// val uPriceRDD = parsedRDD.map(t => (t._1, (t._2, t._3, t._4)))

import java.lang.Math._

object Neighbor3 {
  def lof3(xs: Seq[Double], k: Int):  Array[Double] = {
    val ds = Array.ofDim[(Int, Double)](xs.size, xs.size)
    
    for (i <- 0 until xs.size; j<- 0 until xs.size) {
      ds(i)(j) = (j, abs(xs(i) - xs(j)))
    }
    
    val knn = Array.ofDim[(Int, Double)](xs.size, k)
    
    for (i <- 0 until xs.size) {
      val sm = ds(i).sortBy(t => t._2)
      
      var z0 = 0;
      while (sm(z0)._2 == 0 & z0 < xs.size) z0 = z0 + 1
      
      for (j <- 0 until k) {
        if ((z0+j) < xs.size) knn(i)(j) = sm(z0+j)
      }
    }
    
    val lrds = new Array[Double](xs.size)
    
    for (i <- 0 until xs.size) {
      var rd = 0.0
      
      for (j <- 0 until k) {        
        if (knn(knn(i)(j)._1)(k-1)._2 > ds(i)(knn(i)(j)._1)._2) rd += knn(knn(i)(j)._1)(k-1)._2
        else rd += ds(i)(knn(i)(j)._1)._2
      }
      
      lrds(i) = k / rd
    }
    
    val lofs = new Array[Double](xs.size)
    
    var minLof = 0.0; var maxLof = 0.0
    
    for (i <- 0 until xs.size) {
      var ls = 0.0
      
      for (j <- 0 until k) {
        ls += lrds(knn(i)(j)._1)
      }
      
      lofs(i) = ls / k / lrds(i)
      
      if (lofs(i) < minLof) minLof = lofs(i)
      else if (lofs(i) > maxLof) maxLof = lofs(i)
    }
    
    if (maxLof == minLof) {
      for (i <- 0 until xs.size) {
        lofs(i) = 0.0
      }
    } else {
      for (i <- 0 until xs.size) {
        lofs(i) = lofs(i) / (maxLof - minLof)
      }
    }
    
    lofs
  }
}

import Neighbor3._

case class LofScore(prod: String, price: Double, insp: String, id: String, lot: Double)

val resDF = parsedRDD.groupBy(x => x._1).flatMap {t =>
  val lf3 = lof3(t._2.map(t => t._2).toSeq, 3)

  val m = t._2 zip lf3

  m.map(t => LofScore(t._1._1, t._1._2, t._1._3, t._1._4, t._2))
}.toDF

resDF.show()

+----+----------------+----+----+-------------------+                           
|prod|           price|insp|  id|                lot|
+----+----------------+----+----+-------------------+
|p888|14.0107913669065|  ok|v805|0.07273692498549779|
|p888|10.8677685950413|  ok|v474|0.07703755403740682|
|p888|4.37123169681309|  ok|v806|0.07023007536318415|
|p888|5.85714285714286|  ok|v654|0.04304210630148039|
|p888|7.51766784452297|  ok|v807|0.06462897241751338|
|p888|3.61889961645285|  ok|v808| 0.1520229512697277|
|p888|14.5907928388747|  ok|v809| 0.0771262052543678|
|p888|13.2857142857143|  ok|v810|0.07396952166694518|
|p888|2.76946786329435|  ok|v811|0.07979592517607186|
|p888|10.6954887218045|  ok|v671|0.07720804715578061|
|p888|10.8208955223881|  ok| v15|0.10565849171131729|
|p888|5.35310394610202|  ok|v423| 0.0640158019191777|
|p888|6.92920681986657|  ok|v333|0.23225244306375725|
|p888|           9.725|  ok|v333|0.06117638735081638|
|p888|27.6111111111111|  ok| v19|0.07554137922389072|
|p888|22.2839506172839|  ok|v528|0.09289403333709993|
|p888|8.87387387387387|  ok|v596|0.07236045101262115|
|p888|11.1818181818182|  ok|v506|0.08626378375569417|
|p888|4.69059405940594|  ok|v538|0.08844491189393562|
|p888|3.28777777777778|  ok|v538|0.07903694639463436|
+----+----------------+----+----+-------------------+


~~~







