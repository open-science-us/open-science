## [Local Outlier Factor](https://en.wikipedia.org/wiki/Local_outlier_factor)

### Ranking
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


> lofs[is.nan(lofs)] <- 1


> lof1 <- lof(prodGroup[['p1']], 3)

> lof1[is.nan(lof1)] <- 1

> lof1[is.infinite(lof1)] <- 100

> cl <- cbind(prodGroup[['p1']], lof1)
~~~








