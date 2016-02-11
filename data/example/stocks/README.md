# Trading S&P 500 market index


## Goal

We will address the task of building a stock trading system based on prediction models obtained with daily stock quotes data. 
Several models will be tried with the goal of predicting the future returns of the S&P 500 market index. These predictions will 
be used together with a trading strategy to reach a decision regarding the market orders to generate.


## Data Source

~~~
> install.packages('tseries')

> library('tseries')

> library(xts)

> GSPC <- as.xts(get.hist.quote("^GSPC",start="1970-01-01",quote=c("Open", "High", "Low", "Close","Volume","AdjClose")))
~~~


## Reference

(1) [Data Mining with R] (http://www.amazon.com/Data-Mining-Learning-Knowledge-Discovery/dp/1439810184)
