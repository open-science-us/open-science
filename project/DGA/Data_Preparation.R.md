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

lngram1 <- ngram(ldomain, 1)
lngram2 <- ngram(ldomain, 2)
lngram3 <- ngram(ldomain, 3)
lngram4 <- ngram(ldomain, 4)
lngram5 <- ngram(ldomain, 5)
lngram345 <- ngram(ldomain, c(3,4,5))
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
> sampledga$entropy=entropy(sampledga$domain)

> sampledga$length=nchar(sampledga$domain)

> sampledga$dictionary <- wmatch(sampledga$domain)

sampledga$gram1 <- getngram(lngram1, sampledga$domain)
sampledga$gram2 <- getngram(lngram2, sampledga$domain)
sampledga$gram3 <- getngram(lngram3, sampledga$domain)
sampledga$gram4 <- getngram(lngram4, sampledga$domain)
sampledga$gram5 <- getngram(lngram5, sampledga$domain)
sampledga$gram345 <- getngram(lngram345, sampledga$domain)

> head(sampledga)

           host    domain tld class subclass  entropy length dictionary    gram1     gram2    gram3     gram4     gram5   gram345
1    google.com    google com legit    alexa 1.918296      6  1.0000000 20.45111 11.552775 7.550393 5.5899686 3.7266457 16.867008
2  facebook.com  facebook com legit    alexa 2.750000      8  1.0000000 26.66997 14.916048 7.263576 2.8115750 0.9030900 10.978241
3   youtube.com   youtube com legit    alexa 2.521641      7  1.0000000 23.07979 12.472083 6.674159 2.5105450 0.0000000  9.184704
4     yahoo.com     yahoo com legit    alexa 1.921928      5  1.0000000 16.77977  8.271564 2.593286 0.9542425 0.4771213  4.024650
5     baidu.com     baidu com legit    alexa 2.321928      5  0.8000000 16.66165  8.393773 0.698970 0.0000000 0.0000000  0.698970
6 wikipedia.org wikipedia org legit    alexa 2.641604      9  0.7777778 30.19710 17.108382 7.568363 3.1122698 0.4771213 11.157754

> sampledga[c(sample(5000, 3), sample(5000, 3)+5000),]

                                   host                        domain          tld class     subclass  entropy length dictionary    gram1     gram2      gram3    gram4    gram5    gram345
437414 carriescornerishere.blogspot.com           carriescornerishere blogspot.com legit        alexa 2.900052     19  1.0000000 66.75973 43.894913 24.2053278 8.077147 2.158362 34.4408377
321616                   helpmefind.com                    helpmefind          com legit        alexa 3.121928     10  1.0000000 33.40558 19.278485  7.7257379 2.472756 0.000000 10.1984943
390                           optmd.com                         optmd          com legit        alexa 2.321928      5  0.6000000 16.63749  6.473498  0.9542425 0.000000 0.000000  0.9542425
36122  gyuklyxgmgqemlbfakzofprclztzp.ru gyuklyxgmgqemlbfakzofprclztzp           ru   dga          goz 4.021268     29  0.4482759 89.36610 33.025804  0.9542425 0.000000 0.000000  0.9542425
50980   pik8ue1817ka514e4u4m1j6xguh.net   pik8ue1817ka514e4u4m1j6xguh          net   dga       newgoz 3.884155     27  0.5555556 70.02843 14.415488  0.0000000 0.000000 0.000000  0.0000000
32630                wmgsfxcexscrqhh.ru               wmgsfxcexscrqhh           ru   dga cryptolocker 3.373557     15  0.2000000 45.98314 16.253728  1.1461280 0.000000 0.000000  1.1461280
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
      gg[i,j] <- gg[i,j] + scale_fill_manual(values=c("#00CC00", "#CC0000")) + scale_color_manual(values=c("#00CC00", "#CC0000"))  
    }
  }
  
> print(gg)
~~~
![features](images/features.png)
