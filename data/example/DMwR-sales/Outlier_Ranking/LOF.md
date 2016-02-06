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




~~~







