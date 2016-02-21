## Preprocessing


### Filtering in lines with Bitcoin-related titles

~~~
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 1/*.gz > All-201501.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 2/*.gz > All-201502.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 3/*.gz > All-201503.txt
~~~

### Raw data issues

1. pagecounts-20150106-120001.gz
~~~
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" pagecounts-20150106-120000.gz > All-20150106-12.txt

zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" pagecounts-20150106-120001.gz > All-20150106-12-1.txt

diff All-20150106-12.txt All-20150106-12-1.txt

6c6
< commons.m File:Bitcoin_exchange_BTC-e_log_scale.png 1 9747
---
> commons.m File:Bitcoin_exchange_BTC-e_log_scale.png 1 10444
8,9c8,9
< commons.m File:Bitcoin_winkdex.png 1 10194
< cs Bitcoin 9 265341
---
> commons.m File:Bitcoin_winkdex.png 1 10893
> cs Bitcoin 9 266040
12c12
< de Bitcoin 82 6814555
---
> de Bitcoin 78 6818067
14,15c14
< de Diskussion:Bitcoin 16 681187
< el Bitcoin 2 48150
---
> de Diskussion:Bitcoin 16 692341
16a16,17
> el Bitcoin 2 48150
> en.d Bitstamp 2 33726
18c19
< en Bitcoin 309 43069253
---
> en Bitcoin 298 42854167
25c26
< en Bitcoin_network 8 182016
---
> en Bitcoin_network 8 182780
28c29
< en Bitstamp 34 398888
---
> en Bitstamp 34 399558
34c35
< en Block_chain 3 23999
---
> en Block_chain 3 24697
36c37
< en Blockchain.info 11 139821
---
> en Blockchain.info 11 140504
40c41
< en Cryptocurrency 40 1881604
---
> en Cryptocurrency 39 1852339
42c43
< en Digital_currency 11 238653
---
> en Digital_currency 11 239337
44c45
< en File:Bitcoin.svg 1 9814
---
> en File:Bitcoin.svg 1 10515
49c50
< en Legality_of_Bitcoin_by_country 9 219254
---
> en Legality_of_Bitcoin_by_country 9 220016
54c55
< en Talk:Bitcoin 5 557911
---
> en Talk:Bitcoin 5 558609
59d59
< en.d Bitstamp 2 33726
61c61
< fi Bitcoin 6 182190
---
> fi Bitcoin 6 182940
63c63
< fr Bitcoin 23 1059633
---
> fr Bitcoin 23 1060316
75c75
< nl Bitcoin 15 213359
---
> nl Bitcoin 16 228600
77c77
< pl Bitcoin 63 1599969
---
> pl Bitcoin 62 1573740
79a80
> ru.n %d0%94%d0%b2%d0%b5_%d0%ba%d1%80%d1%83%d0%bf%d0%bd%d0%b5%d0%b9%d1%88%d0%b8%d0%b5_%d0%b1%d0%b8%d1%80%d0%b6%d0%b8_Bitcoin_%d1%81%d1%82%d0%b0%d0%bb%d0%b8_%d0%b6%d0%b5%d1%80%d1%82%d0%b2%d0%b0%d0%bc%d0%b8_DDoS-%d0%b0%d1%82%d0%b0%d0%ba 1 19992
81,83c82,83
< ru Bitcoin 29 2980938
< ru Bitcoin_Foundation 2 27052
< ru.n %d0%94%d0%b2%d0%b5_%d0%ba%d1%80%d1%83%d0%bf%d0%bd%d0%b5%d0%b9%d1%88%d0%b8%d0%b5_%d0%b1%d0%b8%d1%80%d0%b6%d0%b8_Bitcoin_%d1%81%d1%82%d0%b0%d0%bb%d0%b8_%d0%b6%d0%b5%d1%80%d1%82%d0%b2%d0%b0%d0%bc%d0%b8_DDoS-%d0%b0%d1%82%d0%b0%d0%ba 1 19293
---
> ru Bitcoin 29 2989334
> ru Bitcoin_Foundation 2 27721
85c85
< sl Bitcoin 17 391254
---
> sl Bitcoin 16 375672
~~~

2. pagecounts-20150226-200000.gz, size 4.0K
3. pagecounts-20150401-010000.gz (missing)
4. pagecounts-201505*.gz contain lines with very long (>= 1024) titles

~~~
# filter out lines with long titles

wc -l All-201505.txt
54732

awk '{ if (length($0) < 1024) print }' All-201505.txt > All-201505-1.txt

wc -l  All-201505-1.txt
54719

awk '{ if (length($0) >= 1024) print }' All-201505.txt > All-201505-2.txt

wc -l All-201505-2.txt
13
~~~


### Using Spark

~~~
bin/spark-shell --master spark://localhost:7077 \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
--executor-cores=2 --num-executors=2


import org.apache.log4j.Logger
import org.apache.log4j.Level
Logger.getLogger("org.apache.spark").setLevel(Level.WARN)

import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel


val grepRDD =  sc.textFile("/work/R/example/Wikipedia/Bitcoin/All-2015*.txt", 4)

grepRDD.cache()

grepRDD.take(10).foreach(println)

1/pagecounts-20150101-000000.gz:ca Bitcoin 1 33665
1/pagecounts-20150101-000000.gz:commons.m Category:Cryptocurrency 2 15241
1/pagecounts-20150101-000000.gz:commons.m File:Bitcoin-coins.jpg 2 16968
1/pagecounts-20150101-000000.gz:commons.m File:Bitcoin_logo.svg 1 10702
1/pagecounts-20150101-000000.gz:commons.m File:Sample_Bitcoin_paper_wallet.png 1 9692
1/pagecounts-20150101-000000.gz:cs Bitcoin 1 0
1/pagecounts-20150101-000000.gz:de Bitcoin 14 1134233
1/pagecounts-20150101-000000.gz:el.b %CE%A4%CE%B1_%CF%80%CF%81%CF%8E%CF%84%CE%B1_%CE%B2%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_%CF%83%CF%84%CE%BF_Bitcoin 1 12482
1/pagecounts-20150101-000000.gz:en BitPay 7 87807
1/pagecounts-20150101-000000.gz:en Bitcoin 188 20961624

grepRDD.count
res6: Long = 703885                                                             

val goodRDD = grepRDD.filter(line => line.split(" ").size == 4)

goodRDD.count
res10: Long = 703878 


val pvRDD = goodRDD.map(line => line.split(".gz:")(1))

pvRDD.take(10).foreach(println)

ca Bitcoin 1 33665
commons.m Category:Cryptocurrency 2 15241
commons.m File:Bitcoin-coins.jpg 2 16968
commons.m File:Bitcoin_logo.svg 1 10702
commons.m File:Sample_Bitcoin_paper_wallet.png 1 9692
cs Bitcoin 1 0
de Bitcoin 14 1134233
el.b %CE%A4%CE%B1_%CF%80%CF%81%CF%8E%CF%84%CE%B1_%CE%B2%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_%CF%83%CF%84%CE%BF_Bitcoin 1 12482
en BitPay 7 87807
en Bitcoin 188 20961624


val pvTupleRDD = goodRDD.map{ line => 
  val a = line.split(".gz:")
  
  val i = a(0).indexOf("-")
  val j = a(0).indexOf("-", i+1)
  
  val a1 = a(1).split(" ")
  
  (a1(0), a1(1), a1(2).toInt, a1(3).toLong, a(0).substring(i+1,j))
}

pvTupleRDD.take(10).foreach(println)

(ca,Bitcoin,1,33665,20150101)
(commons.m,Category:Cryptocurrency,2,15241,20150101)
(commons.m,File:Bitcoin-coins.jpg,2,16968,20150101)
(commons.m,File:Bitcoin_logo.svg,1,10702,20150101)
(commons.m,File:Sample_Bitcoin_paper_wallet.png,1,9692,20150101)
(cs,Bitcoin,1,0,20150101)
(de,Bitcoin,14,1134233,20150101)
(el.b,%CE%A4%CE%B1_%CF%80%CF%81%CF%8E%CF%84%CE%B1_%CE%B2%CE%AE%CE%BC%CE%B1%CF%84%CE%B1_%CF%83%CF%84%CE%BF_Bitcoin,1,12482,20150101)
(en,BitPay,7,87807,20150101)
(en,Bitcoin,188,20961624,20150101)

pvTupleRDD.map(t => (t._2, t._3)).reduceByKey(_+_, 1).sortBy(t => t._2, false).take(50).foreach(println)

(Bitcoin,5906673)                                                               
(Cryptocurrency,309760)
(Block_chain_(database),256258)
(History_of_Bitcoin,134661)
(Digital_currency,90970)
(Block_chain,84307)
(Bitcoin_network,67132)
(Blockchain.info,56625)
(Coinbase,55445)
(Block_chain_(transaction_database),38416)
(Bitcoin_ATM,37064)
(BitPay,31367)
(Legality_of_Bitcoin_by_country,30666)
(Bitcoin_Foundation,29407)
(Bitcoin_protocol,29199)
(Digital_currency_exchanger,26562)
(Bitstamp,26055)
(Bitcoin_mining,22971)
(Bitcoin_faucet,21851)
(Bitcoins,17335)
(Bitcoin_Fog,13537)
(Talk:Bitcoin,12824)
(Category:Bitcoin,12384)
(Cryptocurrency_tumbler,10048)
(File:Bitcoin_logo.svg,9540)
(File:Bitcoin_Transaction_Visual.svg,9513)
(LocalBitcoins,8712)
(File:Bitcoin_October_2013.png,8518)
(File:BitcoinSign.svg,6696)
(Block_chain_%28database%29,6466)
(Category:Cryptocurrency,6164)
(File:Bitcoin_price_and_volatility.svg,5612)
(Category:Bitcoin_exchanges,4918)
(File:Bitcoin-coins.jpg,4836)
(Bitcoin_XT,4618)
(File:Bitcoin.svg,4265)
(File:De_Waag_Bitcoin.jpg,4129)
(Bitcoin_exchange,4049)
(File:Cryptocurrency_Mining_Farm.jpg,3971)
(File:Bitcoin_paper_wallet_generated_at_bitaddress.jpg,3963)
(Bitcoin_Protocol,2827)
(Legal_status_of_Bitcoin,2825)
(File:Electrum_Bitcoin_Wallet.png,2824)
(Legality_of_Bitcoins_by_country,2437)
(File:Bitcoin_Foundation_logo.png,2430)
(Template:Bitcoin,2388)
(File:BitstampUSD_weekly.png,2130)
(List_of_Bitcoin_companies,2036)
(File:Bitcoin_exchange.png,2035)
(Category:People_associated_with_Bitcoin,2004)


val bitcoinRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin")

bitcoinRDD.take(10).foreach(println)

(ca,Bitcoin,1,33665,20150101)
(cs,Bitcoin,1,0,20150101)
(de,Bitcoin,14,1134233,20150101)
(en,Bitcoin,188,20961624,20150101)
(es,Bitcoin,14,648809,20150101)
(et,Bitcoin,1,15424,20150101)
(fi,Bitcoin,1,30670,20150101)
(fr,Bitcoin,7,276072,20150101)
(hu,Bitcoin,1,20909,20150101)
(id,Bitcoin,1,25061,20150101)

bitcoinRDD.map(t => t._3).collect().sum
res22: Int = 5906673

val dailyBitcoinRDD = bitcoinRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinRDD.take(10).foreach(println)

2015-01-07,13514                                                                
2015-02-05,12397
2015-03-17,25360
2015-03-21,10399
2015-09-24,9359
2015-01-30,9520
2015-09-23,41870
2015-06-10,9499
2015-11-27,8738
2015-12-02,10740

dailyBitcoinRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin-2015-daily.csv")


val cryptocurrencyRDD = pvTupleRDD.filter(t => t._2 == "Cryptocurrency")

cryptocurrencyRDD.take(10).foreach(println)

(en,Cryptocurrency,21,979691,20150101)
(en,Cryptocurrency,26,855446,20150101)
(zh-yue,Cryptocurrency,2,21450,20150101)
(en,Cryptocurrency,16,466862,20150101)
(zh-yue,Cryptocurrency,2,21450,20150101)
(en,Cryptocurrency,11,311201,20150101)
(en,Cryptocurrency,12,559320,20150101)
(en,Cryptocurrency,19,621574,20150101)
(en,Cryptocurrency,15,621542,20150101)
(en,Cryptocurrency,22,762087,20150101)

cryptocurrencyRDD.map(t => t._3).collect().sum
res22: Int = 309760

val dailyCryptocurrencyRDD = cryptocurrencyRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyCryptocurrencyRDD.take(10).foreach(println)

2015-02-05,977                                                                  
2015-01-07,1116
2015-03-17,1217
2015-03-21,2554
2015-09-24,792
2015-01-30,842
2015-09-23,738
2015-06-10,758
2015-12-02,846
2015-06-19,563

dailyCryptocurrencyRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency-2015-daily.csv")


val bcRDD = pvTupleRDD.filter(t => t._2 == "Block_chain")

bcRDD.take(10).foreach(println)

(en,Block_chain,2,16010,20150101)
(en,Block_chain,1,8005,20150101)
(en,Block_chain,1,7995,20150101)
(en,Block_chain,1,7995,20150101)
(en,Block_chain,1,7995,20150101)
(en,Block_chain,1,7995,20150101)
(en,Block_chain,1,7995,20150101)
(en,Block_chain,2,7995,20150101)
(en,Block_chain,1,7995,20150101)
(en,Block_chain,1,7995,20150101)

bcRDD.map(t => t._3).collect().sum
res22: Int = 84307

val dailyBcRDD = bcRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBcRDD.take(10).foreach(println)

(2015-01-07,37)                                                                 
(2015-02-05,31)
(2015-09-24,377)
(2015-11-27,350)
(2015-03-17,36)
(2015-01-30,23)
(2015-09-23,526)
(2015-06-10,23)
(2015-12-02,296)
(2015-06-19,14)

dailyBcRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain-2015-daily.csv")


val bcdRDD = pvTupleRDD.filter(t => t._2 == "Block_chain_(transaction_database)" || t._2 == "Block_chain_(database)")

bcdRDD.take(10).foreach(println)

(en,Block_chain_(transaction_database),2,220492,20150101)
(en,Block_chain_(transaction_database),2,219808,20150101)
(en,Block_chain_(transaction_database),5,548254,20150101)
(en,Block_chain_(transaction_database),1,109921,20150101)
(en,Block_chain_(transaction_database),1,109909,20150101)
(en,Block_chain_(transaction_database),2,219302,20150101)
(en,Block_chain_(transaction_database),3,328967,20150101)
(en,Block_chain_(transaction_database),4,438632,20150101)
(en,Block_chain_(transaction_database),5,549384,20150101)
(en,Block_chain_(transaction_database),1,109658,20150101)

bcdRDD.map(t => t._3).collect().sum
res22: Int = 294674

val dailyBcdRDD = bcdRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBcdRDD.take(10).foreach(println)

(2015-01-07,222)                                                                
(2015-02-05,139)
(2015-03-17,256)
(2015-03-21,97)
(2015-09-24,1318)
(2015-01-30,141)
(2015-09-23,1561)
(2015-06-10,737)
(2015-12-02,2072)
(2015-06-19,446)

dailyBcdRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain_database-2015-daily.csv")


val historyOfBitcoinRDD = pvTupleRDD.filter(t => t._2 == "History_of_Bitcoin")

historyOfBitcoinRDD.take(10).foreach(println)

(en,History_of_Bitcoin,14,717774,20150101)
(en,History_of_Bitcoin,6,307578,20150101)
(en,History_of_Bitcoin,2,102526,20150101)
(en,History_of_Bitcoin,6,307578,20150101)
(en,History_of_Bitcoin,7,358841,20150101)
(en,History_of_Bitcoin,5,205052,20150101)
(en,History_of_Bitcoin,9,609178,20150101)
(en,History_of_Bitcoin,66,15924958,20150101)
(en,History_of_Bitcoin,9,410096,20150101)
(en,History_of_Bitcoin,3,102526,20150101)

historyOfBitcoinRDD.map(t => t._3).collect().sum
res22: Int = 134661

val dailyHistoryOfBitcoinRDD = historyOfBitcoinRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyHistoryOfBitcoinRDD.take(10).foreach(println)

2015-01-07,411                                                                  
2015-02-05,350
2015-03-17,485
2015-03-21,978
2015-09-24,240
2015-01-30,313
2015-09-23,371
2015-06-10,245
2015-11-27,225
2015-12-02,346

dailyHistoryOfBitcoinRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/History_of_Bitcoin-2015-daily.csv")


val digitalcurrencyRDD = pvTupleRDD.filter(t => t._2 == "Digital_currency")

digitalcurrencyRDD.take(10).foreach(println)

(en,Digital_currency,6,97855,20150101)
(en,Digital_currency,15,336913,20150101)
(en,Digital_currency,6,117451,20150101)
(en,Digital_currency,7,137027,20150101)
(en,Digital_currency,2,19571,20150101)
(en,Digital_currency,4,58728,20150101)
(en,Digital_currency,12,219466,20150101)
(en,Digital_currency,10,184495,20150101)
(en,Digital_currency,6,160723,20150101)
(en,Digital_currency,3,58720,20150101)

digitalcurrencyRDD.map(t => t._3).collect().sum
res22: Int = 90970

val dailyDigitalcurrencyRDD = digitalcurrencyRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyDigitalcurrencyRDD.take(10).foreach(println)

2015-02-05,302                                                                  
2015-01-07,262
2015-03-17,371
2015-03-21,1011
2015-09-24,205
2015-01-30,243
2015-09-23,224
2015-06-10,254
2015-12-02,272
2015-06-19,162

dailyDigitalcurrencyRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Digital_currency-2015-daily.csv")


val bitcoinNetworkRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_network")

bitcoinNetworkRDD.take(10).foreach(println)

(en,Bitcoin_network,5,115142,20150101)
(en,Bitcoin_network,1,22749,20150101)
(en,Bitcoin_network,4,91002,20150101)
(en,Bitcoin_network,11,227520,20150101)
(en,Bitcoin_network,8,159261,20150101)
(en,Bitcoin_network,3,45504,20150101)
(en,Bitcoin_network,4,68256,20150101)
(en,Bitcoin_network,2,45504,20150101)
(en,Bitcoin_network,6,68256,20150101)
(en,Bitcoin_network,3,135792,20150101)

bitcoinNetworkRDD.map(t => t._3).collect().sum
res22: Int = 84307

val dailyBitcoinNetworkRDD = bitcoinNetworkRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinNetworkRDD.take(10).foreach(println)

2015-02-05,193                                                                  
2015-01-07,188
2015-03-17,352
2015-03-21,966
2015-09-24,143
2015-01-30,133
2015-09-23,137
2015-06-10,171
2015-12-02,115
2015-06-19,114

dailyBitcoinNetworkRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_network-2015-daily.csv")


val blockchainInfoRDD = pvTupleRDD.filter(t => t._2 == "Blockchain.info")

blockchainInfoRDD.take(10).foreach(println)

(en,Blockchain.info,5,106683,20150101)
(en,Blockchain.info,6,76326,20150101)
(en,Blockchain.info,4,91892,20150101)
(zh,Blockchain.info,1,11085,20150101)
(en,Blockchain.info,4,91871,20150101)
(en,Blockchain.info,3,38163,20150101)
(en,Blockchain.info,3,38163,20150101)
(en,Blockchain.info,1,12721,20150101)
(en,Blockchain.info,2,25424,20150101)
(en,Blockchain.info,7,130042,20150101)

blockchainInfoRDD.map(t => t._3).collect().sum
res22: Int = 56625

val dailyBlockchainInfoRDD = blockchainInfoRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBlockchainInfoRDD.take(10).foreach(println)

2015-01-07,163                                                                  
2015-02-05,170
2015-03-17,292
2015-03-21,914
2015-09-24,108
2015-01-30,144
2015-09-23,134
2015-06-10,178
2015-11-27,117
2015-12-02,107

dailyBlockchainInfoRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Blockchain_info-2015-daily.csv")


val coinbaseRDD = pvTupleRDD.filter(t => t._2 == "Coinbase")

coinbaseRDD.take(10).foreach(println)

(en,Coinbase,2,30072,20150101)
(en,Coinbase,1,60582,20150101)
(en,Coinbase,3,30072,20150101)
(en,Coinbase,3,45915,20150101)
(en,Coinbase,3,45109,20150101)
(en,Coinbase,3,90668,20150101)
(en,Coinbase,1,15037,20150101)
(en,Coinbase,2,30070,20150101)
(en,Coinbase,1,15037,20150101)
(en,Coinbase,2,30074,20150101)

coinbaseRDD.map(t => t._3).collect().sum
res22: Int = 55445

val dailyCoinbaseRDD = coinbaseRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyCoinbaseRDD.take(10).foreach(println)

2015-02-05,129                                                                  
2015-01-07,126
2015-03-17,253
2015-03-21,900
2015-09-24,140
2015-01-30,183
2015-09-23,147
2015-06-10,115
2015-12-02,153
2015-06-19,106

dailyCoinbaseRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Coinbase-2015-daily.csv")


/*
val bctdRDD = pvTupleRDD.filter(t => t._2 == "Block_chain_(transaction_database)")

bctdRDD.take(10).foreach(println)

(en,Block_chain_(transaction_database),2,220492,20150101)
(en,Block_chain_(transaction_database),2,219808,20150101)
(en,Block_chain_(transaction_database),5,548254,20150101)
(en,Block_chain_(transaction_database),1,109921,20150101)
(en,Block_chain_(transaction_database),1,109909,20150101)
(en,Block_chain_(transaction_database),2,219302,20150101)
(en,Block_chain_(transaction_database),3,328967,20150101)
(en,Block_chain_(transaction_database),4,438632,20150101)
(en,Block_chain_(transaction_database),5,549384,20150101)
(en,Block_chain_(transaction_database),1,109658,20150101)

bctdRDD.map(t => t._3).collect().sum
res22: Int = 38416

val dailyBctdRDD = bctdRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBctdRDD.take(10).foreach(println)

2015-01-07,222                                                                  
2015-02-05,139
2015-03-17,256
2015-03-21,97
2015-09-24,9
2015-01-30,141
2015-09-23,16
2015-06-10,40
2015-11-27,10
2015-12-02,4

dailyBctdRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain_transaction_database-2015-daily.csv")
*/


val bitcoinATMRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_ATM")

bitcoinATMRDD.take(10).foreach(println)

(en,Bitcoin_ATM,1,13396,20150101)
(en,Bitcoin_ATM,1,13406,20150101)
(en,Bitcoin_ATM,1,13401,20150101)
(en,Bitcoin_ATM,1,13396,20150101)
(en,Bitcoin_ATM,4,40188,20150101)
(en,Bitcoin_ATM,3,40188,20150101)
(en,Bitcoin_ATM,1,13396,20150101)
(en,Bitcoin_ATM,2,26814,20150101)
(en,Bitcoin_ATM,1,13407,20150101)
(en,Bitcoin_ATM,5,144261,20150101)

bitcoinATMRDD.map(t => t._3).collect().sum
res22: Int = 37064

val dailyBitcoinATMRDD = bitcoinATMRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinATMRDD.take(10).foreach(println)

2015-02-05,113                                                                  
2015-01-07,93
2015-03-17,234
2015-03-21,858
2015-09-24,105
2015-01-30,102
2015-09-23,90
2015-06-10,69
2015-12-02,81
2015-06-19,64

dailyBitcoinATMRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_ATM-2015-daily.csv")


val bitPayRDD = pvTupleRDD.filter(t => t._2 == "BitPay")

bitPayRDD.take(10).foreach(println)

(en,BitPay,7,87807,20150101)
(en,BitPay,2,58538,20150101)
(en,BitPay,1,29269,20150101)
(en,BitPay,4,58538,20150101)
(en,BitPay,3,193341,20150101)
(en,BitPay,3,58538,20150101)
(en,BitPay,1,0,20150101)
(en,BitPay,6,58538,20150101)
(en,BitPay,6,87807,20150101)
(en,BitPay,6,0,20150101)

bitPayRDD.map(t => t._3).collect().sum
res22: Int = 31367

val dailyBitPayRDD = bitPayRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitPayRDD.take(10).foreach(println)

2015-02-05,66                                                                   
2015-01-07,188
2015-03-17,213
2015-03-21,860
2015-09-24,75
2015-01-30,51
2015-09-23,54
2015-06-10,66
2015-12-02,79
2015-06-19,97

dailyBitPayRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/BitPay-2015-daily.csv")


val legalityRDD = pvTupleRDD.filter(t => t._2 == "Legality_of_Bitcoins_by_country" || t._2 ==  "Legality_of_Bitcoin_by_country")

legalityRDD.take(10).foreach(println)

(en,Legality_of_Bitcoin_by_country,7,133210,20150101)
(en,Legality_of_Bitcoin_by_country,6,177615,20150101)
(en,Legality_of_Bitcoin_by_country,3,44404,20150101)
(en,Legality_of_Bitcoins_by_country,1,44483,20150101)
(en,Legality_of_Bitcoin_by_country,5,222020,20150101)
(en,Legality_of_Bitcoin_by_country,2,88808,20150101)
(en,Legality_of_Bitcoin_by_country,6,267100,20150101)
(en,Legality_of_Bitcoin_by_country,1,0,20150101)
(en,Legality_of_Bitcoins_by_country,2,88966,20150101)
(en,Legality_of_Bitcoin_by_country,11,88808,20150101)

legalityRDD.map(t => t._3).collect().sum
res22: Int = 33103

val dailyLegalityRDD = legalityRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyLegalityRDD.take(10).foreach(println)

(2015-02-05,277)                                                                
(2015-01-07,343)
(2015-03-17,204)
(2015-03-21,846)
(2015-09-24,26)
(2015-01-30,285)
(2015-09-23,32)
(2015-06-10,19)
(2015-12-02,16)
(2015-06-19,26)

dailyLegalityRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Legality_of_Bitcoin_by_country-2015-daily.csv")


val foundationRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_Foundation")

foundationRDD.take(10).foreach(println)

(en,Bitcoin_Foundation,1,14226,20150101)
(ru,Bitcoin_Foundation,1,13517,20150101)
(en,Bitcoin_Foundation,2,28456,20150101)
(en,Bitcoin_Foundation,1,0,20150101)
(en,Bitcoin_Foundation,2,28460,20150101)
(en,Bitcoin_Foundation,2,28460,20150101)
(en,Bitcoin_Foundation,1,14230,20150101)
(en,Bitcoin_Foundation,2,28460,20150101)
(en,Bitcoin_Foundation,1,14230,20150101)
(en,Bitcoin_Foundation,5,112760,20150101)

foundationRDD.map(t => t._3).collect().sum
res22: Int = 26055

val dailyFoundationRDD = foundationRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyFoundationRDD.take(10).foreach(println)

2015-01-07,140                                                                  
2015-02-05,64
2015-03-17,200
2015-03-21,845
2015-09-24,59
2015-01-30,75
2015-09-23,93
2015-06-10,62
2015-11-27,20
2015-12-02,48

dailyFoundationRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_Foundation-2015-daily.csv")


val protocolRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_protocol")

protocolRDD.take(10).foreach(println)

(en,Bitcoin_protocol,1,23519,20150101)
(en,Bitcoin_protocol,2,22831,20150101)
(en,Bitcoin_protocol,2,45672,20150101)
(en,Bitcoin_protocol,2,45662,20150101)
(en,Bitcoin_protocol,2,45662,20150101)
(en,Bitcoin_protocol,1,22831,20150101)
(en,Bitcoin_protocol,1,22831,20150101)
(en,Bitcoin_protocol,2,45662,20150101)
(en,Bitcoin_protocol,3,136249,20150101)
(en,Bitcoin_protocol,3,136244,20150101)

protocolRDD.map(t => t._3).collect().sum
res22: Int = 26055

val dailyProtocolRDD = protocolRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyProtocolRDD.take(10).foreach(println)

2015-02-05,340                                                                  
2015-01-07,49
2015-03-17,182
2015-03-21,850
2015-09-24,50
2015-01-30,60
2015-09-23,38
2015-06-10,72
2015-12-02,51
2015-06-19,45

dailyProtocolRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_protocol-2015-daily.csv")


val dceRDD = pvTupleRDD.filter(t => t._2 == "Digital_currency_exchanger")

dceRDD.take(10).foreach(println)

(en,Digital_currency_exchanger,4,71565,20150101)
(en,Digital_currency_exchanger,1,17890,20150101)
(en,Digital_currency_exchanger,5,53688,20150101)
(en,Digital_currency_exchanger,4,71569,20150101)
(en,Digital_currency_exchanger,1,17899,20150101)
(en,Digital_currency_exchanger,2,35798,20150101)
(en,Digital_currency_exchanger,1,17890,20150101)
(en,Digital_currency_exchanger,3,35798,20150101)
(en,Digital_currency_exchanger,4,71596,20150101)
(en,Digital_currency_exchanger,2,35798,20150101)

dceRDD.map(t => t._3).collect().sum
res22: Int = 26055

val dailyDceRDD = dceRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyDceRDD.take(10).foreach(println)

2015-01-07,54                                                                   
2015-02-05,67
2015-03-17,184
2015-03-21,841
2015-09-24,49
2015-01-30,47
2015-09-23,44
2015-06-10,44
2015-11-27,45
2015-12-02,35

dailyDceRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Digital_currency_exchanger-2015-daily.csv")


val bitstampRDD = pvTupleRDD.filter(t => t._2 == "Bitstamp")

bitstampRDD.take(10).foreach(println)

(en,Bitstamp,1,11316,20150101)
(en,Bitstamp,3,11316,20150101)
(en,Bitstamp,4,0,20150101)
(en,Bitstamp,1,11316,20150101)
(en,Bitstamp,2,22632,20150101)
(en,Bitstamp,4,22632,20150101)
(en,Bitstamp,4,22632,20150101)
(en,Bitstamp,1,11316,20150101)
(en,Bitstamp,2,11316,20150101)
(en,Bitstamp,2,11316,20150101)

bitstampRDD.map(t => t._3).collect().sum
res22: Int = 26055

val dailyBitstampRDD = bitstampRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitstampRDD.take(10).foreach(println)

2015-01-07,468                                                                  
2015-02-05,69
2015-03-17,192
2015-03-21,831
2015-09-24,41
2015-01-30,71
2015-09-23,48
2015-06-10,36
2015-11-27,16
2015-12-02,47

dailyBitstampRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitstamp-2015-daily.csv")


val miningRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_mining")

miningRDD.take(10).foreach(println)

(en,Bitcoin_mining,1,22850,20150101)
(en,Bitcoin_mining,1,22850,20150101)
(en,Bitcoin_mining,1,22855,20150101)
(en,Bitcoin_mining,1,90636,20150101)
(en,Bitcoin_mining,3,68565,20150101)
(en,Bitcoin_mining,2,113515,20150101)
(en,Bitcoin_mining,4,159225,20150101)
(en,Bitcoin_mining,3,68565,20150101)
(en,Bitcoin_mining,1,22855,20150101)
(en,Bitcoin_mining,1,90660,20150101)

miningRDD.map(t => t._3).collect().sum
res22: Int = 22971

val dailyMiningRDD = miningRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyMiningRDD.take(10).foreach(println)

2015-01-07,60                                                                   
2015-02-05,49
2015-03-17,59
2015-03-21,28
2015-09-24,60
2015-01-30,45
2015-09-23,50
2015-06-10,60
2015-11-27,91
2015-12-02,190

dailyMiningRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_mining-2015-daily.csv")


val faucetRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_faucet")

faucetRDD.take(10).foreach(println)

(en,Bitcoin_faucet,2,19830,20150101)
(en,Bitcoin_faucet,2,9153,20150101)
(en,Bitcoin_faucet,1,9164,20150101)
(en,Bitcoin_faucet,1,9164,20150101)
(en,Bitcoin_faucet,1,30698,20150101)
(en,Bitcoin_faucet,1,9164,20150101)
(en,Bitcoin_faucet,1,9164,20150101)
(en,Bitcoin_faucet,1,9164,20150101)
(en,Bitcoin_faucet,1,30698,20150101)
(en,Bitcoin_faucet,4,40578,20150101)

faucetRDD.map(t => t._3).collect().sum
res22: Int = 21851

val dailyFaucetRDD = faucetRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyFaucetRDD.take(10).foreach(println)

2015-01-07,24                                                                   
2015-02-05,27
2015-03-17,159
2015-03-21,859
2015-09-24,40
2015-01-30,30
2015-09-23,33
2015-06-10,49
2015-11-27,46
2015-12-02,43

dailyFaucetRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_faucet-2015-daily.csv")


val fogRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_Fog")

fogRDD.take(10).foreach(println)

(en,Bitcoin_Fog,1,7511,20150101)
(en,Bitcoin_Fog,2,13692,20150101)
(en,Bitcoin_Fog,1,6850,20150103)
(en,Bitcoin_Fog,1,24268,20150104)
(en,Bitcoin_Fog,1,6850,20150105)
(en,Bitcoin_Fog,1,6886,20150106)
(en,Bitcoin_Fog,1,6854,20150107)
(en,Bitcoin_Fog,1,6855,20150110)
(en,Bitcoin_Fog,1,6847,20150110)
(en,Bitcoin_Fog,1,6852,20150111)

fogRDD.map(t => t._3).collect().sum
res22: Int = 13537

val dailyFogRDD = fogRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyFogRDD.take(10).foreach(println)

2015-01-07,1                                                                    
2015-06-15,88
2015-12-16,53
2015-02-05,1
2015-11-28,67
2015-04-13,5
2015-09-24,51
2015-11-27,87
2015-02-11,4
2015-01-30,1

dailyFogRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_Fog-2015-daily.csv")


val cctRDD = pvTupleRDD.filter(t => t._2 == "Cryptocurrency_tumbler")

cctRDD.take(10).foreach(println)

(en,Cryptocurrency_tumbler,23,377922,20150517)
(en,Cryptocurrency_tumbler,77,1484420,20150517)
(en,Cryptocurrency_tumbler,34,889496,20150517)
(en,Cryptocurrency_tumbler,8,191620,20150517)
(en,Cryptocurrency_tumbler,6,202801,20150517)
(en,Cryptocurrency_tumbler,1,11331,20150517)
(en,Cryptocurrency_tumbler,1,11331,20150517)
(en,Cryptocurrency_tumbler,1,42263,20150518)
(en,Cryptocurrency_tumbler,1,11331,20150518)
(en,Cryptocurrency_tumbler,2,84526,20150518)

cctRDD.map(t => t._3).collect().sum
res22: Int = 10048

val dailyCctRDD = cctRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyCctRDD.take(10).foreach(println)

2015-06-15,48                                                                   
2015-11-28,46
2015-09-24,36
2015-11-27,30
2015-09-23,58
2015-06-10,36
2015-11-15,32
2015-06-25,42
2015-12-02,51
2015-06-21,19

dailyCctRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency_tumbler-2015-daily.csv")


val legalStatusRDD = pvTupleRDD.filter(t => t._2 == "Legal_status_of_Bitcoin")

legalStatusRDD.take(10).foreach(println)

(en,Legal_status_of_Bitcoin,1,44490,20150101)
(en,Legal_status_of_Bitcoin,1,44481,20150101)
(en,Legal_status_of_Bitcoin,3,134149,20150101)
(en,Legal_status_of_Bitcoin,1,44481,20150102)
(en,Legal_status_of_Bitcoin,1,216259,20150102)
(en,Legal_status_of_Bitcoin,1,44484,20150102)
(en,Legal_status_of_Bitcoin,1,44484,20150102)
(en,Legal_status_of_Bitcoin,1,44481,20150103)
(en,Legal_status_of_Bitcoin,2,88962,20150103)
(en,Legal_status_of_Bitcoin,1,44480,20150104)

legalStatusRDD.map(t => t._3).collect().sum
res78: Int = 2825                                                              

val dailyLegalStatusRDD = legalStatusRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyLegalStatusRDD.take(10).foreach(println)

(2015-02-05,4)                                                                  
(2015-01-07,3)
(2015-12-16,5)
(2015-06-15,2)
(2015-11-28,2)
(2015-04-13,4)
(2015-02-11,3)
(2015-03-17,11)
(2015-03-21,6)
(2015-01-30,5)

dailyLegalStatusRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Legal_status_of_Bitcoin-2015-daily.csv")
~~~


### Raw gzip files

~~~
val rawRDD =  sc.textFile("/work/R/example/Wikipedia/pagecounts*.gz")

rawRDD.cache()

rawRDD.take(10).foreach(println)

aa %22/ar/1541%22 1 4643
aa %C4%BDudov%C3%ADt_XV 1 4658
aa %D0%86%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%B0_%D0%BA%D0%B2%D0%BE%D1%82%D0%B0 1 4733
aa %D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9A_%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E/%22/ru/%D0%9D%D0%BE%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B9,_%D0%A0%D0%B5%D0%BD%D0%B5%22 1 4946
aa %D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9A_%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E/%22/ru/%D0%9F%D1%80%D0%B8%D0%B4%D0%BD%D0%B5%D1%81%D1%82%D1%80%D0%BE%D0%B2%D1%8C%D0%B5%22 1 4925
aa Arms_of_Ireland 1 4633
aa Henri_de_La_Tour_d%27Auvergne_(1555-1623)/fr/Henri_de_La_Tour_d%27Auvergne,_duc_de_Bouillon 1 4782
aa Indonesian_Wikipedia 1 4627
aa Kategori:308_f.Kr 1 4644
aa L%27Odyss%C3%A9e_(s%C3%A9rie_t%C3%A9l%C3%A9vis%C3%A9e_d%27animation)/fr/L%27Odyss%C3%A9e_(M6) 1 4786

rawRDD.count()
res5: Long = 19908646 


val goodRDD = rawRDD.map(line => line.split(" ")).filter(_.size == 4)

goodRDD.count()
res6: Long = 19908646

// val bitcoinRDD = rawRDD.map(line => line.split(" ")).filter(_.size == 4).filter(a => a(1).contains("Bitcoin"))
val bitcoinRDD = rawRDD.filter(line => line.contains("Bitcoin"))

bitcoinRDD.count()
res7: Long = 190  
~~~
