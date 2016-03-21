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


> test <- sampledga[-trainindex, ]

> nrow(test)
[1] 2498
~~~
