## Salespeople
~~~
> barplot(table(sales$ID), main="Transactions per Salespeople", names.arg="", xlab="Salespeople", ylab="Transactions", ylim=c(0,12000))
~~~
![sales_ID](images/sales_ID.png)

~~~
> valueByID <- aggregate(Val, list(ID), sum, na.rm=TRUE)

> head(valueByID)

  Group.1       x
1      v1  917030
2      v2 1090375
3      v3  517490
4      v4  728880
5      v5   59050
6      v6 1164325

> plot(log(valueByID$x) ~ valueByID$Group.1, main="Sales per Salespeople", names.arg="", xlab="Salespeople", ylab="Log(Sales)")
~~~
![sales](images/sales.png)

~~~
> valueByID[order(valueByID$x, decreasing=TRUE)[1:10],]

     Group.1         x
427     v431 211489170
54       v54 139322315
19       v19  71983200
4497   v4520  64398195
949     v955  63182215
1431   v1437  50013195
3882   v3901  48769945
354     v356  42131925
5050   v5086  41845760
743     v749  39526285

> topIDs <- valueByID[order(valueByID$x, decreasing=TRUE)[1:10], "Group.1"]

> topSalesByID <- sales[ID %in% topIDs, c("ID", "Prod", "Val")]

> topSalesByID$ID.f <- factor(topSalesByID$ID, topIDs)

> boxplot(Val ~ ID.f, data= topSalesByID, main="Transaction Values of 10 Top Salespeople", xlab="Salespeople", ylab="Log(Transaction Value)", log="y")
~~~
![top_sales](images/top_sales.png)

~~~
> topSalesByIDProd <- aggregate(topSalesByID$Val, list(topSalesByID$ID, topSalesByID$Prod), sum, na.rm=TRUE)

> head(topSalesByIDProd)

  Group.1 Group.2       x
1    v431      p1   60720
2    v749      p1  475740
3    v431      p3   10720
4    v431      p4       0
5    v431      p5    1760
6     v54     p16 6032990

> topSalesByIDProd$Group.1 <- factor(topSalesByIDProd$Group.1, topIDs)

> boxplot(log(x) ~ Group.1, data=topSalesByIDProd, main="Product Sales of 10 Top Salespeople", xlab="Salespeople", ylab="Log(Product Sales)")
~~~
![top_sales_product](images/top_sales_product.png)

~~~
> head(valueByID[order(valueByID$x),])

     Group.1    x
3342   v3355 1050
6015   v6069 1080
5828   v5876 1115
6004   v6058 1115
4492   v4515 1125
4315   v4337 1130

> bottomIDs <- valueByID[order(valueByID$x)[1:100], "Group.1"]

> bottomSalesByID <- sales[ID %in% bottomIDs, c("ID", "Prod", "Val")]

> bottomSalesByID$ID.f <- factor(bottomSalesByID$ID, bottomIDs)

> boxplot(Val ~ ID.f, data= bottomSalesByID, main="Transaction Values of 100 Bottom Salespeople", xlab="Salespeople", ylab="Transaction Value")
~~~
![bottom_sales](images/bottom_sales.png)

~~~
# Top 100 Salespeople account for 38% income

> sum(valueByID[order(valueByID$x, decreasing=T)[1:100], 2]) / sum(Val, na.rm=T) * 100
[1] 38.33277

# Bottom 2000 Salespeople account for less than 2% income

> sum(valueByID[order(valueByID $x, decreasing=F)[1:2000], 2]) / sum(Val, na.rm=T) * 100
[1] 1.988716
~~~
