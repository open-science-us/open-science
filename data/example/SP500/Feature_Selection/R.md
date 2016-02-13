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

> imp70_94 <- importance(rf@fitted.model, type = 1)
> df70_94 <- data.frame(as.numeric(imp70_94))
> df70_94$feature <- rownames(imp70_94)
> colnames(df70_94) <- c("importance", "feature")

> df70_94[order(df70_94 $importance, decreasing=T)[1:10],c("feature","importance")]

             feature importance
26 runMean.myCl.GSPC  13.903021
11        myATR.GSPC  12.738431
25        mySAR.GSPC  11.303793
21      myVolat.GSPC  11.059647
13        myADX.GSPC  10.673914
22       myMACD.GSPC  10.230337
12        mySMI.GSPC   9.271612
27   runSD.myCl.GSPC   8.938491
23        myMFI.GSPC   8.323043
14      myAroon.GSPC   7.353545

> varImpPlot(rf70_94@fitted.model, type = 1)
~~~
![rf70_94](../images/rf70_94.png)
