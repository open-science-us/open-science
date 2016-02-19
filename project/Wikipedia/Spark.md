## Using Spark

### Preprocessing on a Mac laptop
~~~
bin/spark-shell --master spark://localhost:7077 \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
--executor-cores=2 --num-executors=2


import org.apache.log4j.Logger
import org.apache.log4j.Level
Logger.getLogger("org.apache.spark").setLevel(Level.WARN)

import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel


val grepRDD =  sc.textFile("/work/R/example/Wikipedia/Bitcoin/All-*.txt", 4)

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

pvTupleRDD.map(t => (t._2, t._3)).reduceByKey(_+_, 1).sortBy(t => t._2, false).take(30).foreach(println)

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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBitcoinRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyCryptocurrencyRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency-2015-daily.csv")


val bcdRDD = pvTupleRDD.filter(t => t._2 == "Block_chain_(database)")

bcdRDD.take(10).foreach(println)

(en,Block_chain_(database),10,179444,20150530)                                  
(en,Block_chain_(database),2,56502,20150530)
(en,Block_chain_(database),1,0,20150530)
(en,Block_chain_(database),1,11072,20150530)
(en,Block_chain_(database),1,11072,20150530)
(en,Block_chain_(database),2,22144,20150530)
(en,Block_chain_(database),1,11072,20150530)
(en,Block_chain_(database),3,34957,20150530)
(en,Block_chain_(database),3,34180,20150530)
(en,Block_chain_(database),1,11080,20150531)

bcdRDD.map(t => t._3).collect().sum
res22: Int = 256258

val dailyBcdRDD = bcdRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
}

dailyBcdRDD.take(10).foreach(println)

2015-06-15,402                                                                  
2015-11-28,783
2015-09-24,1309
2015-11-27,1533
2015-09-23,1545
2015-06-10,697
2015-11-15,850
2015-06-25,485
2015-12-02,2068
2015-06-21,194

dailyBcdRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain_database-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyHistoryOfBitcoinRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/History_of_Bitcoin-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyDigitalcurrencyRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Digital_currency-2015-daily.csv")


val blockchainRDD = pvTupleRDD.filter(t => t._2 == "Block_chain")

blockchainRDD.take(10).foreach(println)

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

blockchainRDD.map(t => t._3).collect().sum
res22: Int = 84307

val dailyBlockchainRDD = blockchainRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
}

dailyBlockchainRDD.take(10).foreach(println)

2015-01-07,37                                                                   
2015-02-05,31
2015-03-17,36
2015-03-21,24
2015-09-24,377
2015-01-30,23
2015-09-23,526
2015-06-10,23
2015-11-27,350
2015-12-02,296

dailyBlockchainRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBitcoinNetworkRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_network-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBlockchainInfoRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Blockchain_info-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyCoinbaseRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Coinbase-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBctdRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain_transaction_database-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBitcoinATMRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_ATM-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBitPayRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/BitPay-2015-daily.csv")


val legalityRDD = pvTupleRDD.filter(t => t._2 == "Legality_of_Bitcoin_by_country")

legalityRDD.take(10).foreach(println)

(en,Legality_of_Bitcoin_by_country,7,133210,20150101)
(en,Legality_of_Bitcoin_by_country,6,177615,20150101)
(en,Legality_of_Bitcoin_by_country,3,44404,20150101)
(en,Legality_of_Bitcoin_by_country,5,222020,20150101)
(en,Legality_of_Bitcoin_by_country,2,88808,20150101)
(en,Legality_of_Bitcoin_by_country,6,267100,20150101)
(en,Legality_of_Bitcoin_by_country,1,0,20150101)
(en,Legality_of_Bitcoin_by_country,11,88808,20150101)
(en,Legality_of_Bitcoin_by_country,4,88808,20150101)
(en,Legality_of_Bitcoin_by_country,5,222027,20150101)

legalityRDD.map(t => t._3).collect().sum
res22: Int = 31367

val dailyLegalityRDD = legalityRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
}

dailyLegalityRDD.take(10).foreach(println)

2015-01-07,335                                                                  
2015-02-05,271
2015-03-17,191
2015-03-21,837
2015-09-24,24
2015-01-30,277
2015-09-23,30
2015-06-10,16
2015-11-27,4
2015-12-02,7

dailyLegalityRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Legality_of_Bitcoin_by_country-2015-daily.csv")


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
  x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6) + "," + x._2
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

dailyBitstampRDD.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitstamp-2015-daily.csv")
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
