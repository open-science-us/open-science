## Preprocessing


### Filtering in lines with Bitcoin-related titles

~~~
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 1/*.gz > All-201401.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 2/*.gz > All-201402.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 3/*.gz > All-201403.txt
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


val grepRDD =  sc.textFile("/work/R/example/Wikipedia/Bitcoin/All-2014*.txt", 4)

grepRDD.cache()

grepRDD.take(10).foreach(println)

1/pagecounts-20140101-000000.gz:commons.m Category:Bitcoin 2 26423
1/pagecounts-20140101-000000.gz:commons.m Category:Cryptocurrency 1 5885
1/pagecounts-20140101-000000.gz:commons.m Category:Cryptocurrencym 1 5885
1/pagecounts-20140101-000000.gz:commons.m File:Bitcoin-client-0.7.1.png 1 10412
1/pagecounts-20140101-000000.gz:commons.m File:Bitcoin.svg 1 9260
1/pagecounts-20140101-000000.gz:commons.m File:Bitcoin_exchange.png 8 136213
1/pagecounts-20140101-000000.gz:commons.m File:Bitcoin_logo.svg 1 10277
1/pagecounts-20140101-000000.gz:commons.m File:Bitcoin_screenshot_windows7.png 1 10414
1/pagecounts-20140101-000000.gz:commons.m File:De_Waag_Bitcoin.jpg 1 9713
1/pagecounts-20140101-000000.gz:commons.m File:Screenshot_of_Bitcoin-qt.png 4 37726

grepRDD.count
res3: Long = 719837                                                             

val goodRDD = grepRDD.filter(line => line.split(" ").size == 4)

goodRDD.count
res4: Long = 718543

val pvRDD = goodRDD.map(line => line.split(".gz:")(1))

pvRDD.take(10).foreach(println)

commons.m Category:Bitcoin 2 26423
commons.m Category:Cryptocurrency 1 5885
commons.m Category:Cryptocurrencym 1 5885
commons.m File:Bitcoin-client-0.7.1.png 1 10412
commons.m File:Bitcoin.svg 1 9260
commons.m File:Bitcoin_exchange.png 8 136213
commons.m File:Bitcoin_logo.svg 1 10277
commons.m File:Bitcoin_screenshot_windows7.png 1 10414
commons.m File:De_Waag_Bitcoin.jpg 1 9713
commons.m File:Screenshot_of_Bitcoin-qt.png 4 37726


val pvTupleRDD = goodRDD.map{ line => 
  val a = line.split(".gz:")
  
  val i = a(0).indexOf("-")
  val j = a(0).indexOf("-", i+1)
  
  val a1 = a(1).split(" ")
  
  (a1(0), a1(1), a1(2).toInt, a1(3).toLong, a(0).substring(i+1,j))
}

pvTupleRDD.take(10).foreach(println)

(commons.m,Category:Bitcoin,2,26423,20140101)
(commons.m,Category:Cryptocurrency,1,5885,20140101)
(commons.m,Category:Cryptocurrencym,1,5885,20140101)
(commons.m,File:Bitcoin-client-0.7.1.png,1,10412,20140101)
(commons.m,File:Bitcoin.svg,1,9260,20140101)
(commons.m,File:Bitcoin_exchange.png,8,136213,20140101)
(commons.m,File:Bitcoin_logo.svg,1,10277,20140101)
(commons.m,File:Bitcoin_screenshot_windows7.png,1,10414,20140101)
(commons.m,File:De_Waag_Bitcoin.jpg,1,9713,20140101)
(commons.m,File:Screenshot_of_Bitcoin-qt.png,4,37726,20140101)

pvTupleRDD.map(t => (t._2, t._3)).reduceByKey(_+_, 1).sortBy(t => t._2, false).take(30).foreach(println)

(Bitcoin,9229277)                                                               
(Cryptocurrency,525946)
(History_of_Bitcoin,199944)
(Digital_currency,131844)
(Bitcoin_protocol,110453)
(Bitcoin_network,67281)
(Coinbase,52644)
(Legality_of_Bitcoins_by_country,50524)
(Bitcoin_mining,39298)
(File:De_Waag_Bitcoin.jpg,39109)
(Bitcoins,38090)
(Bitcoin_ATM,37198)
(Legality_of_Bitcoin_by_country,35935)
(Digital_currency_exchanger,35773)
(File:Bitcoin-coins.jpg,34145)
(File:Bitcoin_October_2013.png,32600)
(Bitstamp,32060)
(File:Bitcoin_exchange.png,29530)
(Bitcoin_Foundation,26248)
(File:Bitcoin_logo.svg,25468)
(BitPay,22623)
(Blockchain.info,22038)
(Talk:Bitcoin,21287)
(File:Bitcoin_paper_wallet_generated_at_bitaddress.jpg,20211)
(Category:Bitcoin,19661)
(File:Electrum_Bitcoin_Wallet.png,19478)
(File:BitstampUSD_weekly.png,17995)
(Legal_status_of_Bitcoin,17664)
(File:Bitcoin_Transaction_Visual.png,16965)
(File:Bitcoin_winkdex.png,13852)


val bitcoinRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin")

bitcoinRDD.take(10).foreach(println)

(cs,Bitcoin,6,160908,20140101)
(da,Bitcoin,3,23560,20140101)
(de,Bitcoin,21,1933805,20140101)
(el,Bitcoin,3,69842,20140101)
(en,Bitcoin,1038,64958400,20140101)
(es,Bitcoin,90,3033703,20140101)
(et,Bitcoin,2,28882,20140101)
(fi,Bitcoin,9,255834,20140101)
(fr,Bitcoin,38,1598390,20140101)
(hy,Bitcoin,1,20403,20140101)

bitcoinRDD.map(t => t._3).collect().sum
res22: Int = 5906673

val dailyBitcoinRDD = bitcoinRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinRDD.take(10).foreach(println)

(2014-03-23,24083)                                                              
(2014-10-31,10410)
(2014-01-05,6279)
(2014-10-15,16448)
(2014-12-29,14758)
(2014-07-20,10852)
(2014-02-17,42804)
(2014-03-30,21796)
(2014-06-18,21536)
(2014-04-24,19196)

dailyBitcoinRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin-2014-daily.csv")


val cryptocurrencyRDD = pvTupleRDD.filter(t => t._2 == "Cryptocurrency")

cryptocurrencyRDD.take(10).foreach(println)

(en,Cryptocurrency,60,1055286,20140101)
(en,Cryptocurrency,76,1368081,20140101)
(en,Cryptocurrency,59,1034192,20140101)
(en,Cryptocurrency,63,1199954,20140101)
(en,Cryptocurrency,37,712061,20140101)
(en,Cryptocurrency,43,748242,20140101)
(en,Cryptocurrency,45,808301,20140101)
(en,Cryptocurrency,42,807432,20140101)
(id,Cryptocurrency,1,5937,20140101)
(nl,Cryptocurrency,3,42729,20140101)

cryptocurrencyRDD.map(t => t._3).collect().sum
res22: Int = 309760

val dailyCryptocurrencyRDD = cryptocurrencyRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyCryptocurrencyRDD.take(10).foreach(println)

(2014-03-23,1598)                                                               
(2014-10-31,717)
(2014-01-05,389)
(2014-10-15,980)
(2014-12-29,774)
(2014-07-20,674)
(2014-02-17,3614)
(2014-03-30,1650)
(2014-06-18,1397)
(2014-04-24,1350)

dailyCryptocurrencyRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency-2014-daily.csv")


val historyOfBitcoinRDD = pvTupleRDD.filter(t => t._2 == "History_of_Bitcoin")

historyOfBitcoinRDD.take(10).foreach(println)

(en,History_of_Bitcoin,22,909595,20140101)
(en,History_of_Bitcoin,23,1713781,20140101)
(en,History_of_Bitcoin,11,501388,20140101)
(en,History_of_Bitcoin,8,319449,20140101)
(en,History_of_Bitcoin,16,894912,20140101)
(en,History_of_Bitcoin,12,667385,20140101)
(en,History_of_Bitcoin,18,486368,20140101)
(en,History_of_Bitcoin,21,500561,20140101)
(en,History_of_Bitcoin,18,638902,20140101)
(en,History_of_Bitcoin,23,1046681,20140101)

historyOfBitcoinRDD.map(t => t._3).collect().sum
res22: Int = 134661

val dailyHistoryOfBitcoinRDD = historyOfBitcoinRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyHistoryOfBitcoinRDD.take(10).foreach(println)

(2014-03-23,531)                                                                
(2014-10-31,290)
(2014-01-05,91)
(2014-10-15,457)
(2014-12-29,389)
(2014-07-20,277)
(2014-02-17,933)
(2014-03-30,558)
(2014-06-18,426)
(2014-04-24,587)

dailyHistoryOfBitcoinRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/History_of_Bitcoin-2014-daily.csv")


~~~

