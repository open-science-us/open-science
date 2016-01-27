# [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)


## References

(1) [Apache Commons Math 3.6 API](https://commons.apache.org/proper/commons-math/apidocs/org/apache/commons/math3/stat/inference/KolmogorovSmirnovTest.html)

(2) [KolmogorovSmirnovTest.java](https://commons.apache.org/proper/commons-math/jacoco/org.apache.commons.math3.stat.inference/KolmogorovSmirnovTest.java.html)


## Case One:  Detecting Fraudulent Transactions


Section 4.2.3.2 (Few Transactions of Some Products) in Chapter 4 (Detecting Fraudulent Transactions) in the book [Data Mining with R] (http://www.amazon.com/Data-Mining-Learning-Knowledge-Discovery/dp/1439810184)

There are products with very few (< 20) transactions. For each of the products that has less than 20 transactions, search for the product with the most similar unit price distribution and use Kolmogorov-Smirnov test to check if the similarity is statistically significant.







