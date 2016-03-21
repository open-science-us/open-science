## n-gram using R

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


lngram1 <- ngram(ldomain, 1)
lngram2 <- ngram(ldomain, 2)
lngram4 <- ngram(ldomain, 4)
lngram5 <- ngram(ldomain, 5)
lngram345 <- ngram(ldomain, c(3,4,5))
~~~
