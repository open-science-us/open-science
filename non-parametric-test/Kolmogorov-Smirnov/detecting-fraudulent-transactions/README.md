# Case One:  Detecting Fraudulent Transactions


Section 4.2.3.2 (Few Transactions of Some Products) in Chapter 4 (Detecting Fraudulent Transactions) in the book [Data Mining with R] (http://www.amazon.com/Data-Mining-Learning-Knowledge-Discovery/dp/1439810184)

There are products with very few (< 20) transactions. For each of the products that has less than 20 transactions, we will search for the product with the most similar unit price distribution and then use a Kolmogorov-Smirnov test to check if the similarity is statistically signicant.

Carrying out this task for all combinations of products would be computationally too demanding. Instead, the author searched for the product with the most similar median and IQR. Given this similar product and then carried out a Kolmogorov-Smirnov test between their respective unit price distributions, storing the results of this test. Only 117 out of 985 products with less than 20 transactions were found.

I use an alternative solution. Use an estimation method to get top 15 similar ones quickly, then carried out the full Kolmogorov-Smirnov test to get the most similar one out of the top 15 ones. 358 out of 985 products are found.

