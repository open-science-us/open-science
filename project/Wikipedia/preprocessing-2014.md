## Preprocessing


### Filtering in lines with Bitcoin-related titles

~~~
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 1/*.gz > All-201401.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 2/*.gz > All-201402.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 3/*.gz > All-201403.txt
~~~

### Raw data issues

1. pagecounts-20141212-140001.gz
2. pagecounts-20141225-190001.gz
3. pagecounts-20141225-195959.gz
4. pagecounts-20141225-200001.gz
5. pagecounts-20141111-020001.gz
6. pagecounts-20141123-080001.gz
7. pagecounts-20141010-010001.gz
8. pagecounts-20141016-160001.gz
9. pagecounts-20141029-040001.gz
10. pagecounts-20140908-010001.gz
10. pagecounts-20140919-070001.gz
11. pagecounts-20140929-180001.gz
11. pagecounts-20140804-090001.gz
12. pagecounts-20140808-180001.gz
13. pagecounts-20140812-200001.gz
14. pagecounts-20140817-050013.gz
15. pagecounts-20140824-080001.gz
16. pagecounts-20140825-100001.gz
17. pagecounts-20140825-210001.gz
18. pagecounts-20140826-220015.gz
19. pagecounts-20140826-230001.gz
20. pagecounts-20140827-000013.gz
21. pagecounts-20140827-010006.gz
22. pagecounts-20140827-020003.gz
23. pagecounts-20140827-030015.gz
24. pagecounts-20140827-050001.gz
25. pagecounts-20140827-070014.gz
26. pagecounts-20140827-080017.gz
27. pagecounts-20140827-100015.gz
28. pagecounts-20140827-120015.gz
29. pagecounts-20140827-160001.gz
30. pagecounts-20140827-170007.gz
31. pagecounts-20140827-180013.gz
32. pagecounts-20140827-190016.gz
33. pagecounts-20140702-200001.gz
34. pagecounts-20140703-230001.gz
35. pagecounts-20140704-070001.gz
36. pagecounts-20140705-080001.gz
37. pagecounts-20140706-170002.gz
38. pagecounts-20140707-160001.gz
39. pagecounts-20140709-220001.gz
40. pagecounts-20140711-060001.gz
41. pagecounts-20140713-110001.gz
42. pagecounts-20140715-110001.gz
43. pagecounts-20140718-220001.gz
44. pagecounts-20140720-030001.gz
45. pagecounts-20140720-140001.gz
46. pagecounts-20140721-140001.gz
47. pagecounts-20140725-080001.gz
48. pagecounts-20140728-190001.gz
49. pagecounts-20140731-150001.gz
50. pagecounts-20140601-160001.gz
51. pagecounts-20140604-130003.gz
52. pagecounts-20140604-190002.gz
53. pagecounts-20140605-220001.gz
54. pagecounts-20140608-080001.gz
55. pagecounts-20140609-090002.gz
56. pagecounts-20140613-020001.gz
57. pagecounts-20140614-090001.gz
58. pagecounts-20140617-100001.gz
59. pagecounts-20140621-180001.gz
60. pagecounts-20140625-120001.gz
61. pagecounts-20140629-050001.gz
62. pagecounts-20140502-090001.gz
63. pagecounts-20140506-070001.gz
64. pagecounts-20140507-190001.gz
65. pagecounts-20140511-010001.gz
66. pagecounts-20140515-050001.gz
67. pagecounts-20140516-220001.gz
68. pagecounts-20140517-090011.gz
69. pagecounts-20140517-110001.gz
70. pagecounts-20140521-160001.gz
71. pagecounts-20140522-140001.gz
72. pagecounts-20140523-160001.gz
73. pagecounts-20140525-020001.gz
74. pagecounts-20140527-230001.gz
75. pagecounts-20140528-110001.gz
76. pagecounts-20140530-220001.gz
77. pagecounts-20140408-010001.gz
78. pagecounts-20140410-120011.gz
79. pagecounts-20140411-130001.gz
80. pagecounts-20140411-180001.gz
81. pagecounts-20140414-100002.gz
82. pagecounts-20140416-100003.gz
83. pagecounts-20140417-120001.gz
84. pagecounts-20140418-010007.gz
85. pagecounts-20140418-050001.gz
86. pagecounts-20140418-120001.gz
87. pagecounts-20140419-120001.gz
88. pagecounts-20140423-160002.gz
89. pagecounts-20140425-200001.gz
90. pagecounts-20140430-140001.gz
91. pagecounts-20140301-160001.gz
92. pagecounts-20140302-050001.gz
93. pagecounts-20140303-170002.gz
94. pagecounts-20140306-090001.gz
95. pagecounts-20140306-170001.gz
96. pagecounts-20140308-190001.gz
97. pagecounts-20140310-100001.gz
98. pagecounts-20140311-230001.gz
99. pagecounts-20140313-030001.gz
100. pagecounts-20140314-120001.gz
101. pagecounts-20140314-190001.gz
102. pagecounts-20140317-160001.gz
103. pagecounts-20140319-030011.gz
104. pagecounts-20140323-070001.gz
105. pagecounts-20140323-180002.gz
106. pagecounts-20140324-000001.gz
107. pagecounts-20140324-160001.gz
108. pagecounts-20140325-210001.gz
109. pagecounts-20140201-100001.gz
110. pagecounts-20140202-190001.gz
111. pagecounts-20140204-030001.gz
112. pagecounts-20140204-160001.gz
113. pagecounts-20140206-060002.gz
114. pagecounts-20140209-200001.gz
115. pagecounts-20140210-230002.gz
116. pagecounts-20140212-090001.gz
117. pagecounts-20140217-200001.gz
118. pagecounts-20140219-170001.gz
119. pagecounts-20140222-070001.gz
120. pagecounts-20140225-090002.gz
121. pagecounts-20140228-030001.gz
122. pagecounts-20140228-170001.gz
123. pagecounts-20140101-030001.gz
124. pagecounts-20140101-040008.gz
125. 

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
res22: Int = 9229277

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
res22: Int = 525946

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
res22: Int = 199944

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


val digitalcurrencyRDD = pvTupleRDD.filter(t => t._2 == "Digital_currency")

digitalcurrencyRDD.take(10).foreach(println)

(en,Digital_currency,10,172857,20140101)
(en,Digital_currency,19,260881,20140101)
(en,Digital_currency,12,304186,20140101)
(en,Digital_currency,24,389856,20140101)
(en,Digital_currency,15,289962,20140101)
(en,Digital_currency,20,418155,20140101)
(en,Digital_currency,21,331947,20140101)
(en,Digital_currency,19,375086,20140101)
(en,Digital_currency,33,693305,20140101)
(en,Digital_currency,32,534693,20140101)

digitalcurrencyRDD.map(t => t._3).collect().sum
res22: Int = 131844

val dailyDigitalcurrencyRDD = digitalcurrencyRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyDigitalcurrencyRDD.take(10).foreach(println)

(2014-03-23,335)                                                                
(2014-10-31,177)
(2014-01-05,91)
(2014-10-15,373)
(2014-12-29,266)
(2014-07-20,173)
(2014-02-17,621)
(2014-03-30,326)
(2014-06-18,279)
(2014-04-24,316)

dailyDigitalcurrencyRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Digital_currency-2014-daily.csv")


val protocolRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_protocol")

protocolRDD.take(10).foreach(println)

(en,Bitcoin_protocol,20,357450,20140101)
(en,Bitcoin_protocol,50,895428,20140101)
(en,Bitcoin_protocol,27,496462,20140101)
(en,Bitcoin_protocol,25,378199,20140101)
(en,Bitcoin_protocol,25,476558,20140101)
(en,Bitcoin_protocol,18,319628,20140101)
(en,Bitcoin_protocol,65,1211566,20140101)
(en,Bitcoin_protocol,28,495414,20140101)
(en,Bitcoin_protocol,37,755501,20140101)
(en,Bitcoin_protocol,36,637343,20140101)

protocolRDD.map(t => t._3).collect().sum
res25: Int = 110453   

val dailyProtocolRDD = protocolRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyProtocolRDD.take(10).foreach(println)

(2014-03-23,109)                                                                
(2014-10-31,43)
(2014-01-05,219)
(2014-10-15,100)
(2014-12-29,50)
(2014-07-20,58)
(2014-02-17,1128)
(2014-03-30,101)
(2014-06-18,83)
(2014-04-24,76)

dailyProtocolRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_protocol-2014-daily.csv")


val bitcoinNetworkRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_network")

bitcoinNetworkRDD.take(10).foreach(println)

(en,Bitcoin_network,1,7003,20140114)
(en,Bitcoin_network,50,1576517,20140302)
(en,Bitcoin_network,8,211091,20140302)
(en,Bitcoin_network,3,60412,20140302)
(en,Bitcoin_network,1,20469,20140303)
(en,Bitcoin_network,2,20483,20140303)
(en,Bitcoin_network,2,42147,20140303)
(en,Bitcoin_network,30,1132072,20140303)
(en,Bitcoin_network,7,134155,20140303)
(en,Bitcoin_network,4,76660,20140303)

bitcoinNetworkRDD.map(t => t._3).collect().sum
res33: Int = 67281 

val dailyBitcoinNetworkRDD = bitcoinNetworkRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinNetworkRDD.take(10).foreach(println)

(2014-09-23,325)                                                                
(2014-03-23,367)
(2014-05-17,153)
(2014-10-31,137)
(2014-10-15,178)
(2014-12-29,173)
(2014-06-25,169)
(2014-06-16,582)
(2014-03-30,337)
(2014-06-18,371)

dailyBitcoinNetworkRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_network-2014-daily.csv")
~~~

