## Using R and xts

~~~
> library(xts)

> Bitcoin <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Bitcoin-2015-daily.csv", sep=",", header=T))

> dim(Bitcoin)
[1] 365   1

> colnames(Bitcoin) <- c("Volume")

> head(Bitcoin)

           Volume
2015-01-01   7238
2015-01-02  10130
2015-01-03   9417
2015-01-04   9552
2015-01-05  12212
2015-01-06  16097

> plot(x=log(Bitcoin), ylab = "log(Volume)", main = "Bitcoin")
~~~
![Bitcoin_2015](images/Bitcoin_2015.png)

~~~
> Cryptocurrency <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency-2015-daily.csv", sep=",", header=T))

> dim(Cryptocurrency)
[1] 364   1

> colnames(Cryptocurrency) <- c("Volume")

> head(Cryptocurrency)

           Volume
2015-01-01    570
2015-01-02    796
2015-01-03    706
2015-01-04    744
2015-01-05   1000
2015-01-06   1090

> plot(x=log(Cryptocurrency), ylab = "log(Volume)", main = "Cryptocurrency")
~~~
![Cryptocurrency_2015](images/Cryptocurrency_2015.png)

~~~
> BlockchainDB <- as.xts(read.zoo("/work/R/example/Wikipedia/Bitcoin/Block_chain_database-2015-daily.csv", sep=",", header=T))

> dim(BlockchainDB)
[1] 215   1

> colnames(BlockchainDB) <- c("Volume")

> head(BlockchainDB)

           Volume
2015-05-30     24
2015-05-31     32
2015-06-01     67
2015-06-02     74
2015-06-03     89
2015-06-04    404

> plot(x=BlockchainDB, ylab = "Volume", main = "Block_chain_(database)")
~~~
![Blockchain_database_2015](images/Blockchain_database_2015.png)

