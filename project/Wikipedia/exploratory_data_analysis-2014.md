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


> History_of_Bitcoin <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/History_of_Bitcoin-2014-daily.csv", sep=",", header=T))

> dim(History_of_Bitcoin)
[1] 364   1

> colnames(History_of_Bitcoin) <- c("Volume")

> head(History_of_Bitcoin)

           Volume
2014-01-01    483
2014-01-02    548
2014-01-03    555
2014-01-04    526
2014-01-05    105
2014-01-06    333

> plot(x=log(History_of_Bitcoin), ylab = "log(Volume)", main = "History_of_Bitcoin")
~~~
![History_of_Bitcoin_2014](images/History_of_Bitcoin_2014.png)


> Digital_currency <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Digital_currency-2014-daily.csv", sep=",", header=T))

> dim(Digital_currency)
[1] 364   1

> colnames(Digital_currency) <- c("Volume")

> head(Digital_currency)

           Volume
2014-01-01    518
2014-01-02    643
2014-01-03    643
2014-01-04    732
2014-01-05    107
2014-01-06    340

> plot(x=log(Digital_currency), ylab = "log(Volume)", main = "Digital_currency")
~~~
![Digital_currency_2014](images/Digital_currency_2014.png)


> Bitcoin_protocol <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Bitcoin_protocol-2014-daily.csv", sep=",", header=T))

> dim(Bitcoin_protocol)
[1] 364   1

> colnames(Bitcoin_protocol) <- c("Volume")

> head(Bitcoin_protocol)

           Volume
2014-01-01    774
2014-01-02   1279
2014-01-03   1471
2014-01-04   1153
2014-01-05    259
2014-01-06    808

> plot(x=log(Bitcoin_protocol), ylab = "log(Volume)", main = "Bitcoin_protocol")
~~~
![Bitcoin_protocol_2014](images/Bitcoin_protocol_2014.png)

