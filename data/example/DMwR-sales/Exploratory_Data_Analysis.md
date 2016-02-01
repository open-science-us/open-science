# Exploratory Data Analysis with R

## data source
~~~
> install.packages('DMwR')

> library(DMwR)

> data(sales)

> attach(sales)
~~~

## basic
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


## unit price
~~~
> sales$Uprice <- Val/Quant

> head(sales)

  ID Prod Quant   Val Insp    Uprice
1 v1   p1   182  1665 unkn  9.148352
2 v2   p1  3072  8780 unkn  2.858073
3 v3   p1 20393 76990 unkn  3.775315
4 v4   p1   112  1100 unkn  9.821429
5 v3   p1  6164 20260 unkn  3.286827
6 v5   p2   104  1155 unkn 11.105769

> summary(sales$Uprice)

    Min.  1st Qu.   Median     Mean  3rd Qu.     Max.     NA's 
    0.00     8.46    11.89    20.30    19.11 26460.00    14136 


> MUprice <- aggregate(sales$Uprice, list(Prod), median, na.rm=TRUE)

> head(MUprice)

  Group.1         x
1      p1 11.428571
2      p2 10.877863
3      p3 10.000000
4      p4  9.911243
5      p5 11.000000
6      p6 13.270677

> head(MUprice[order(MUprice$x),])

     Group.1          x
560     p560 0.01688455
559     p559 0.01884438
4195   p4195 0.03025914
601     p601 0.05522265
563     p563 0.05576406
561     p561 0.09115803

> head(MUprice[order(MUprice$x, decreasing=TRUE),])

     Group.1         x
3689   p3689 9204.1954
2453   p2453  456.0784
2452   p2452  329.3137
2456   p2456  304.8515
2459   p2459  283.8119
2451   p2451  262.2277

> tops <- sales[Prod %in% c("p560", "p3689"), c("Prod", "Uprice")]

> tops$Prod.f <- factor(tops$Prod)
 
> boxplot(Uprice ~ Prod.f, data=tops, ylab="Uprice", log="y")
~~~

![tops](tops.png)




