## Products withe few (<20) transactions

~~~
> setwd("/work/R/example")
 
> load('salesClean.rdata')

> attach(sales)

> notF <- which(Insp != 'fraud')

> mi <- function(x) { 
+   bp <- boxplot.stats(x)$stats 
+   c(median = bp[3], iqr = bp[4]-bp[2])
+ }

> ms <- tapply(Uprice[notF], list(Prod=Prod[notF]), mi)

> m <- matrix(unlist(ms), length(ms), 2, byrow=T, dimnames=list(names(ms), c('median', 'iqr')))

> par(mfrow= c(1,2))

> plot(m[,1], m[,2], xlab="Median", ylab="IQR", main="")
 
> plot(m[,1], m[,2], xlab="Median", ylab="IQR", main="", col="grey", log="xy")

> smalls <- which(table(Prod) < 20)

> length(smalls)
[1] 985
 
> points(log(m[smalls, 1]), log(m[smalls, 2]), pch="+")
~~~
![Small Products](../images/smalls.png)

### Kolmogorov–Smirnov test

[Using Spark with Apache Commons Math 3.6 API](/methodology/non-parametric-test/Kolmogorov-Smirnov/detecting-fraudulent-transactions/README.md), 357 out of 985 products are found and have 321 different products with the most similar unit price distribution.
