## Data Preparation using R

### Overall
~~~
> library(dga)

> data(sampledga)

> head(sampledga, 5)

          host   domain tld class subclass
1   google.com   google com legit    alexa
2 facebook.com facebook com legit    alexa
3  youtube.com  youtube com legit    alexa
4    yahoo.com    yahoo com legit    alexa
5    baidu.com    baidu com legit    alexa

> tail(sampledga, 5)

                                host                     domain tld class subclass
47771 r3o3mt1q7qhld1mp4g2akzqs37.biz r3o3mt1q7qhld1mp4g2akzqs37 biz   dga   newgoz
50826  b05q9rw9lv1d1aq5po08iyjn5.org  b05q9rw9lv1d1aq5po08iyjn5 org   dga   newgoz
52350  sgem711uuk2vmyl1qlrdymhvl.org  sgem711uuk2vmyl1qlrdymhvl org   dga   newgoz
45591  ozhujl16ayo6crwwdf7fxskdk.org  ozhujl16ayo6crwwdf7fxskdk org   dga   newgoz
51407  9hw0nq1p9binuc6jrifi1noiu.biz  9hw0nq1p9binuc6jrifi1noiu biz   dga   newgoz

> sampledga[sample(which(sampledga$subclass=="opendns"), 5), ]

                           host                domain   tld class subclass
980482       newburylibrary.net        newburylibrary   net legit  opendns
973900 dncvirtualsolutions14.us dncvirtualsolutions14    us legit  opendns
978481     cleansebyclare.co.uk        cleansebyclare co.uk legit  opendns
985590     hallhealthcenter.com      hallhealthcenter   com legit  opendns
984832              dewmate.com               dewmate   com legit  opendns

> sampledga[sample(which(sampledga$subclass=="cryptolocker"), 5), ]

                    host          domain tld class     subclass
14920  wlcspnpwiencec.ru  wlcspnpwiencec  ru   dga cryptolocker
14325    hdlyjxohahdq.ru    hdlyjxohahdq  ru   dga cryptolocker
33394 wiuhegvgxbpaany.ru wiuhegvgxbpaany  ru   dga cryptolocker
30721  vifgurkyjepqju.ru  vifgurkyjepqju  ru   dga cryptolocker
15149    hqmvumpdumrc.ru    hqmvumpdumrc  ru   dga cryptolocker
~~~

### n-gram
~~~
> install.packages('stringdist')

> library(stringdist)

> qgrams("facebook", q=3)

   fac ook ace ceb ebo boo
V1   1   1   1   1   1   1

> qgrams("sandbandcandy", q=3)

   san and ndb ndc ndy dba dca ban can
V1   1   3   1   1   1   1   1   1   1

> qgrams("kykwdvibps", q=3)

   kyk ykw wdv vib kwd dvi ibp bps
V1   1   1   1   1   1   1   1   1


> ldomain <- sampledga$domain[sampledga$class=="legit"]

> l3gram <- qgrams(ldomain, q=3)

> class(l3gram)
[1] "matrix"
 
> mode(l3gram)
[1] "numeric"

> nrow(l3gram)
[1] 1

> ncol(l3gram)
[1] 7362

> l3gram[1, head(order(-l3gram), 10), drop=F]

   ing ter ine the lin ion est ent ers and
V1 161 138 130 113 111 106 103 102 100  93
~~~
