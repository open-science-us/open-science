# Sales

Transactions reported by salespeople of some company. These salespeople sell a set of products of the company, are free to set the selling price according their own policy and market, report their sales back to the company at the end of each month.

## Our Goal

Our goal is to help in the task of verifying the veracity of these reports given past experience of the company that has detected error and fraud attempts in these transaction reports. The help we provide will take the form of a ranking of the reports according to their probability of being fraudulent. This ranking will allow to allocate the limited inspection resources of the company to the reports that our system signals as being more \suspicious".

## Exploratory Data Analysis with R

### data source
~~~
> install.packages('DMwR')

> library(DMwR)

> data(sales)

> attach(sales)
~~~

### basic
~~~
> head(sales)

  ID Prod Quant   Val Insp
1 v1   p1   182  1665 unkn
2 v2   p1  3072  8780 unkn
3 v3   p1 20393 76990 unkn
4 v4   p1   112  1100 unkn
5 v3   p1  6164 20260 unkn
6 v5   p2   104  1155 unkn


> summary(sales)

       ID              Prod            Quant                Val             Insp       
 v431   : 10159   p1125  :  3923   Min.   :      100   Min.   :   1005   ok   : 14462  
 v54    :  6017   p3774  :  1824   1st Qu.:      107   1st Qu.:   1345   unkn :385414  
 v426   :  3902   p1437  :  1720   Median :      168   Median :   2675   fraud:  1270  
 v1679  :  3016   p1917  :  1702   Mean   :     8442   Mean   :  14617                 
 v1085  :  3001   p4089  :  1598   3rd Qu.:      738   3rd Qu.:   8680                 
 v1183  :  2642   p2742  :  1519   Max.   :473883883   Max.   :4642955                 
 (Other):372409   (Other):388860   NA's   :13842       NA's   :1182                    


> nlevels(ID)
[1] 6016

> nlevels(Prod)
[1] 4548


> length(which(is.na(sales$Quant) & is.na(sales$Val)))
[1] 888

> length(which(is.na(sales$Quant) & sales$Insp == 'ok'))
[1] 110

> length(which(is.na(sales$Val) & sales$Insp == 'ok'))
[1] 8


> length(which(is.na(sales$Quant) & is.na(sales$Val) & sales$Insp == 'ok'))
[1] 3

> sales[which(is.na(sales$Quant) & is.na(sales$Val) & sales$Insp == 'ok'), ]

         ID  Prod Quant Val Insp
6624   v709 p1125    NA  NA   ok
9808  v1109 p1462    NA  NA   ok
15414 v1158 p1910    NA  NA   ok


> table(sales$Insp) / nrow(sales) * 100 

       ok      unkn     fraud 
 3.605171 96.078236  0.316593 

> barplot(table(sales$ID), main="Transactions per salespeople", names.arg="", xlab="Salespeople", ylab="Amount", ylim=c(0,12000))

> barplot(table(sales$Prod), main="Transactions per product", names.arg="", xlab="Products", ylab="Amount", ylim=c(0,4000))
~~~

![sales_ID](sales_ID.png)
![sales_Prod](sales_Prod.png)





