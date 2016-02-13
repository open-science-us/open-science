### Feature List

1. ATR, Average True Range, which is an indicator of the volatility of the series;

2. SMI, Stochastic Momentum Index, which is a momentum indicator; 

3. ADX, Welles Wilder's Directional Movement Index; 

4. Arron, the indicator that tries to identify starting trends; 

5. BB, Bollinger Bands, that compare the volatility over a period of time; 

6. Chaikin Volatility; 

7. CLV, Close Location Value, that relates the session Close to its trading range; 

8. EMV, Arms' Ease of Movement Value (EMV); 

9. the MACD oscillator; 

10. MFI, Money Flow Index (MFI);

11. Parabolic Stop-and-Reverse; 

12. the Volatility indicator.


### Using R
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


> library(randomForest)

> model <- specifyModel(T.ind2(GSPC) ~ Delt(myCl(GSPC),k=1:10) + myATR(GSPC) + mySMI(GSPC) + myADX(GSPC) + myAroon(GSPC) +
  myBB(GSPC) + myChaikinVol(GSPC) + myCLV(GSPC) + CMO(myCl(GSPC)) + EMA(Delt(myCl(GSPC))) + myEMV(GSPC) +
  myVolat(GSPC) + myMACD(GSPC) + myMFI(GSPC) + RSI(myCl(GSPC)) + mySAR(GSPC) + runMean(myCl(GSPC)) + runSD(myCl(GSPC)))
 
> set.seed(1234)

> rf <- buildModel(model, method='randomForest',training.per=c(start(GSPC),index(GSPC["1999-12-31"])),ntree=50, importance=T)

> varImpPlot(rf@fitted.model, type = 1)

> imp <- importance(rf@fitted.model, type = 1)

> imp[order(imp, decreasing=TRUE)[1:10],]

 myADX.GSPC                   myMACD.GSPC                   myATR.GSPC 
 12.165387                    11.979254                     11.326473
 
 myVolat.GSPC                 runMean.myCl.GSPC             myMFI.GSPC 
 10.852970                    10.539441                     10.361515 
 
 runSD.myCl.GSPC              myEMV.GSPC                    Delt.myCl.GSPC.k.1.10.Delt.3.arithmetic
 9.768877                     9.467952                      8.960619 
 
 mySMI.GSPC 
 8.709901 

> names(imp[order(imp, decreasing=TRUE)[1:10],])

 [1] "myADX.GSPC"  "myMACD.GSPC"  "myATR.GSPC"                             
 [4] "myVolat.GSPC"  "runMean.myCl.GSPC"  "myMFI.GSPC"                             
 [7] "runSD.myCl.GSPC"  "myEMV.GSPC"  "Delt.myCl.GSPC.k.1.10.Delt.3.arithmetic"
[10] "mySMI.GSPC"                             
~~~
