# [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)


## [Apache Commons Math 3.6 API](https://commons.apache.org/proper/commons-math/apidocs/org/apache/commons/math3/stat/inference/KolmogorovSmirnovTest.html)

## [KolmogorovSmirnovTest.java](https://commons.apache.org/proper/commons-math/jacoco/org.apache.commons.math3.stat.inference/KolmogorovSmirnovTest.java.html)


## Case One:  Fraud Detection

Carry out Kolmogorov-Smirnov test to compare the two distributions of unit prices in sales data for fraud detection


**Method 1 estimation method:** Call bootstrap to search for top N products for each of the products that has less than 20 transactions. 
**Method 2 kolmogorovSmirnovTest method:** Call kolmogorovSmirnovTest against top N products to find the one with the highest p-value for each of the products that has less than 20 transactions. 
 







