## Data Preparation using R

### overall
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

> table(sampledga$subclass)

       alexa      opendns cryptolocker          goz       newgoz 
        4948           52         1667         1667         1666 
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

> lqgram3 <- qgrams(ldomain, q=3)

> class(lqgram3)
[1] "matrix"
 
> mode(lqgram3)
[1] "numeric"

> nrow(lqgram3)
[1] 1

> ncol(lqgram3)
[1] 7362

> lqgram3[1, head(order(-lqgram3), 10), drop=F]

   ing ter ine the lin ion est ent ers and
V1 161 138 130 113 111 106 103 102 100  93

> good <- c("facebook", "google", "youtube", "yahoo", "baidu", "wikipedia")

> getngram(lqgram3, good)

 facebook    google   youtube     yahoo     baidu wikipedia 
      125       309       122        25         9       178 


> lngram3 <- ngram(ldomain, 3)

> lngram3[1, head(order(-lngram3), 10), drop=F]

          ing      ter      ine      the      lin      ion      est    ent ers      and
[1,] 2.206826 2.139879 2.113943 2.053078 2.045323 2.025306 2.012837 2.0086   2 1.968483

> getngram(lngram3, good)

 facebook    google   youtube     yahoo     baidu wikipedia 
 7.263576  7.550393  6.674159  2.593286  0.698970  7.568363 

> bad <- c("hwenbesxjwrwa", "oovftsaempntpx", "uipgqhfrojbnjo", "igpjponmegrxjtr", "eoitadcdyaeqh", "bqadfgvmxmypkr")

> getngram(lngram3, bad)

  hwenbesxjwrwa  oovftsaempntpx  uipgqhfrojbnjo igpjponmegrxjtr   eoitadcdyaeqh  bqadfgvmxmypkr 
       2.681241        4.121560        2.949878        2.748188        3.763802        0.602060 
~~~

### dictionary matching
~~~
> wmatch(c("facebook", "oxfordlawtrove", "uipgqhfrojbnjo"))
[1] 1.0000000 1.0000000 0.4285714

> wmatch(good)
[1] 1.0000000 1.0000000 1.0000000 1.0000000 0.8000000 0.7777778
 
> wmatch(bad)
[1] 0.6923077 0.7142857 0.4285714 0.7333333 0.7692308 0.2142857
~~~

### all
~~~
> sampledga$gram3 <- getngram(lngram3, sampledga$domain)

> sampledga$entropy=entropy(sampledga$domain)

> sampledga$length=nchar(sampledga$domain)

> sampledga$dictionary <- wmatch(sampledga$domain)

> head(sampledga)

           host    domain tld class subclass  entropy length    gram3 dictionary
1    google.com    google com legit    alexa 1.918296      6 7.550393  1.0000000
2  facebook.com  facebook com legit    alexa 2.750000      8 7.263576  1.0000000
3   youtube.com   youtube com legit    alexa 2.521641      7 6.674159  1.0000000
4     yahoo.com     yahoo com legit    alexa 1.921928      5 2.593286  1.0000000
5     baidu.com     baidu com legit    alexa 2.321928      5 0.698970  0.8000000
6 wikipedia.org wikipedia org legit    alexa 2.641604      9 7.568363  0.7777778

> sampledga[c(sample(5000, 3), sample(5000, 3)+5000),]

                                  host                      domain tld class subclass  entropy length     gram3 dictionary
25                          tumblr.com                      tumblr com legit    alexa 2.584963      6  2.209515  0.5000000
534206                        senaf.it                       senaf  it legit    alexa 2.321928      5  2.518514  1.0000000
465220                    freeradio.cz                   freeradio  cz legit    alexa 2.725481      9 10.315485  1.0000000
44580    o3kxkf19ttvw1vw801m4fy09h.org   o3kxkf19ttvw1vw801m4fy09h org   dga   newgoz 3.893661     25  0.000000  0.4000000
51882  1ksosm5sralfu1epvx1s1bm3s48.org 1ksosm5sralfu1epvx1s1bm3s48 org   dga   newgoz 3.954530     27  5.153998  0.5925926
51092    1de526ck9zea73pu3hjo6op8r.net   1de526ck9zea73pu3hjo6op8r net   dga   newgoz 4.243856     25  0.000000  0.5200000
~~~

### feature visualization
~~~
> install.packages('GGally')

> library(GGally)

> library(ggplot2)
  
> gg <- ggpairs(sampledga, 
        columns = c("entropy", "length", "gram3", "dictionary", "class"),
        mapping = aes(color = class),
        lower = list(continuous = wrap('smooth', alpha = 0.5)),
        upper = list(continuous = wrap('density', alpha = 0.5), combo = wrap('box', alpha = 0.5)),
        axisLabels = 'show'
  )
  
> for(i in 1:gg$nrow) {
    for(j in 1:gg$ncol) {
      gg[i,j] <- gg[i,j] + scale_fill_manual(values=c("green", "red")) + scale_color_manual(values=c("green", "red"))  
    }
  }
  
> print(gg)
~~~
![features](images/features.png)
