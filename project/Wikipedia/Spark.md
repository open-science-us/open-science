## Using Spark

~~~
bin/spark-shell --master spark://localhost:7077 \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer


import org.apache.log4j.Logger
import org.apache.log4j.Level
Logger.getLogger("org.apache.spark").setLevel(Level.WARN)

import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel


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

bitcoinRDD.collect().foreach(println)

ca Bitcoin 2 69374                                                              
commons.m %22https://upload.wikimedia.org/wikipedia/commons/1/12/Bitcoin_explained_in_3_minutes.webm%22 1 4845
commons.m %22https://upload.wikimedia.org/wikipedia/commons/1/12/Bitcoin_explained_in_3_minutes.webm%22>download 1 4508
commons.m %22https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Bitcoin_explained_in_3_minutes.webm/854px--Bitcoin_explained_in_3_minutes.webm.jpg%22 1 4914
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.1080p.webm%22 1 4913
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.160p.ogv%22 1 4915
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.360p.ogv%22 1 4914
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.360p.webm%22 1 4912
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.480p.ogv%22 1 4916
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.480p.webm%22 1 4913
commons.m %22https://upload.wikimedia.org/wikipedia/commons/transcoded/1/12/Bitcoin_explained_in_3_minutes.webm/Bitcoin_explained_in_3_minutes.webm.720p.webm%22 1 4913
commons.m %C3%8Domh%C3%A1:Bitcoin_logo.svg 1 4714
commons.m File:Bitcoin-coins.jpg 1 4996
commons.m File:Bitcoin_explained_in_3_minutes.webm 1 9957
commons.m File:Denarium_Bitcoin_100k_Bits.png 1 8607
cs Bitcoin 6 189234
de Bitcoin 34 3092297
de Bitcoin_Fog 1 9472
de Diskussion:Bitcoin 1 29115
el Bitcoin 2 53236
en Bitcoin 164 22021019
en Bitcoin/robots.txt 1 6590
en Bitcoin/trackback 1 25093
en Bitcoin_ATM 1 12099
en Bitcoin_Black_Friday 1 649073
en Bitcoin_Center_NYC 1 8595
en Bitcoin_Fog 6 112706
en Bitcoin_Foundation 2 30570
en Bitcoin_Protocol 1 24111
en Bitcoin_faucet 3 64429
en Bitcoin_mining 2 48248
en Bitcoin_network 7 168191
en Bitcoins 2 774278
en Bitcoinwww.urbandictionary.com/ 1 6616
en Book:Bitcoin 1 8136
en File%3ABitcoin_magazine_adjust_350.png 1 8339
en File:Bitcoin_October_2013.png 1 8090
en File:Bitcoinpaymentverification.png 1 9043
en File:Icarus_Bitcoin_Mining_rig.jpg 1 9407
en History_of_Bitcoin 19 925985
en LocalBitcoins 2 20386
en Special:RecentChangesLinked/Bitcoin 1 13866
en Talk:Bitcoin/Archive_20 1 41641
en Talk:Bitcoin/Archive_5 2 0
en Wikipedia:WikiProject_Bitcoin/sidebar 1 6603
en Zooko_Wilcox-O'%3E%3Cb%3EZooko%20Wilcox%3C/b%3E%3C/a%3E%3Cspan%3E%20told%20WIRED%20the%20launch%20is%20still%20roughly%20six%20months%20away.%20%3C/span%3E%3C/p%3E%20%3Cp%3E%3Cspan%3EThere%20are%20some%20similarities%20between%20Bitcoin%20and%20ZCash%20though,%20as%20both%20digital%20currencies%20are%20generated%20through%20a%20process%20known%20as%20%E2%80%9C%3C/span%3E%3Ca 1 15477
es Bitcoin 24 1228221
es Bitcoinhttps://es.wikipedia.org/wiki/Bitcoin 1 30753
et Arutelu:Bitcoin 1 6077
fa %D9%88%DB%8C%DA%98%D9%87:%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87%D9%94_%D8%B3%D8%B1%D8%A7%D8%B3%D8%B1%DB%8C/Bitcoin_logo.svg 1 7541
fi Bitcoin 4 123624
fr Bitcoin 20 1145565
fr Bitcoins 1 51924
hr Bitcoin 1 14943
hu Bitcoin 4 91998
id Berkas:BitcoinSign.svg 1 9886
id Berkas:Bitcoin_screenshot_windows7.png 1 10002
id Bitcoin 4 101714
it Bitcoin 11 225288
nl Bitcoin 2 31918
pl Bitcoin 11 290466
pt Armazenamento_Quente_e_Frio_(Bitcoin) 1 15875
pt Bitcoin 11 550126
ro Bitcoin 3 59952
ru Bitcoin 5 1031825
ru.n %D0%92%D0%B5%D0%B4%D1%83%D1%89%D0%B8%D0%B9_Bloomberg_%D1%81%D1%82%D0%B0%D0%BB_%D0%B6%D0%B5%D1%80%D1%82%D0%B2%D0%BE%D0%B9_%D0%BA%D1%80%D0%B0%D0%B6%D0%B8_Bitcoin_%D0%B2_%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D0%BC_%D1%8D%D1%84%D0%B8%D1%80%D0%B5 1 19335
sh Bitcoin 1 12020
sk Bitcoin 1 12569
sl Bitcoin 1 15994
sv Bitcoin 1 22161
tr Bitcoin 5 73763
tr Dosya:Bitcoin_Transaction_Visual.svg 1 9299
tr Ro.wikipedia.org/wiki/Bitcoin 1 5925
uk Bitcoin 7 149156
vi Bitcoin 2 74086
zh User_talk:HorseRider_Bitcointalk 1 9320
commons.m File:Bitcoin-coins.jpg 1 4995
commons.m File:Bitcoin-screen.png 1 7970
commons.m File:Bitcoin.svg 1 11584
commons.m File:Physical_Bitcoin_by_Mike_Cauldwell_(Casascius).jpg 1 9680
commons.m Image:Bitcoin_screenshot_windows7.png 1 10967
cs Bitcoin 1 31539
da Bitcoin 1 19998
de Benutzer:Bitcoiner 1 6289
de Bitcoin 11 1030618
de Diskussion:Bitcoin 1 29115
el Bitcoin 1 26618
en Bitcoin 150 20351448
en Bitcoin_ATM 3 36422
en Bitcoin_Core 1 649041
en Bitcoin_Fog 2 24784
en Bitcoin_Foundation 1 15285
en Bitcoin_Group 1 10471
en Bitcoin_mining 3 72361
en Bitcoin_network 7 240526
en Bitcoin_protocol 1 24108
en Bitcoinage 1 125267
en Bitcoins 1 125254
en CEX.IO_Bitcoin_Exchange 2 18176
en Category:People_associated_with_Bitcoin 1 24591
en Category_talk:Bitcoin_exchanges 1 9727
en File:Bitcoin_price_and_volatility.svg 1 20590
en File:Denarium_Bitcoin_100k_Bits.png 2 17290
en File:Electrum_Bitcoin_Wallet.png 1 10273
en History_of_Bitcoin 14 720248
en LocalBitcoins 1 10201
en Talk:Bitcoin/Archive_10 2 303307
en User_talk:Bitcoin_Guy 1 8567
es Bitcoin 34 1871477
fa %D9%BE%D8%B1%D9%88%D9%86%D8%AF%D9%87:Bitcoin.svg 1 11530
fi Bitcoin 1 30906
fr Bitcoin 51 2536920
fr Bitcoin%26usg%3DAFQjCNHzsLiNJVTlV0HmaokOCcPJ5O3PxQ%26sig2%3DrhR6rn3znLyqeKyjIslDCw%26bvm%3Dbv.113034660,d.d2s 3 21834
hr Bitcoin 3 44829
id Berkas:Bitcoin_screenshot_windows7.png 1 10002
id Bitcoin 5 127135
is Bitcoin 1 10789
it Bitcoin 12 309789
nl Bitcoin 3 47877
no Bitcoin 1 22836
pl Bitcoin 7 184842
pl Bitcoin%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%A0%C3%A2%E2%82%AC%E2%84%A2%C3%83%C6%92%C3%A2%E2%82%AC_%C3%83%C2%A2%C3%A2%E2%80%9A%C2%AC%C3%A2%E2%80%9E%C2%A2%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%9A%C3%82%C2%A2%C3%83%C6%92%C3%82%C2%A2%C3%83%C2%A2%C3%A2%E2%80%9A%C2%AC%C3%85%C2%A1%C3%83%E2%80%9A%C3%82%C2%AC%C3%83%C6%92%C3%A2%E2%82%AC%C2%A6%C3%83%E2%80%9A%C3%82%C2%A1%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%A0%C3%A2%E2%82%AC%E2%84%A2%C3%83%C6%92%C3%82%C2%A2%C3%83%C2%A2%C3%A2%E2%82%AC%C5%A1%C3%82%C2%AC%C3%83%E2%80%A6%C3%82%C2%A1%C3%83%C6%92%C3%86%E2%80%99%C3%83%C2%A2%C3%A2%E2%80%9A%C2%AC%C3%85%C2%A1%C3%83%C6%92%C3%A2%E2%82%AC%C5%A1%C3%83%E2%80%9A%C3%82 2 13856
pt Bitcoin 22 1045237
ru Bitcoin 1 85419
simple Talk:Bitcoin 1 5739
sk Bitcoin 1 12543
sr %D0%9F%D0%BE%D1%81%D0%B5%D0%B1%D0%BD%D0%BE:GlobalUsage/Bitcoin_logo.svg 1 7410
tr Bitcoin 3 44270
vi Bitcoin 3 111123
ca Bitcoin 1 34309
ca Fitxer:BitcoinSign.svg 1 10213
ca Fitxer:Bitcoin_logo.svg 1 11257
commons.m Category:Bitcoin_companies 1 7116
commons.m File%3ABitcoin_Block_Data.png 1 8809
commons.m File:Bitcoin-coins.jpg 1 4995
commons.m File:Bitcoin-heart-on-a-black-background.jpg 1 8109
commons.m File:Bitcoin.png 1 9336
commons.m File:Bitcoin_screenshot_windows7.png 1 10036
commons.m File:Bitcoin_wallet.png 1 5021
commons.m Special:RecentChangesLinked/File:Bitcoin_USB_rig_3_April_2014.ogv 1 6353
commons.m Special:WhatLinksHere/Category:Physical_Bitcoins 1 5310
cs Bitcoin 2 63078
de Bitcoin 10 842967
en Bitcoin 169 22691826
en Bitcoin_ATM 6 105100
en Bitcoin_Classic 4 57108
en Bitcoin_Fog 6 189414
en Bitcoin_Fog%27, 1 6618
en Bitcoin_Foundation 2 75963
en Bitcoin_Protocol 2 24114
en Bitcoin_XT 5 104615
en Bitcoin_fog 1 24784
en Bitcoin_network 4 168266
en Bitcoin_protocol 3 217017
en Bitcoins 1 125254
en Category:Bitcoin_exchanges 1 7518
en File%3ABitcoin-coins.jpg 1 5037
en File:Bitcoin_October_2013.png 1 8090
en File:Bitcoin_Transaction_Visual.svg 1 8667
en History_of_Bitcoin 14 1323305
en Kraken_Bitcoin_Exchange 1 23113
en LocalBitcoins 3 57720
en LocalBitcoins%27, 1 6617
en Protocol_of_Bitcoin 1 24133
en Special:WhatLinksHere/Bitcoin_Group 1 6100
en Talk:Bitcoin/Archive_10 2 153848
en Talk:Bitcoin/Archive_13 2 173308
en Talk:Bitcoin_network 1 69241
en Talk:Legality_of_Bitcoin_by_country 4 240730
es Bitcoin 25 1228236
fi Bitcoin 2 30948
fr Bitcoin 9 464922
fr Bitcoins 1 51924
hu Bitcoin 1 0
id Bitcoin 4 101720
is Bitcoin 1 10789
it Bitcoin 4 84489
it Speciale:PuntanoQui/File:Bitcoin_logo.svg 1 5643
ja Bitcoin 1 57624
ko %C3%83%C2%AD%C3%85%E2%80%99%C3%85%E2%80%99%C3%83%C2%AC%C3%82%C2%9D%C3%82%C2%BC:Bitcoin_logo.svg 1 6926
lv Bitcoin 1 14537
nl Bitcoin 5 79795
pl Bitcoin%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%A0%C3%A2%E2%82%AC%E2%84%A2%C3%83%C6%92%C3%A2%E2%82%AC_%C3%83%C2%A2%C3%A2%E2%80%9A%C2%AC%C3%A2%E2%80%9E%C2%A2%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%9A%C3%82%C2%A2%C3%83%C6%92%C3%82%C2%A2%C3%83%C2%A2%C3%A2%E2%80%9A%C2%AC%C3%85%C2%A1%C3%83%E2%80%9A%C3%82%C2%AC%C3%83%C6%92%C3%A2%E2%82%AC%C2%A6%C3%83%E2%80%9A%C3%82%C2%A1%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%A0%C3%A2%E2%82%AC%E2%84%A2%C3%83%C6%92%C3%82%C2%A2%C3%83%C2%A2%C3%A2%E2%82%AC%C5%A1%C3%82%C2%AC%C3%83%E2%80%A6%C3%82%C2%A1%C3%83%C6%92%C3%86%E2%80%99%C3%83%C2%A2%C3%A2%E2%80%9A%C2%AC%C3%85%C2%A1%C3%83%C6%92%C3%A2%E2%82%AC%C5%A1%C3%83%E2%80%9A%C3%82 2 13856
pt Bitcoin 13 715179
pt Ficheiro:Bitcoin_logo.svg 1 11736
ru Bitcoin 3 775576
sh Bitcoin 1 12020
sv Bitcoin 1 22168
tr Bitcoin 1 14752
vi Bitcoin 4 148166
~~~
