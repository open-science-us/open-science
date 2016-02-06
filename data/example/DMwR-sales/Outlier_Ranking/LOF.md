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
  (parts(1).substring(1, parts(1).length-1), parts(2).substring(1, parts(2).length-1), parts(6).toDouble, parts(5).substring(1, parts(5).length-1))
}
parsedRDD.persist(StorageLevel.MEMORY_ONLY_SER)

val nfRDD = parsedRDD.filter(t => t._4 != "fraud")
val uPriceRDD = nfRDD.map(t => (t._2, t._3))

object Neighbor2 {
  def lof2(xs: Seq[Double], k: Int):  Array[Double] = {
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
    
    for (i <- 0 until xs.size) {
      var ls = 0.0
      
      for (j <- 0 until k) {
        ls += lrds(knn(i)(j)._1)
      }
      
      lofs(i) = ls / k / lrds(i)
    }
    
    lofs
  }
}

import Neighbor2._

uPriceRDD.groupByKey().map{ t => (t._1, lof2(t._2.toSeq, 3)) }.take(1)

res24: Array[(String, Array[Double])] = Array((p888,Array(1.0610170758623598, 1.1237505618041288, 1.0244495380344383, 0.6278573059839813, 0.9427459759137612, 2.2175662121038537, 1.1250437214339912, 1.0789970238313962, 1.163987056270633, 1.126237553245514, 1.5412455769599926, 0.9338016279188617, 3.387877725797848, 0.8923829489867461, 1.1019257867544237, 1.3550497994799966, 1.0555254316401232, 1.258334025139751, 1.2901502477774205, 1.152915795731602, 1.046737422908462, 3.887671349776141, 0.9298387674091654, 1.1989309720690942, 1.121834804678539, 0.9625007632454563, 0.9730146569340613, 1.1251184001698238, 1.1490065191935932, 1.2205996066566376, 1.143255126184313, 2.223546010349797, 1.412460445615115, 3.387877725797848, 0.8923829489867461, 1.1019257867544237, 0.9457001783342768, 1.013876435...

~~~







