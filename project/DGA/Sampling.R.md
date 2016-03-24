## Stratified Random Sampling using R

~~~
> library('caret')

> set.seed(1492)


> trainindex <- createDataPartition(sampledga$subclass, p=0.75, list=F)

> fields <- c("class", "entropy", "length",  "dictionary", "gram1", "gram2", "gram3", "gram4", "gram5", "gram345")

> traindga <- sampledga[trainindex, fields]

> nrow(traindga)
[1] 7502

> class(traindga)
[1] "data.frame"

> mode(traindga)
[1] "list"

> head(traindga)

  class  entropy length dictionary    gram1     gram2    gram3     gram4     gram5   gram345
1 legit 1.918296      6  1.0000000 20.45111 11.552775 7.550393 5.5899686 3.7266457 16.867008
2 legit 2.750000      8  1.0000000 26.66997 14.916048 7.263576 2.8115750 0.9030900 10.978241
4 legit 1.921928      5  1.0000000 16.77977  8.271564 2.593286 0.9542425 0.4771213  4.024650
6 legit 2.641604      9  0.7777778 30.19710 17.108382 7.568363 3.1122698 0.4771213 11.157754
8 legit 2.251629      6  1.0000000 20.08431 11.166920 5.565546 3.4683473 2.2922561 11.326149
9 legit 2.000000      4  1.0000000 13.44665  6.930911 3.350248 1.3802112 0.0000000  4.730459

> tail(traindga)

      class  entropy length dictionary    gram1     gram2     gram3 gram4 gram5   gram345
43523   dga 4.103910     26  0.3461538 73.53179 17.131297 0.7781513     0     0 0.7781513
47408   dga 3.950064     26  0.5384615 68.78791 12.097082 0.0000000     0     0 0.0000000
47771   dga 4.103910     26  0.4615385 68.53945 11.714118 0.0000000     0     0 0.0000000
50826   dga 4.133661     25  0.4000000 63.44397  7.971196 0.0000000     0     0 0.0000000
52350   dga 3.833270     25  0.3200000 72.61882 20.907838 1.3010300     0     0 1.3010300
45591   dga 4.163856     25  0.2800000 71.77578 19.488250 0.6020600     0     0 0.6020600

> table(sampledga$subclass)

       alexa      opendns cryptolocker          goz       newgoz 
        4948           52         1667         1667         1666 

> table(sampledga$subclass[trainindex])

       alexa      opendns cryptolocker          goz       newgoz 
        3711           39         1251         1251         1250 


> levels(traindga$class) <- c("dga", "legit")


> testdga <- sampledga[-trainindex, ]

> nrow(testdga)
[1] 2498

> head(testdga)

          host  domain   tld class subclass  entropy length dictionary     gram1      gram2    gram3     gram4     gram5   gram345
3  youtube.com youtube   com legit    alexa 2.521641      7        1.0 23.079787 12.4720826 6.674159 2.5105450 0.0000000  9.184704
5    baidu.com   baidu   com legit    alexa 2.321928      5        0.8 16.661646  8.3937731 0.698970 0.0000000 0.0000000  0.698970
7       qq.com      qq   com legit    alexa 0.000000      2        0.0  4.008643  0.4771213 0.000000 0.0000000 0.0000000  0.000000
10 twitter.com twitter   com legit    alexa 2.128085      7        1.0 24.062252 13.5336424 7.042795 3.4683473 2.0000000 12.511143
18 yahoo.co.jp   yahoo co.jp legit    alexa 1.921928      5        1.0 16.779775  8.2715637 2.593286 0.9542425 0.4771213  4.024650
20    ebay.com    ebay   com legit    alexa 2.000000      4        1.0 13.343090  6.4331624 2.477121 1.0413927 0.0000000  3.518514

> tail(testdga)

                                  host                       domain tld class subclass  entropy length dictionary    gram1    gram2     gram3 gram4 gram5   gram345
49076   1vdcdgqz8ysmh16uwzko7abt1e.net   1vdcdgqz8ysmh16uwzko7abt1e net   dga   newgoz 4.363713     26  0.5384615 73.06997 15.15001 0.4771213     0     0 0.4771213
49589  1cg1dg610ku0wsrdryf61m1wiv4.com  1cg1dg610ku0wsrdryf61m1wiv4 com   dga   newgoz 3.880456     27  0.5555556 73.30296 18.87960 0.0000000     0     0 0.0000000
49698   1wedd0q9d1vk1l8vit01ujy9gr.org   1wedd0q9d1vk1l8vit01ujy9gr org   dga   newgoz 3.979098     26  0.5000000 69.22053 16.69131 1.6232493     0     0 1.6232493
43714 19g6afw1xzq6sd1a6ai5m1hukls7.net 19g6afw1xzq6sd1a6ai5m1hukls7 net   dga   newgoz 4.110577     28  0.4642857 74.75867 12.57807 0.4771213     0     0 0.4771213
52577    4bh34b1dfu4hxvkicz1p7858e.com    4bh34b1dfu4hxvkicz1p7858e com   dga   newgoz 4.133661     25  0.4000000 64.58371 12.67118 0.6020600     0     0 0.6020600
51407    9hw0nq1p9binuc6jrifi1noiu.biz    9hw0nq1p9binuc6jrifi1noiu biz   dga   newgoz 3.893661     25  0.6400000 71.62919 21.67631 3.6488477     0     0 3.6488477


> levels(testdga$class) <- c("dga", "legit")


> fields2 <- c("class", "length",  "dictionary", "gram345")

> traindga2 <- sampledga[trainindex, fields2]

> head(traindga2)

  class length dictionary   gram345
1 legit      6  1.0000000 16.867008
2 legit      8  1.0000000 10.978241
4 legit      5  1.0000000  4.024650
6 legit      9  0.7777778 11.157754
8 legit      6  1.0000000 11.326149
9 legit      4  1.0000000  4.730459
 
> tail(traindga2)

      class length dictionary   gram345
43523   dga     26  0.3461538 0.7781513
47408   dga     26  0.5384615 0.0000000
47771   dga     26  0.4615385 0.0000000
50826   dga     25  0.4000000 0.0000000
52350   dga     25  0.3200000 1.3010300
45591   dga     25  0.2800000 0.6020600

> levels(traindga2$class) <- c("dga", "legit")
~~~
