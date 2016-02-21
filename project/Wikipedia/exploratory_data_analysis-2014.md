## Using R and xts

~~~
> library(xts)

> Bitcoin <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Bitcoin-2014-daily.csv", sep=",", header=T))

> dim(Bitcoin)
[1] 364   1

> colnames(Bitcoin) <- c("Volume")

> head(Bitcoin)

           Volume
2014-01-01  39410
2014-01-02  49019
2014-01-03  51499
2014-01-04  41665
2014-01-05   7177
2014-01-06  25219

> plot(x=log(Bitcoin), ylab = "log(Volume)", main = "Bitcoin")
~~~
![Bitcoin_2014](images/Bitcoin_2014.png)


> Cryptocurrency <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency-2014-daily.csv", sep=",", header=T))

> dim(Cryptocurrency)
[1] 364   1

> colnames(Cryptocurrency) <- c("Volume")

> head(Cryptocurrency)

           Volume
2014-01-01   1616
2014-01-02   2394
2014-01-03   2549
2014-01-04   2499
2014-01-05    449
2014-01-06   1055

> plot(x=log(Cryptocurrency), ylab = "log(Volume)", main = "Cryptocurrency")
~~~
![Cryptocurrency_2014](images/Cryptocurrency_2014.png)

