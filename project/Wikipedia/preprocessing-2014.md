## Preprocessing


### Filtering in lines with Bitcoin-related titles

~~~
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 1/*.gz > All-201401.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 2/*.gz > All-201402.txt
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" 3/*.gz > All-201403.txt
~~~

### Raw data issues

Gzip file names do not end with "0000.gz".

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
14. pagecounts-20140817-000001.gz
14. pagecounts-20140817-050013.gz
15. pagecounts-20140819-010002.gz
16. pagecounts-20140821-030001.gz
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
63. pagecounts-20140502-120001.gz
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
77. pagecounts-20140403-140001.gz
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
109. pagecounts-20140331-040001.gz
109. pagecounts-20140201-100001.gz
110. pagecounts-20140202-190001.gz
111. pagecounts-20140204-030001.gz
112. pagecounts-20140204-160001.gz
113. pagecounts-20140206-060002.gz
114. pagecounts-20140209-200001.gz
115. pagecounts-20140210-230002.gz
116. pagecounts-20140212-090001.gz
117. pagecounts-20140217-200001.gz
118. pagecounts-20140218-110002.gz
118. pagecounts-20140219-170001.gz
119. pagecounts-20140222-070001.gz
120. pagecounts-20140225-090002.gz
121. pagecounts-20140228-030001.gz
122. pagecounts-20140228-170001.gz
123. pagecounts-20140101-030001.gz
124. pagecounts-20140101-040008.gz
125. pagecounts-20140101-050001.gz
126. pagecounts-20140101-080008.gz
127. pagecounts-20140101-100008.gz
128. pagecounts-20140101-110011.gz
129. pagecounts-20140101-140002.gz
130. pagecounts-20140101-180004.gz
131. pagecounts-20140101-190013.gz
132. pagecounts-20140101-200001.gz
133. pagecounts-20140101-210012.gz
134. pagecounts-20140101-220012.gz
135. pagecounts-20140102-020011.gz
136. pagecounts-20140102-040003.gz
137. pagecounts-20140102-050011.gz
138. pagecounts-20140102-060008.gz
139. pagecounts-20140102-070005.gz
140. pagecounts-20140102-100001.gz
141. pagecounts-20140102-130015.gz
142. pagecounts-20140102-140004.gz
143. pagecounts-20140102-150001.gz
144. pagecounts-20140102-160014.gz
145. pagecounts-20140102-170015.gz
146. pagecounts-20140102-210014.gz
147. pagecounts-20140102-230013.gz
148. pagecounts-20140103-050001.gz
149. pagecounts-20140103-100001.gz
150. pagecounts-20140103-140001.gz
151. pagecounts-20140103-190001.gz
152. pagecounts-20140103-200013.gz
153. pagecounts-20140103-220006.gz
154. pagecounts-20140104-000014.gz
155. pagecounts-20140104-030001.gz
156. pagecounts-20140104-080001.gz
157. pagecounts-20140104-090005.gz
158. pagecounts-20140104-120001.gz
159. pagecounts-20140104-160013.gz
160. pagecounts-20140104-170006.gz
161. pagecounts-20140104-180006.gz
162. pagecounts-20140104-210004.gz
163. pagecounts-20140104-230001.gz
164. pagecounts-20140105-040001.gz
165. pagecounts-20140109-230001.gz
165. pagecounts-20140112-020001.gz
166. pagecounts-20140114-180001.gz
167. pagecounts-20140118-080001.gz
168. pagecounts-20140120-020001.gz
169. pagecounts-20140123-020001.gz
170. pagecounts-20140127-020003.gz
171. pagecounts-20140128-220002.gz

~~~
zgrep -E "Digital_currency|Cryptocurrency|Bitcoin|Bitstamp|Coinbase|BitPay|Block_chain|Blockchain.info" pagecounts-2014*.gz > All-2014-missing.txt &
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
res3: Long = 736262                                                             

val goodRDD = grepRDD.filter(line => line.split(" ").size == 4)

goodRDD.count
res4: Long = 734968

val pvRDD = goodRDD.map(line => line.split(".gz:")(1))

pvRDD.take(10).foreach(println)

commons.m Category:Cryptocurrency 1 5885
commons.m Category:Cryptocurrencyn 1 5885
commons.m File:Bitcoin-0.6.0.png 1 8615
commons.m File:Bitcoin.png 3 94290
commons.m File:Bitcoin_Transaction_Visual.png 1 10791
commons.m File:Bitcoin_exchange.png 6 73461
commons.m File:Bitcoin_logo.svg 1 10270
commons.m File:Bitcoin_screenshot_windows7.png 1 10413
commons.m File:Electrum_Bitcoin_Wallet.png 1 10418
commons.m File:Screenshot_of_Bitcoin-qt.png 3 28296


val pvTupleRDD = goodRDD.map{ line => 
  val a = line.split(".gz:")
  
  val i = a(0).indexOf("-")
  val j = a(0).indexOf("-", i+1)
  
  val a1 = a(1).split(" ")
  
  (a1(0), a1(1), a1(2).toInt, a1(3).toLong, a(0).substring(i+1,j))
}

pvTupleRDD.take(10).foreach(println)

(commons.m,Category:Cryptocurrency,1,5885,20140101)
(commons.m,Category:Cryptocurrencyn,1,5885,20140101)
(commons.m,File:Bitcoin-0.6.0.png,1,8615,20140101)
(commons.m,File:Bitcoin.png,3,94290,20140101)
(commons.m,File:Bitcoin_Transaction_Visual.png,1,10791,20140101)
(commons.m,File:Bitcoin_exchange.png,6,73461,20140101)
(commons.m,File:Bitcoin_logo.svg,1,10270,20140101)
(commons.m,File:Bitcoin_screenshot_windows7.png,1,10413,20140101)
(commons.m,File:Electrum_Bitcoin_Wallet.png,1,10418,20140101)
(commons.m,File:Screenshot_of_Bitcoin-qt.png,3,28296,20140101)

pvTupleRDD.map(t => (t._2, t._3)).reduceByKey(_+_, 1).sortBy(t => t._2, false).take(50).foreach(println)

(Bitcoin,9481480)                                                               
(Cryptocurrency,539869)
(History_of_Bitcoin,204831)
(Digital_currency,135307)
(Bitcoin_protocol,114584)
(Bitcoin_network,68410)
(Coinbase,53817)
(Legality_of_Bitcoins_by_country,51679)
(Bitcoin_mining,40617)
(File:De_Waag_Bitcoin.jpg,40538)
(Bitcoins,39107)
(Bitcoin_ATM,37778)
(Digital_currency_exchanger,36707)
(Legality_of_Bitcoin_by_country,36197)
(File:Bitcoin-coins.jpg,35267)
(File:Bitcoin_October_2013.png,33578)
(Bitstamp,33111)
(File:Bitcoin_exchange.png,30653)
(Bitcoin_Foundation,26914)
(File:Bitcoin_logo.svg,26216)
(BitPay,22887)
(Blockchain.info,22351)
(Talk:Bitcoin,21895)
(File:Bitcoin_paper_wallet_generated_at_bitaddress.jpg,20986)
(File:Electrum_Bitcoin_Wallet.png,20196)
(Category:Bitcoin,20162)
(File:BitstampUSD_weekly.png,18491)
(Legal_status_of_Bitcoin,18203)
(File:Bitcoin_Transaction_Visual.png,17972)
(File:Bitcoin_winkdex.png,14257)
(File:Bitcoin_screenshot.png,13681)
(File:Bitcoin_screenshot_windows7.png,12995)
(File:Bitcoin_Transaction_Visual.svg,12649)
(Block_chain,12530)
(Block_chain_(transaction_database),11988)
(Category:Cryptocurrency,11943)
(Bitcoinp,11636)
(File:Bitcoin_exchange_mtgox_-_Feb2012-Feb2014_-_log_scale.png,11256)
(Category:Bitcoin_exchanges,10320)
(File:BitcoinSign.svg,9011)
(File:Bitcoin.png,8650)
(LocalBitcoins,7950)
(Protocol_of_Bitcoin,7801)
(%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Bitcoin_screenshot_windows7.png,7483)
(en:Bitcoin,6811)
(File:Screenshot_of_Bitcoin-qt.png,6713)
(File:Bitcoin.svg,6173)
(File:Butterfly_Labs_60GH_Bitcoin_Miner_Single_SC.jpg,5728)
(%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:De_Waag_Bitcoin.jpg,5566)
(File:Bitcoinpaymentverification.png,5454)


val bitcoinRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin")

bitcoinRDD.take(10).foreach(println)

(cs,Bitcoin,4,80454,20140101)
(da,Bitcoin,2,23560,20140101)
(de,Bitcoin,36,2602878,20140101)
(el,Bitcoin,2,0,20140101)
(en,Bitcoin,898,54800696,20140101)
(es,Bitcoin,47,1550497,20140101)
(et,Bitcoin,1,14441,20140101)
(fi,Bitcoin,4,113688,20140101)
(fr,Bitcoin,20,622835,20140101)
(hr,Bitcoin,1,0,20140101)

bitcoinRDD.map(t => t._3).collect().sum
res22: Int = 9481480

val dailyBitcoinRDD = bitcoinRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinRDD.take(10).foreach(println)

(2014-03-23,26328)                                                              
(2014-10-31,10410)
(2014-01-05,7177)
(2014-12-29,14758)
(2014-07-20,11714)
(2014-02-17,44765)
(2014-10-15,16448)
(2014-06-18,21536)
(2014-04-24,19196)
(2014-03-30,21796)

dailyBitcoinRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin-2014-daily.csv")


val cryptocurrencyRDD = pvTupleRDD.filter(t => t._2 == "Cryptocurrency")

cryptocurrencyRDD.take(10).foreach(println)

(en,Cryptocurrency,59,907602,20140101)
(en,Cryptocurrency,39,821175,20140101)
(en,Cryptocurrency,66,1200845,20140101)
(en,Cryptocurrency,69,1107968,20140101)
(en,Cryptocurrency,58,1197453,20140101)
(en,Cryptocurrency,37,754296,20140101)
(en,Cryptocurrency,57,1145927,20140101)
(en,Cryptocurrency,82,1447924,20140101)
(id,Cryptocurrency,1,5941,20140101)
(en,Cryptocurrency,69,1245881,20140101)

cryptocurrencyRDD.map(t => t._3).collect().sum
res22: Int = 539869

val dailyCryptocurrencyRDD = cryptocurrencyRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyCryptocurrencyRDD.take(10).foreach(println)

(2014-03-23,1750)                                                               
(2014-10-31,717)
(2014-01-05,449)
(2014-12-29,774)
(2014-07-20,728)
(2014-02-17,3786)
(2014-10-15,980)
(2014-06-18,1397)
(2014-04-24,1350)
(2014-03-30,1650)

dailyCryptocurrencyRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Cryptocurrency-2014-daily.csv")


val historyOfBitcoinRDD = pvTupleRDD.filter(t => t._2 == "History_of_Bitcoin")

historyOfBitcoinRDD.take(10).foreach(println)

(en,History_of_Bitcoin,9,363969,20140101)
(en,History_of_Bitcoin,13,1046574,20140101)
(en,History_of_Bitcoin,10,455943,20140101)
(en,History_of_Bitcoin,36,941362,20140101)
(en,History_of_Bitcoin,9,409535,20140101)
(en,History_of_Bitcoin,30,803911,20140101)
(en,History_of_Bitcoin,24,866492,20140101)
(en,History_of_Bitcoin,37,1676081,20140101)
(en,History_of_Bitcoin,25,1141613,20140101)
(fa,History_of_Bitcoin,1,7212,20140101)

historyOfBitcoinRDD.map(t => t._3).collect().sum
res22: Int = 204831

val dailyHistoryOfBitcoinRDD = historyOfBitcoinRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyHistoryOfBitcoinRDD.take(10).foreach(println)

(2014-03-23,573)                                                                
(2014-10-31,290)
(2014-10-15,457)
(2014-01-05,105)
(2014-12-29,389)
(2014-07-20,305)
(2014-02-17,983)
(2014-03-30,558)
(2014-06-18,426)
(2014-04-24,587)

dailyHistoryOfBitcoinRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/History_of_Bitcoin-2014-daily.csv")


val digitalcurrencyRDD = pvTupleRDD.filter(t => t._2 == "Digital_currency")

digitalcurrencyRDD.take(10).foreach(println)

(en,Digital_currency,11,187209,20140101)
(en,Digital_currency,14,201626,20140101)
(en,Digital_currency,15,347532,20140101)
(en,Digital_currency,34,423326,20140101)
(en,Digital_currency,15,335570,20140101)
(en,Digital_currency,15,245280,20140101)
(en,Digital_currency,28,911389,20140101)
(en,Digital_currency,23,331765,20140101)
(en,Digital_currency,22,389451,20140101)
(en,Digital_currency,29,463151,20140101)

digitalcurrencyRDD.map(t => t._3).collect().sum
res22: Int = 135307

val dailyDigitalcurrencyRDD = digitalcurrencyRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyDigitalcurrencyRDD.take(10).foreach(println)

(2014-03-23,369)                                                                
(2014-10-31,177)
(2014-10-15,373)
(2014-01-05,107)
(2014-12-29,266)
(2014-07-20,181)
(2014-02-17,647)
(2014-03-30,326)
(2014-06-18,279)
(2014-04-24,316)

dailyDigitalcurrencyRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Digital_currency-2014-daily.csv")


val protocolRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_protocol")

protocolRDD.take(10).foreach(println)

(en,Bitcoin_protocol,32,517261,20140101)
(en,Bitcoin_protocol,25,456201,20140101)
(en,Bitcoin_protocol,23,398061,20140101)
(en,Bitcoin_protocol,38,459569,20140101)
(en,Bitcoin_protocol,20,436344,20140101)
(en,Bitcoin_protocol,31,633401,20140101)
(en,Bitcoin_protocol,28,575826,20140101)
(en,Bitcoin_protocol,41,1032503,20140101)
(en,Bitcoin_protocol,30,538016,20140101)
(en,Bitcoin_protocol,30,556414,20140101)

protocolRDD.map(t => t._3).collect().sum
res25: Int = 114584   

val dailyProtocolRDD = protocolRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyProtocolRDD.take(10).foreach(println)

(2014-03-23,118)                                                                
(2014-10-31,43)
(2014-01-05,259)
(2014-12-29,50)
(2014-07-20,63)
(2014-02-17,1180)
(2014-10-15,100)
(2014-06-18,83)
(2014-04-24,76)
(2014-03-30,101)

dailyProtocolRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_protocol-2014-daily.csv")


val bitcoinNetworkRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_network")

bitcoinNetworkRDD.take(10).foreach(println)

(en,Bitcoin_network,9,168680,20140303)
(en,Bitcoin_network,4,58020,20140306)
(en,Bitcoin_network,21,451119,20140306)
(en,Bitcoin_network,7,115301,20140308)
(en,Bitcoin_network,5,129585,20140310)
(en,Bitcoin_network,15,263095,20140311)
(en,Bitcoin_network,6,76296,20140313)
(en,Bitcoin_network,5,95481,20140314)
(en,Bitcoin_network,15,393057,20140314)
(en,Bitcoin_network,33,573074,20140317)

bitcoinNetworkRDD.map(t => t._3).collect().sum
res33: Int = 68410 

val dailyBitcoinNetworkRDD = bitcoinNetworkRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinNetworkRDD.take(10).foreach(println)

(2014-09-23,325)                                                                
(2014-03-23,399)
(2014-05-17,156)
(2014-10-31,137)
(2014-10-15,178)
(2014-12-29,173)
(2014-06-25,181)
(2014-07-20,121)
(2014-06-16,582)
(2014-03-30,337)

dailyBitcoinNetworkRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_network-2014-daily.csv")


val coinbaseRDD = pvTupleRDD.filter(t => t._2 == "Coinbase")

coinbaseRDD.take(10).foreach(println)

(de,Coinbase,1,6031,20140101)
(en,Coinbase,10,115986,20140101)
(en,Coinbase,5,50642,20140101)
(en,Coinbase,5,51577,20140101)
(en,Coinbase,1,10121,20140101)
(en,Coinbase,2,20248,20140101)
(en,Coinbase,2,21227,20140101)
(en,Coinbase,2,21227,20140101)
(en,Coinbase,6,60744,20140101)
(en,Coinbase,7,71782,20140101)

coinbaseRDD.map(t => t._3).collect().sum
res41: Int = 53817 

val dailyCoinbaseRDD = coinbaseRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyCoinbaseRDD.take(10).foreach(println)

(2014-03-23,92)                                                                 
(2014-10-31,88)
(2014-01-05,42)
(2014-12-29,90)
(2014-07-20,149)
(2014-02-17,181)
(2014-10-15,291)
(2014-06-18,137)
(2014-04-24,137)
(2014-03-30,126)

dailyCoinbaseRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Coinbase-2014-daily.csv")


val legalityRDD = pvTupleRDD.filter(t => t._2 == "Legality_of_Bitcoins_by_country" || t._2 == "Legality_of_Bitcoin_by_country")

legalityRDD.take(10).foreach(println)

(en,Legality_of_Bitcoins_by_country,15,631339,20140228)
(en,Legality_of_Bitcoins_by_country,51,1990600,20140228)
(en,Legality_of_Bitcoins_by_country,6,86681,20140301)
(en,Legality_of_Bitcoins_by_country,7,145469,20140302)
(en,Legality_of_Bitcoins_by_country,28,630987,20140303)
(en,Legality_of_Bitcoins_by_country,20,643648,20140306)
(en,Legality_of_Bitcoins_by_country,24,492396,20140306)
(en,Legality_of_Bitcoins_by_country,14,323323,20140308)
(en,Legality_of_Bitcoins_by_country,11,440903,20140310)
(en,Legality_of_Bitcoins_by_country,14,528906,20140311)

legalityRDD.map(t => t._3).collect().sum
res46: Int = 87876                                                              

val dailyLegalityRDD = legalityRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyLegalityRDD.take(10).foreach(println)

(2014-09-23,314)                                                                
(2014-03-23,185)
(2014-05-17,123)
(2014-10-31,307)
(2014-10-15,312)
(2014-12-29,681)
(2014-06-25,181)
(2014-07-20,290)
(2014-06-16,207)
(2014-03-30,337)

dailyLegalityRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Legality_of_Bitcoin_by_country-2014-daily.csv")


val miningRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_mining")

miningRDD.take(10).foreach(println)

(en,Bitcoin_mining,8,139583,20140101)
(en,Bitcoin_mining,11,192898,20140101)
(en,Bitcoin_mining,9,179457,20140101)
(en,Bitcoin_mining,5,100673,20140101)
(en,Bitcoin_mining,13,239246,20140101)
(en,Bitcoin_mining,12,239270,20140101)
(en,Bitcoin_mining,8,140511,20140101)
(en,Bitcoin_mining,18,418148,20140101)
(en,Bitcoin_mining,12,219318,20140101)
(en,Bitcoin_mining,21,398757,20140101)

miningRDD.map(t => t._3).collect().sum
res50: Int = 40617                                                              

val dailyMiningRDD = miningRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyMiningRDD.take(10).foreach(println)

(2014-03-23,62)                                                                 
(2014-10-31,45)
(2014-01-05,79)
(2014-12-29,49)
(2014-07-20,55)
(2014-02-17,94)
(2014-10-15,50)
(2014-06-18,130)
(2014-04-24,67)
(2014-03-30,69)

dailyMiningRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_mining-2014-daily.csv")


val bitcoinATMRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_ATM")

bitcoinATMRDD.take(10).foreach(println)

(en,Bitcoin_ATM,1,8750,20140101)
(en,Bitcoin_ATM,1,8742,20140102)
(en,Bitcoin_ATM,1,9728,20140103)
(en,Bitcoin_ATM,1,9776,20140103)
(en,Bitcoin_ATM,1,8767,20140104)
(en,Bitcoin_ATM,1,8767,20140104)
(en,Bitcoin_ATM,1,7197,20140128)
(en,Bitcoin_ATM,1,7241,20140201)
(en,Bitcoin_ATM,1,8830,20140209)
(en,Bitcoin_ATM,1,32105,20140210)

bitcoinATMRDD.map(t => t._3).collect().sum
res54: Int = 37778                                                              

val dailyBitcoinATMRDD = bitcoinATMRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitcoinATMRDD.take(10).foreach(println)

(2014-03-23,135)                                                                
(2014-10-31,95)
(2014-10-15,285)
(2014-01-05,2)
(2014-12-29,74)
(2014-07-20,101)
(2014-02-17,10)
(2014-03-30,115)
(2014-06-18,148)
(2014-04-24,91)

dailyBitcoinATMRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_ATM-2014-daily.csv")


val dceRDD = pvTupleRDD.filter(t => t._2 == "Digital_currency_exchanger")

dceRDD.take(10).foreach(println)

(en,Digital_currency_exchanger,3,38478,20140101)
(en,Digital_currency_exchanger,3,38479,20140101)
(en,Digital_currency_exchanger,1,12827,20140101)
(en,Digital_currency_exchanger,4,51308,20140101)
(en,Digital_currency_exchanger,2,25632,20140101)
(en,Digital_currency_exchanger,7,91732,20140101)
(en,Digital_currency_exchanger,8,103575,20140101)
(en,Digital_currency_exchanger,12,257230,20140101)
(en,Digital_currency_exchanger,5,66355,20140101)
(en,Digital_currency_exchanger,9,119467,20140101)

dceRDD.map(t => t._3).collect().sum
res58: Int = 36707                                                              

val dailyDceRDD = dceRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyDceRDD.take(10).foreach(println)

(2014-03-23,77)                                                                 
(2014-10-31,42)
(2014-10-15,314)
(2014-01-05,27)
(2014-12-29,63)
(2014-07-20,52)
(2014-02-17,170)
(2014-03-30,70)
(2014-06-18,65)
(2014-04-24,84)

dailyDceRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Digital_currency_exchanger-2014-daily.csv")


val bitstampRDD = pvTupleRDD.filter(t => t._2 == "Bitstamp")

bitstampRDD.take(10).foreach(println)

(en,Bitstamp,4,60973,20140101)
(en,Bitstamp,4,27919,20140101)
(en,Bitstamp,1,9312,20140101)
(en,Bitstamp,3,18638,20140101)
(en,Bitstamp,1,9318,20140101)
(en,Bitstamp,4,38239,20140101)
(en,Bitstamp,6,80561,20140101)
(en,Bitstamp,4,60978,20140101)
(en,Bitstamp,5,39045,20140101)
(en,Bitstamp,2,18630,20140101)

bitstampRDD.map(t => t._3).collect().sum
res62: Int = 33111                                                              

val dailyBitstampRDD = bitstampRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitstampRDD.take(10).foreach(println)

(2014-03-23,87)                                                                 
(2014-10-31,38)
(2014-01-05,20)
(2014-12-29,35)
(2014-07-20,50)
(2014-02-17,221)
(2014-10-15,78)
(2014-06-18,80)
(2014-04-24,82)
(2014-03-30,76)

dailyBitstampRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitstamp-2014-daily.csv")


val foundationRDD = pvTupleRDD.filter(t => t._2 == "Bitcoin_Foundation")

foundationRDD.take(10).foreach(println)

(en,Bitcoin_Foundation,4,37744,20140101)
(en,Bitcoin_Foundation,1,9436,20140101)
(en,Bitcoin_Foundation,1,9436,20140101)
(en,Bitcoin_Foundation,5,47160,20140101)
(en,Bitcoin_Foundation,4,37728,20140101)
(en,Bitcoin_Foundation,1,9442,20140101)
(en,Bitcoin_Foundation,4,60041,20140101)
(en,Bitcoin_Foundation,6,56652,20140101)
(en,Bitcoin_Foundation,1,9445,20140101)
(en,Bitcoin_Foundation,1,9445,20140101)

foundationRDD.map(t => t._3).collect().sum
res66: Int = 26914                                                              

val dailyFoundationRDD = foundationRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyFoundationRDD.take(10).foreach(println)

(2014-03-23,61)                                                                 
(2014-10-31,121)
(2014-10-15,66)
(2014-01-05,15)
(2014-12-29,67)
(2014-07-20,67)
(2014-02-17,46)
(2014-03-30,79)
(2014-06-18,75)
(2014-04-24,55)

dailyFoundationRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Bitcoin_Foundation-2014-daily.csv")


val bitPayRDD = pvTupleRDD.filter(t => t._2 == "BitPay")

bitPayRDD.take(10).foreach(println)

(en,BitPay,1,6943,20140102)
(zh,BitPay,1,8354,20140102)
(en,BitPay,1,6968,20140103)
(en,BitPay,2,1732,20140123)
(en,BitPay,1,9945,20140127)
(en,BitPay,1,10028,20140201)
(en,BitPay,1,10041,20140204)
(en,BitPay,2,20088,20140206)
(en,BitPay,1,10027,20140209)
(en,BitPay,1,10027,20140210)

bitPayRDD.map(t => t._3).collect().sum
res70: Int = 22887                                                              

val dailyBitPayRDD = bitPayRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBitPayRDD.take(10).foreach(println)

(2014-09-23,96)                                                                 
(2014-03-23,18)
(2014-01-23,23)
(2014-05-17,33)
(2014-10-31,64)
(2014-10-15,84)
(2014-12-29,140)
(2014-02-22,55)
(2014-02-17,55)
(2014-02-23,31)

dailyBitPayRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/BitPay-2014-daily.csv")


val blockchainInfoRDD = pvTupleRDD.filter(t => t._2 == "Blockchain.info")

blockchainInfoRDD.take(10).foreach(println)

(en,Blockchain.info,6,146384,20140109)
(en,Blockchain.info,2,18276,20140112)
(en,Blockchain.info,10,18004,20140114)
(en,Blockchain.info,1,8995,20140120)
(en,Blockchain.info,3,28567,20140127)
(en,Blockchain.info,3,26742,20140128)
(en,Blockchain.info,9,85685,20140201)
(en,Blockchain.info,3,28914,20140202)
(en,Blockchain.info,2,40098,20140204)
(en,Blockchain.info,4,29960,20140206)

blockchainInfoRDD.map(t => t._3).collect().sum
res74: Int = 22351                                                              

val dailyBlockchainInfoRDD = blockchainInfoRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBlockchainInfoRDD.take(10).foreach(println)

(2014-03-23,45)                                                                 
(2014-10-31,44)
(2014-10-15,63)
(2014-12-29,132)
(2014-07-20,35)
(2014-02-17,59)
(2014-03-30,23)
(2014-06-18,75)
(2014-04-24,51)
(2014-08-21,50)

dailyBlockchainInfoRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Blockchain_info-2014-daily.csv")


val legalStatusRDD = pvTupleRDD.filter(t => t._2 == "Legal_status_of_Bitcoin")

legalStatusRDD.take(10).foreach(println)

(en,Legal_status_of_Bitcoin,20,596598,20140101)
(en,Legal_status_of_Bitcoin,11,331792,20140101)
(en,Legal_status_of_Bitcoin,3,137435,20140101)
(en,Legal_status_of_Bitcoin,3,72171,20140101)
(en,Legal_status_of_Bitcoin,5,121300,20140101)
(en,Legal_status_of_Bitcoin,8,193484,20140101)
(en,Legal_status_of_Bitcoin,12,290806,20140101)
(en,Legal_status_of_Bitcoin,3,72183,20140101)
(en,Legal_status_of_Bitcoin,5,210623,20140101)
(en,Legal_status_of_Bitcoin,1,24058,20140102)

legalStatusRDD.map(t => t._3).collect().sum
res78: Int = 18203                                                              

val dailyLegalStatusRDD = legalStatusRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyLegalStatusRDD.take(10).foreach(println)

(2014-09-23,2)                                                                  
(2014-03-23,28)
(2014-01-23,191)
(2014-05-17,12)
(2014-10-31,6)
(2014-01-05,11)
(2014-12-29,7)
(2014-02-22,129)
(2014-02-17,204)
(2014-06-16,24)

dailyLegalStatusRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Legal_status_of_Bitcoin-2014-daily.csv")


val bcRDD = pvTupleRDD.filter(t => t._2 == "Block_chain")

bcRDD.take(10).foreach(println)

(en,Block_chain,4,33249,20140101)
(en,Block_chain,4,33200,20140101)
(en,Block_chain,2,8300,20140101)
(en,Block_chain,1,25719,20140101)
(en,Block_chain,1,8313,20140101)
(en,Block_chain,1,8313,20140101)
(en,Block_chain,2,16626,20140101)
(en,Block_chain,1,8313,20140101)
(en,Block_chain,2,17614,20140101)
(en,Block_chain,2,34043,20140102)

bcRDD.map(t => t._3).collect().sum
res22: Int = 12530

val dailyBcRDD = bcRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBcRDD.take(10).foreach(println)

(2014-03-23,44)                                                                 
(2014-10-31,31)
(2014-01-05,2)
(2014-10-15,38)
(2014-12-29,21)
(2014-07-20,25)
(2014-02-17,56)
(2014-03-30,50)
(2014-06-18,34)
(2014-04-24,73)

dailyBcRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain-2014-daily.csv")


val bcdRDD = pvTupleRDD.filter(t => t._2 == "Block_chain_(transaction_database)" || t._2 == "Block_chain_(database)")

bcdRDD.take(10).foreach(println)

(en,Block_chain_(transaction_database),4,29615,20140728)
(en,Block_chain_(transaction_database),1,7405,20140731)
(en,Block_chain_(transaction_database),4,29701,20140808)
(en,Block_chain_(transaction_database),7,53031,20140812)
(en,Block_chain_(transaction_database),1,7422,20140817)
(en,Block_chain_(transaction_database),3,22267,20140819)
(en,Block_chain_(transaction_database),2,14849,20140821)
(en,Block_chain_(transaction_database),1,7423,20140824)
(en,Block_chain_(transaction_database),1,7428,20140825)
(en,Block_chain_(transaction_database),3,22336,20140826)

bcdRDD.map(t => t._3).collect().sum
res22: Int = 11988

val dailyBcdRDD = bcdRDD.map(t => (t._5, t._3)).reduceByKey(_+_, 1).coalesce(1).map{ x => 
  (x._1.substring(0,4) + "-" + x._1.substring(4,6) + "-" + x._1.substring(6), x._2)
}

dailyBcdRDD.take(10).foreach(println)

(2014-09-23,45)                                                                 
(2014-11-27,73)
(2014-09-16,35)
(2014-10-27,192)
(2014-12-14,74)
(2014-10-31,120)
(2014-08-03,15)
(2014-10-15,122)
(2014-12-07,125)
(2014-07-20,16)

dailyBcdRDD.map{x => (x._1 + "," + x._2)}.saveAsTextFile("/work/R/example/Wikipedia/Bitcoin/Block_chain_database-2014-daily.csv")
~~~
