## [Local Outlier Factor](https://en.wikipedia.org/wiki/Local_outlier_factor)

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

import java.lang.Math._

object Neighbor {
  private def distanceImpl(xs: Seq[Double]): Array[Array[(Int, Double)]] = {
    // to be optimized
    val ds = Array.ofDim[(Int, Double)](xs.size, xs.size)
    
    for (i <- 0 until xs.size; j<- 0 until xs.size) {
      ds(i)(j) = (j, abs(xs(i) - xs(j)))
    }
    
    ds
  }
  
  private def knnImpl(ds: Array[Array[(Int, Double)]], k: Int): Array[Array[(Int, Double)]] = {
    val knn = Array.ofDim[(Int, Double)](ds.length, k)
    
    for (i <- 0 until ds.length) {
      val sm = ds(i).sortBy(t => t._2)  
      
      // get rid of duplicated points
      var z0 = 0;
      while (sm(z0)._2 == 0 & z0 < ds.length) z0 = z0 + 1
      
      var max = 0.0
      for (j <- 0 until k) {
        if ((z0+j) < ds.length) {
          knn(i)(j) = sm(z0+j)
          max = sm(z0+j)._2
        } else knn(i)(j) = (i, max)
      }
    }
    
    knn
  }
  
  private def lrdImpl(ds: Array[Array[(Int, Double)]], knn: Array[Array[(Int, Double)]], k: Int): Array[Double] = {
    val lrds = new Array[Double](ds.length)
    
    for (i <- 0 until ds.length) {
      var rd = 0.0
      var count = 0
      
      for (j <- 0 until k) {
        var b = knn(i)(j)._1
        
        if (b != i) {
          count = count + 1
          if (knn(b)(k-1)._2 > ds(i)(b)._2) rd += knn(b)(k-1)._2
          else rd += ds(i)(b)._2
        }
      }
      
      if (count == 0 || rd == 0.0) lrds(i) = 0.0
      else lrds(i) = count / rd
    }

    lrds
  }
  
  private def normalizeLOF(lofs: Array[Double]): Array[Double] = {
    if (lofs.size == 1) {
      lofs(0) = 0.0
    } else {
      var minLof = lofs(0); var maxLof = lofs(0)
      
      for (i <- 1 until lofs.length) {
        if (lofs(i) < minLof) minLof = lofs(i)
        else if (lofs(i) > maxLof) maxLof = lofs(i)
      }
      
      if (maxLof == minLof) {
        for (i <- 0 until lofs.length) {
          lofs(i) = 0.0
        }
      } else {
        for (i <- 0 until lofs.length) {
          lofs(i) = (lofs(i) - minLof) / (maxLof - minLof)
        }
      }
    }
    
    lofs
  }
  
  def lof2(xs: Seq[Double], k: Int):  Array[Double] = {
    if (xs.size <= k) {
      val lofs = new Array[Double](xs.size)
      
      for (i <- 0 until xs.size) lofs(i) = 0.0
      
      return lofs
    }
    
    val ds = distanceImpl(xs)
    
    val knn = knnImpl(ds, k)
    
    val lrds = lrdImpl(ds, knn, k)
    
    val lofs = new Array[Double](xs.size)
    
    for (i <- 0 until xs.size) {
      var ls = 0.0
      var count = 0
      
      for (j <- 0 until k) {
        var b = knn(i)(j)._1
        
        if (b != i) {
          count = count + 1
          ls += lrds(knn(i)(j)._1)
        }
      }
      
      if (count == 0) lofs(i) = 1.0
      else lofs(i) = ls / count / lrds(i)
    }

    normalizeLOF(lofs)
  }
}

import Neighbor._

case class LofScore(Prod: String, Uprice: Double, Insp: String, ID: String, LOF: Double)

val resDF = parsedRDD.groupBy(x => x._1).flatMap {t =>
  val lf2 = lof2(t._2.map(t => t._2).toSeq, 7)

  val m = t._2 zip lf2

  m.map(t => LofScore(t._1._1, t._1._2, t._1._3, t._1._4, t._2))
}.toDF

resDF.show()

+----+----------------+----+----+--------------------+                          
|Prod|          Uprice|Insp|  ID|                 LOF|
+----+----------------+----+----+--------------------+
|p888|14.0107913669065|  ok|v805|0.052659625003884054|
|p888|10.8677685950413|  ok|v474|0.036162154518614695|
|p888|4.37123169681309|  ok|v806| 0.03345011586986922|
|p888|5.85714285714286|  ok|v654| 0.02533299058203707|
|p888|7.51766784452297|  ok|v807| 0.03348365984591198|
|p888|3.61889961645285|  ok|v808| 0.03554912268685448|
|p888|14.5907928388747|  ok|v809| 0.04044545241257655|
|p888|13.2857142857143|  ok|v810| 0.03870865363817622|
|p888|2.76946786329435|  ok|v811|0.040440706241494255|
|p888|10.6954887218045|  ok|v671| 0.03876094222747267|
|p888|10.8208955223881|  ok| v15|0.028028570599895584|
|p888|5.35310394610202|  ok|v423|0.035351736016815016|
|p888|6.92920681986657|  ok|v333|0.038579284393471566|
|p888|           9.725|  ok|v333| 0.02482881814291988|
|p888|27.6111111111111|  ok| v19| 0.03347783191599212|
|p888|22.2839506172839|  ok|v528| 0.03511133333932357|
|p888|8.87387387387387|  ok|v596| 0.03480933670799556|
|p888|11.1818181818182|  ok|v506| 0.04385817977831956|
|p888|4.69059405940594|  ok|v538| 0.03685191766597308|
|p888|3.28777777777778|  ok|v538|0.030263620162344736|
+----+----------------+----+----+--------------------+

resDF.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("/work/R/example/lofData.csv")
~~~

### PR charts with R
~~~
> setwd("/work/R/example")
 
> sales <- read.csv('lofData.csv', header=TRUE)
> 
> head(sales)

  Prod    Uprice Insp   ID        LOF
1 p888 14.010791   ok v805 0.05265963
2 p888 10.867769   ok v474 0.03616215
3 p888  4.371232   ok v806 0.03345012
4 p888  5.857143   ok v654 0.02533299
5 p888  7.517668   ok v807 0.03348366
6 p888  3.618900   ok v808 0.03554912

> attach(sales)


> library(ROCR)

> knownSales <- sales[Insp == 'fraud' | Insp == 'ok',]

> knownSales$Label <- 0

> knownSales[knownSales$Insp == 'fraud', 'Label'] <- 1

> par(mfrow= c(2,2))

> pred <- prediction(knownSales$LOF, knownSales$Label)

> perf <- performance(pred, "prec", "rec")

> plot(perf, main = "PR Chart")

IPRcurve <- function(preds, trues, ...) {
  require(ROCR, quietly = T)
  
  pd <- prediction(preds, trues)
  pf <- performance(pd, "prec", "rec")
  pf@y.values <- lapply(pf@y.values, function(x) rev(cummax(rev(x))))

  plot(pf, ...)
}

> IPRcurve(knownSales$LOF, knownSales$Label, main = "Interpolated PR Chart")

> perf <- performance(pred, "lift", "rpp")

> plot(perf, main = "Lift Chart")

CRchart <- function(preds, trues, ...) {
  require(ROCR, quietly = T)

  pd <- prediction(preds, trues)
  pf <- performance(pd, "rec", "rpp")
 
  plot(pf, ...)
}

> CRchart(knownSales$LOF, knownSales$Label, main = "Cumulative Recall Chart")
~~~
![LOF_PR_Charts](../images/LOF_PR_charts.png)


### Ranking with R
~~~
> install.packages('Rlof')

> library('Rlof')


> setwd("/work/R/example")
 
> load('salesClean.rdata')
 
> attach(sales)

> prodAgg <- split(Uprice, Prod)


> lofs <- numeric()

# Testing,  for (prod in c('p1', 'p2', 'p3')) {
for (prod in levels(Prod)) {
  l <- length(prodAgg[[prod]])
  
  if (l <= 7) lofs <- c(lofs, rep(0.0, each=l))
  else lofs <- c(lofs, lof(prodAgg[[prod]], 7))

  print(prod)
}

> length(which(is.nan(lofs)))
[1] 4307

> length(which(is.infinite(lofs)))
[1] 2613

> fivenum(lofs[which(!is.infinite(lofs) & !is.nan(lofs))])
[1] 7.803117e-01 9.909313e-01 1.038009e+00 1.257241e+00 5.937395e+05

# NaN and Infinite numbers are from duplicated Uprice


> length(prodAgg[['p1']])
[1] 196

> length(which(duplicated(prodAgg[['p1']])))
[1] 76
> 

> duplicates <- 0

for (prod in levels(Prod)) {
  duplicates <- duplicates + length(which(duplicated(prodAgg[[prod]])))
}

> duplicates
[1] 94385

> duplicates / nrow(sales) * 100
[1] 23.58422

# 23.6% Uprices are duplicated


> dups <- numeric(length(levels(Prod)))

i <- 1
for (prod in levels(Prod)) {
  dups[i] <- length(which(duplicated(prodAgg[[prod]]))) / length(prodAgg[[prod]])
  i <- i + 1
}

> lengths <- numeric(length(levels(Prod)))

i <- 1
for (prod in levels(Prod)) {
  lengths[i] <- length(prodAgg[[prod]])
  i <- i + 1
}

> df <- data.frame(cbind(levels(Prod), lengths, dups))

> df[order(df$dups, decreasing=T)[1:10],]

        V1 lengths              dups
638   p638      11 0.818181818181818
826   p826      11 0.818181818181818
259   p259      20              0.75
4197 p4199      16              0.75
4434 p4436      12              0.75
2300 p2300      19 0.736842105263158
695   p695      14 0.714285714285714
689   p689      13 0.692307692307692
3330 p3332      26 0.692307692307692
4145 p4147      19 0.684210526315789


> lofs <- numeric()

for (prod in levels(Prod)) {
  u <- unique(prodAgg[[prod]])
  
  l <- length(u)
  
  if (l <= 7) lofs <- c(lofs, rep(0.0, each=l))
  else lofs <- c(lofs, lof(u, 7))
   
  print(prod)
}

> length(which(is.nan(lofs) | is.infinite(lofs)))
[1] 0

> fivenum(lofs)
[1] 0.000000e+00 9.888399e-01 1.036028e+00 1.176084e+00 1.903022e+04
~~~




