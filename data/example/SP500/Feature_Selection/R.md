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
 
myMACD <- function(x) MACD(Cl(x))[, 2]
 
myMFI <- function(x) MFI(x[,c("High","Low","Close")],x[,"Volume"])
 
mySAR <- function(x) SAR(x[,c("High","Close")])[, 1]
 

~~~
