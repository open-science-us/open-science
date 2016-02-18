### Feature Filtering with Random Forest
~~~
> library(xts)

> Coinbase <- as.xts(read.zoo("/work/R/example/stocks/coinbase-daily.csv", sep=",", header=T))


> avgPrice <- function(p) apply(p[,c("High","Low","Close")], 1, mean)

> library(quantmod)

> fivenum(as.numeric(abs(Next(Delt(Coinbase["2014-12-01/2016-01-10","Close"], Coinbase["2014-12-01/2016-01-10","Close"], k = 1)))))
[1] 0.000000000 0.005372185 0.012660642 0.027697463 0.701833333

> margin <- 0.012660642 / 0.005175095 * 0.025
> margin
[1] 0.0611614


T.ind <- function(quotes, tgt.margin = 0.025, n.days = 10) {
  v <- avgPrice(quotes)
  r <- matrix(NA, ncol = n.days, nrow = NROW(quotes))
  for (x in 1:n.days) r[, x] <- Next(Delt(v, quotes[, "Close"], k = x), x)
  x <- apply(r, 1, function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x, time(quotes))
  else x
}

> library(randomForest)

> model <- specifyModel(T.ind(Coinbase,tgt.margin=0.06) ~ Delt(myCl(Coinbase),k=1:10) + myATR(Coinbase) + mySMI(Coinbase) + 
  myADX(Coinbase) + myAroon(Coinbase) + myBB(Coinbase) + myChaikinVol(Coinbase) + myCLV(Coinbase) + CMO(myCl(Coinbase)) +
  EMA(Delt(myCl(Coinbase))) + myEMV(Coinbase) + myVolat(Coinbase) + myMACD(Coinbase) + myMFI(Coinbase) + 
  RSI(myCl(Coinbase)) + mySAR(Coinbase) + runMean(myCl(Coinbase)) + runSD(myCl(Coinbase)))
 
> set.seed(1234)

> rf <- buildModel(model, method='randomForest', training.per=c('2014-12-01','2016-01-10'), ntree=50, importance=T)

imp <- importance(rf@fitted.model, type = 1)
df <- data.frame(as.numeric(imp))
df$feature <- rownames(imp)
colnames(df) <- c("importance", "feature")

> df[order(df$importance, decreasing=T)[1:10],c("feature","importance")]

                                       feature importance
12                              mySMI.Coinbase   9.199754
11                              myATR.Coinbase   8.157638
25                              mySAR.Coinbase   7.077558
13                              myADX.Coinbase   6.591131
22                             myMACD.Coinbase   5.731505
21                            myVolat.Coinbase   4.944127
27                         runSD.myCl.Coinbase   4.816010
26                       runMean.myCl.Coinbase   4.610843
20                              myEMV.Coinbase   4.482471
9  Delt.myCl.Coinbase.k.1.10.Delt.9.arithmetic   4.465162

> varImpPlot(rf@fitted.model, type = 1)
~~~
![Coinbase_rf](../images/Coinbase_rf.png)
