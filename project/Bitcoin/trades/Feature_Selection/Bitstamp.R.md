### Feature Filtering with Random Forest
~~~
> library(xts)

> Bitstamp <- as.xts(read.zoo("/work/R/example/stocks/bitstamp-daily.csv", sep=",", header=T))


> avgPrice <- function(p) apply(p[,c("High","Low","Close")], 1, mean)

> library(quantmod)

> fivenum(as.numeric(abs(Next(Delt(Bitstamp["2011-09-13/2016-01-10","Close"], Bitstamp["2011-09-13/2016-01-10","Close"], k = 1)))))
[1] 0.00000000 0.00667796 0.01643532 0.03659026 0.56133829

T.ind <- function(quotes, tgt.margin = 0.075, n.days = 10) {
  v <- avgPrice(quotes)
  r <- matrix(NA, ncol = n.days, nrow = NROW(quotes))
  for (x in 1:n.days) r[, x] <- Next(Delt(v, quotes[, "Close"], k = x), x)
  x <- apply(r, 1, function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x, time(quotes))
  else x
}


> library(randomForest)

> model <- specifyModel(T.ind(Bitstamp) ~ Delt(myCl(Bitstamp),k=1:10) + myATR(Bitstamp) + mySMI(Bitstamp) + myADX(Bitstamp) + myAroon(Bitstamp) +
  myBB(Bitstamp) + myChaikinVol(Bitstamp) + myCLV(Bitstamp) + CMO(myCl(Bitstamp)) + EMA(Delt(myCl(Bitstamp))) + myEMV(Bitstamp) +
  myVolat(Bitstamp) + myMACD(Bitstamp) + myMFI(Bitstamp) + RSI(myCl(Bitstamp)) + mySAR(Bitstamp) + runMean(myCl(Bitstamp)) + runSD(myCl(Bitstamp)))
 
> set.seed(1234)

> rf <- buildModel(model, method='randomForest', training.per=c('2011-09-13','2016-01-10'), ntree=50, importance=T)

imp <- importance(rf@fitted.model, type = 1)
df <- data.frame(as.numeric(imp))
df$feature <- rownames(imp)
colnames(df) <- c("importance", "feature")

> df[order(df$importance, decreasing=T)[1:10],c("feature","importance")]

                                        feature importance
12                               mySMI.Bitstamp  12.741066
22                              myMACD.Bitstamp   8.896588
11                               myATR.Bitstamp   8.750648
21                             myVolat.Bitstamp   8.246261
13                               myADX.Bitstamp   8.230835
25                               mySAR.Bitstamp   7.811697
26                        runMean.myCl.Bitstamp   7.255525
27                          runSD.myCl.Bitstamp   6.470454
10 Delt.myCl.Bitstamp.k.1.10.Delt.10.arithmetic   6.208686
24                            RSI.myCl.Bitstamp   6.115769

> varImpPlot(rf@fitted.model, type = 1)
~~~
![Bitstamp_rf](../images/Bitstamp_rf.png)


~~~
> rf1 <- buildModel(model, method='randomForest', training.per=c('2011-09-13','2013-04-09'), ntree=50, importance=T)

imp1 <- importance(rf1@fitted.model, type = 1)
df1 <- data.frame(as.numeric(imp1))
df1$feature <- rownames(imp1)
colnames(df1) <- c("importance", "feature")

> df1[order(df1$importance, decreasing=T)[1:10],c("feature","importance")]

                                       feature importance
26                       runMean.myCl.Bitstamp   7.088991
12                              mySMI.Bitstamp   7.009172
22                             myMACD.Bitstamp   6.651529
13                              myADX.Bitstamp   6.283130
9  Delt.myCl.Bitstamp.k.1.10.Delt.9.arithmetic   5.437152
23                              myMFI.Bitstamp   5.406718
21                            myVolat.Bitstamp   5.379585
25                              mySAR.Bitstamp   5.296223
20                              myEMV.Bitstamp   5.106721
24                           RSI.myCl.Bitstamp   4.817042

> varImpPlot(rf1@fitted.model, type = 1)
~~~
![Bitstamp_rf1](../images/Bitstamp_rf1.png)


~~~
> rf2 <- buildModel(model, method='randomForest', training.per=c('2013-04-10','2013-12-04'), ntree=50, importance=T)

imp2 <- importance(rf2@fitted.model, type = 1)
df2 <- data.frame(as.numeric(imp2))
df2$feature <- rownames(imp2)
colnames(df2) <- c("importance", "feature")

> df2[order(df2$importance, decreasing=T)[1:10],c("feature","importance")]

                                       feature importance
12                              mySMI.Bitstamp   5.502996
25                              mySAR.Bitstamp   5.360556
22                             myMACD.Bitstamp   5.088045
26                       runMean.myCl.Bitstamp   4.946642
13                              myADX.Bitstamp   4.827640
20                              myEMV.Bitstamp   4.434969
11                              myATR.Bitstamp   4.012820
14                            myAroon.Bitstamp   3.863205
17                              myCLV.Bitstamp   3.466611
9  Delt.myCl.Bitstamp.k.1.10.Delt.9.arithmetic   3.418760

> varImpPlot(rf2@fitted.model, type = 1)
~~~
![Bitstamp_rf2](../images/Bitstamp_rf2.png)


~~~
> rf3 <- buildModel(model, method='randomForest', training.per=c('2013-12-05','2014-12-31'), ntree=50, importance=T)

imp3 <- importance(rf3@fitted.model, type = 1)
df3 <- data.frame(as.numeric(imp3))
df3$feature <- rownames(imp3)
colnames(df3) <- c("importance", "feature")

> df3[order(df3$importance, decreasing=T)[1:10],c("feature","importance")]

                                        feature importance
22                              myMACD.Bitstamp   9.898029
11                               myATR.Bitstamp   8.119821
25                               mySAR.Bitstamp   6.889789
21                             myVolat.Bitstamp   6.882294
13                               myADX.Bitstamp   6.344567
26                        runMean.myCl.Bitstamp   5.282253
9   Delt.myCl.Bitstamp.k.1.10.Delt.9.arithmetic   4.314561
10 Delt.myCl.Bitstamp.k.1.10.Delt.10.arithmetic   4.114592
18                            CMO.myCl.Bitstamp   4.075093
24                            RSI.myCl.Bitstamp   4.003254

> varImpPlot(rf3@fitted.model, type = 1)
~~~
![Bitstamp_rf3](../images/Bitstamp_rf3.png)


~~~
> rf4 <- buildModel(model, method='randomForest', training.per=c('2015-01-01','2016-01-10'), ntree=50, importance=T)

imp4 <- importance(rf4@fitted.model, type = 1)
df4 <- data.frame(as.numeric(imp4))
df4$feature <- rownames(imp4)
colnames(df4) <- c("importance", "feature")

> df4[order(df4$importance, decreasing=T)[1:10],c("feature","importance")]

                                        feature importance
12                               mySMI.Bitstamp   9.625574
26                        runMean.myCl.Bitstamp   8.263062
25                               mySAR.Bitstamp   6.141645
21                             myVolat.Bitstamp   5.876912
11                               myATR.Bitstamp   5.698511
10 Delt.myCl.Bitstamp.k.1.10.Delt.10.arithmetic   5.368802
13                               myADX.Bitstamp   5.147859
22                              myMACD.Bitstamp   5.079470
23                               myMFI.Bitstamp   4.495699
18                            CMO.myCl.Bitstamp   3.735109

> varImpPlot(rf4@fitted.model, type = 1)
~~~
![Bitstamp_rf4](../images/Bitstamp_rf4.png)
