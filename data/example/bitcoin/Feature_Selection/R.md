### Using TTR package
~~~
> library(TTR)

myATR <- function(x) ATR(x[,c("High","Low","Close")])[, "atr"]
 
mySMI <- function(x) SMI(x[,c("High","Low","Close")])[, "SMI"]
 
myADX <- function(x) ADX(x[,c("High","Low","Close")])[, "ADX"]
 
myAroon <- function(x) aroon(x[,c("High","Low")])$oscillator
 
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

> model <- specifyModel(T.ind2(Bitstamp) ~ Delt(myCl(Bitstamp),k=1:10) + myATR(Bitstamp) + mySMI(Bitstamp) + myADX(Bitstamp) + myAroon(Bitstamp) +
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
26                        runMean.myCl.Bitstamp  11.522012
11                               myATR.Bitstamp  10.822567
12                               mySMI.Bitstamp  10.711132
22                              myMACD.Bitstamp   9.353580
13                               myADX.Bitstamp   8.261817
25                               mySAR.Bitstamp   7.710538
24                            RSI.myCl.Bitstamp   7.155755
21                             myVolat.Bitstamp   6.950403
10 Delt.myCl.Bitstamp.k.1.10.Delt.10.arithmetic   6.275777
9   Delt.myCl.Bitstamp.k.1.10.Delt.9.arithmetic   6.262225

> varImpPlot(rf@fitted.model, type = 1)
~~~
![Bitstamp_rf](../images/Bitstamp_rf.png)
