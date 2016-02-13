### Using TTR package
~~~
> library(TTR)

myATR <- function(x) ATR(x[,c("High","Low","Close")])[, "atr"]
 
mySMI <- function(x) SMI(x[,c("High","Low","Close")])[, "SMI"]
 
myADX <- function(x) ADX(x[,c("High","Low","Close")])[, "ADX"]
 
myAroon <- function(x) aroon(x[,c("High", "Low")])$oscillator
 
myBB <- function(x) BBands(x[,c("High","Low","Close")])[, "pctB"]
 
myChaikinVol <- function(x) Delt(chaikinVolatility(x[,c("High","Low")]))[, 1]

myCLV <- function(x) EMA(CLV(x[,c("High","Low","Close")]))[, 1]
 
myEMV <- function(x) EMV(x[,c("High","Low")],x[,"Volume"])[, 2]
 
myMACD <- function(x) MACD(x[,c("Close")])[, 2]
 
myMFI <- function(x) MFI(x[,c("High","Low","Close")],x[,"Volume"])
 
mySAR <- function(x) SAR(x[,c("High","Close")])[, 1]
 
myVolat <- function(x) volatility(x[,c("Open","High","Low","Close")], calc = "garman")[, 1]

myCl <- function(x) x[,c("Close")]
~~~

### Feature Filtering with Random Forest
~~~
> library(randomForest)

> model <- specifyModel(T.ind2(GSPC) ~ Delt(myCl(GSPC),k=1:10) + myATR(GSPC) + mySMI(GSPC) + myADX(GSPC) + myAroon(GSPC) +
  myBB(GSPC) + myChaikinVol(GSPC) + myCLV(GSPC) + CMO(myCl(GSPC)) + EMA(Delt(myCl(GSPC))) + myEMV(GSPC) +
  myVolat(GSPC) + myMACD(GSPC) + myMFI(GSPC) + RSI(myCl(GSPC)) + mySAR(GSPC) + runMean(myCl(GSPC)) + runSD(myCl(GSPC)))
 
> set.seed(1234)

> rf70_94 <- buildModel(model, method='randomForest', training.per=c('1970-01-01','1994-12-31'), ntree=50, importance=T)

> imp70_94 <- importance(rf70_94@fitted.model, type = 1)
> df70_94 <- data.frame(as.numeric(imp70_94))
> df70_94$feature <- rownames(imp70_94)
> colnames(df70_94) <- c("importance", "feature")

> df70_94[order(df70_94$importance, decreasing=T)[1:10],c("feature","importance")]

                                    feature importance
21                             myVolat.GSPC  15.701049
22                              myMACD.GSPC  12.087076
20                               myEMV.GSPC  11.227810
26                        runMean.myCl.GSPC  10.160595
11                               myATR.GSPC  10.074549
12                               mySMI.GSPC   9.890472
10 Delt.myCl.GSPC.k.1.10.Delt.10.arithmetic   9.665874
1   Delt.myCl.GSPC.k.1.10.Delt.1.arithmetic   9.550633
13                               myADX.GSPC   8.829990
23                               myMFI.GSPC   8.829491

> varImpPlot(rf70_94@fitted.model, type = 1)
~~~
![rf70_94](../images/rf70_94.png)

~~~
> rf95_04 <- buildModel(model, method='randomForest', training.per=c('1995-01-01','2004-12-31'), ntree=50, importance=T)

> imp95_04 <- importance(rf95_04@fitted.model, type = 1)
> df95_04 <- data.frame(as.numeric(imp95_04))
> df95_04$feature <- rownames(imp95_04)
> colnames(df95_04) <- c("importance", "feature")

> df95_04[order(df95_04$importance, decreasing=T)[1:10],c("feature","importance")]

             feature importance
22       myMACD.GSPC  12.892665
21      myVolat.GSPC  12.602926
26 runMean.myCl.GSPC  12.581297
11        myATR.GSPC  12.190333
25        mySAR.GSPC  10.727503
13        myADX.GSPC   8.630410
20        myEMV.GSPC   8.488823
12        mySMI.GSPC   8.485702
27   runSD.myCl.GSPC   8.172743
14      myAroon.GSPC   8.092307

> varImpPlot(rf95_04@fitted.model, type = 1)
~~~
![rf95_04](../images/rf95_04.png)