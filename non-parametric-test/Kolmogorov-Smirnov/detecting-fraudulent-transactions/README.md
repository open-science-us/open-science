# Case One:  Detecting Fraudulent Transactions


Section 4.2.3.2 (Few Transactions of Some Products) in Chapter 4 (Detecting Fraudulent Transactions) in the book [Data Mining with R] (http://www.amazon.com/Data-Mining-Learning-Knowledge-Discovery/dp/1439810184)

There are 985 products with very few (< 20) transactions. For each of such products, search for the product with the most similar unit price distribution and use Kolmogorov-Smirnov test to check if the similarity is statistically significant.  However, carrying out this task for all combinations of products would be computationally too demanding. Instead, the author searched for the product with the most similar median and IQR. Given this similar product and then carried out a Kolmogorov-Smirnov test between their respective unit price distributions, storing the results of this test. The author found similar products for 117 of them.

I reproduce the result using the R code provided by the author in the book. I also see an interesting thing that the author did not mention in the book. 113 of 117 products have product v559 and 4 of 117 products have product v6199 with the most similar unit price distribution. It is obviously wrong, compared with the visual inspection shown in Figure 4.4 inside the book.

I decide to choose an alternative solution: use the estimation method “bootstrap”, provided by [Apache Commons Math 3.6 API](https://commons.apache.org/proper/commons-math/apidocs/org/apache/commons/math3/stat/inference/KolmogorovSmirnovTest.html), to get top 15 similar ones quickly, then carry out the full Kolmogorov-Smirnov test to get the most similar one out of the top 15 ones. 358 out of 985 products are found.


## Test Environment

(1) Mac Air:  OS X v10.9.5 (Processor: 1.4GHz Intel Core i5, Memory: 4 GB 1600 MHz DDR3)

(2) Java version "1.8.0_66”, Java(TM) SE Runtime Environment (build 1.8.0_66-b17), Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)

(3) [Apache Spark](http://spark.apache.org/docs/latest/) v1.6.0

Built with Apache Commons Math v3.6, instead of v3.4.1, to use the estimation method “bootstrap”.

(4) [R-CRAN](https://cran.r-project.org) version 3.2.3 (2015-12-10)


## Results from R

(1) 117 products with < 20 transactions that have the most similar product that passes Kolmogorov-Smirnov test of unit price distribution.

~~~
> sum(similar[, "ks.p"] >= 0.9)
[1] 117
~~~

(2) 113 of 117 products have product v559 and 4 of 117 products have product v6199 with the most similar unit price distribution.
 
~~~
> table(similar[similar[, "ks.p"] >= 0.9, "Simil"])

 559 6199 
 113    4 
~~~




