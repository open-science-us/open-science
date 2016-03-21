## Stratified Random Sampling using R

~~~
> install.packages('caret')

> library('caret')

> set.seed(1492)

> trainindex <- createDataPartition(sampledga$subclass, p=0.75, list=F)

> fields <- c("class", "entropy", "length",  "dictionary", "gram1", "gram2", "gram3", "gram4", "gram5", "gram345")

> train <- sampledga[trainindex, fields]

> nrow(train)
[1] 7502

> class(train)
[1] "data.frame"

> mode(train)
[1] "list"

> head(train)

  class  entropy length dictionary     gram1      gram2    gram3     gram4     gram5   gram345
1 legit 1.918296      6        1.0 20.451106 11.5527755 7.550393 5.5899686 3.7266457 16.867008
2 legit 2.750000      8        1.0 26.669971 14.9160480 7.263576 2.8115750 0.9030900 10.978241
3 legit 2.521641      7        1.0 23.079787 12.4720826 6.674159 2.5105450 0.0000000  9.184704
4 legit 1.921928      5        1.0 16.779775  8.2715637 2.593286 0.9542425 0.4771213  4.024650
5 legit 2.321928      5        0.8 16.661646  8.3937731 0.698970 0.0000000 0.0000000  0.698970
7 legit 0.000000      2        0.0  4.008643  0.4771213 0.000000 0.0000000 0.0000000  0.000000

> tail(train)

      class  entropy length dictionary    gram1    gram2    gram3 gram4 gram5  gram345
52551   dga 3.970176     24  0.4166667 70.41330 24.27058 2.149219     0     0 2.149219
52577   dga 4.133661     25  0.4000000 64.58371 12.67118 0.602060     0     0 0.602060
47771   dga 4.103910     26  0.4615385 68.53945 11.71412 0.000000     0     0 0.000000
52350   dga 3.833270     25  0.3200000 72.61882 20.90784 1.301030     0     0 1.301030
45591   dga 4.163856     25  0.2800000 71.77578 19.48825 0.602060     0     0 0.602060
51407   dga 3.893661     25  0.6400000 71.62919 21.67631 3.648848     0     0 3.648848

> summary(sampledga$subclass)

       alexa      opendns cryptolocker          goz       newgoz 
        4948           52         1667         1667         1666 

> summary(sampledga$subclass[trainindex])

       alexa      opendns cryptolocker          goz       newgoz 
        3711           39         1251         1251         1250 


> test <- sampledga[-trainindex, ]

> nrow(test)
[1] 2498

> head(test)

            host    domain   tld class subclass  entropy length dictionary     gram1     gram2    gram3     gram4     gram5   gram345
6  wikipedia.org wikipedia   org legit    alexa 2.641604      9  0.7777778 30.197104 17.108382 7.568363 3.1122698 0.4771213 11.157754
18   yahoo.co.jp     yahoo co.jp legit    alexa 1.921928      5  1.0000000 16.779775  8.271564 2.593286 0.9542425 0.4771213  4.024650
21     yandex.ru    yandex    ru legit    alexa 2.584963      6  1.0000000 19.437571 11.571913 5.693086 2.4983106 1.2041200  9.395517
23        vk.com        vk   com legit    alexa 1.000000      2  0.0000000  5.751568  0.903090 0.000000 0.0000000 0.0000000  0.000000
27     weibo.com     weibo   com legit    alexa 2.321928      5  1.0000000 16.714800  8.026804 1.431364 0.0000000 0.0000000  1.431364
32     tmall.com     tmall   com legit    alexa 1.921928      5  1.0000000 17.112269  8.966795 3.933487 0.7781513 0.0000000  4.711639

> tail(test)

                                  host                       domain tld class subclass  entropy length dictionary    gram1     gram2     gram3 gram4 gram5   gram345
42148 1kep5tv1a8b3gs18ixqu21w61uo0.net 1kep5tv1a8b3gs18ixqu21w61uo0 net   dga   newgoz 4.249868     28  0.5357143 73.26023 13.738931 0.0000000     0     0 0.0000000
49698   1wedd0q9d1vk1l8vit01ujy9gr.org   1wedd0q9d1vk1l8vit01ujy9gr org   dga   newgoz 3.979098     26  0.5000000 69.22053 16.691313 1.6232493     0     0 1.6232493
43523   oxtw5d1vn9afn1qs6zadu1gfbd.biz   oxtw5d1vn9afn1qs6zadu1gfbd biz   dga   newgoz 4.103910     26  0.3461538 73.53179 17.131297 0.7781513     0     0 0.7781513
43714 19g6afw1xzq6sd1a6ai5m1hukls7.net 19g6afw1xzq6sd1a6ai5m1hukls7 net   dga   newgoz 4.110577     28  0.4642857 74.75867 12.578069 0.4771213     0     0 0.4771213
47408   c4li3j1b88jcs80jzvb1voekfz.net   c4li3j1b88jcs80jzvb1voekfz net   dga   newgoz 3.950064     26  0.5384615 68.78791 12.097082 0.0000000     0     0 0.0000000
50826    b05q9rw9lv1d1aq5po08iyjn5.org    b05q9rw9lv1d1aq5po08iyjn5 org   dga   newgoz 4.133661     25  0.4000000 63.44397  7.971196 0.0000000     0     0 0.0000000
~~~
