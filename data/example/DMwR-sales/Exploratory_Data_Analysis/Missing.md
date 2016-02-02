## Missing Data

### Overall
~~~
> table(sales$Insp)

    ok   unkn  fraud 
 14462 385414   1270 

> table(sales$Insp) / nrow(sales) * 100 

       ok      unkn     fraud 
 3.605171 96.078236  0.316593 
~~~

### Dual Unknown Values
~~~
> length(which(is.na(sales$Quant) & is.na(sales$Val)))
[1] 888

> head(sales[which(is.na(sales$Quant) & is.na(sales$Val)),])
        ID  Prod Quant Val Insp
3475   v29  p808    NA  NA unkn
4433  v453  p921    NA  NA unkn
5393  v431 p1035    NA  NA unkn
5503  v431    p1    NA  NA unkn
5505  v431    p1    NA  NA unkn
5913 v1039 p1101    NA  NA unkn

> length(which(is.na(sales$Quant) & is.na(sales$Val) & sales$Insp == 'ok'))
[1] 3

> sales[which(is.na(sales$Quant) & is.na(sales$Val) & sales$Insp == 'ok'), ]

         ID  Prod Quant Val Insp
6624   v709 p1125    NA  NA   ok
9808  v1109 p1462    NA  NA   ok
15414 v1158 p1910    NA  NA   ok

> length(which(is.na(sales$Quant) & is.na(sales$Val) & sales$Insp == 'fraud'))
[1] 0

> dualByID <- 100 * table(sales[which(is.na(Quant) & is.na(Val)),'ID']) / table(ID)

> dualByID[order(dualByID, decreasing=T)[1:10]]

    v1237     v4254     v4038     v5248     v3666     v4433     v4170     v4926     v4664     v4642 
13.793103  9.523810  8.333333  8.333333  6.666667  6.250000  5.555556  5.555556  5.494505  4.761905 


> dualByProd <- 100 * table(sales[which(is.na(Quant) & is.na(Val)),'Prod']) / table(Prod)

> dualByProd[order(dualByProd, decreasing=T)[1:10]]

   p2689    p2675    p4061    p2780    p4351    p2686    p2707    p2690    p2691    p2670 
39.28571 35.41667 25.00000 22.72727 18.18182 16.66667 14.28571 14.08451 12.90323 12.76596 

~~~



### Quantity Missing
~~~
> length(which(is.na(sales$Quant) & sales$Insp == 'ok'))
[1] 110

> head(sales[which(is.na(sales$Quant) & sales$Insp == 'ok'),])
        ID  Prod Quant  Val Insp
3459  v614  p807    NA 1010   ok
6450 v1295 p1125    NA 1025   ok
6516  v950 p1125    NA 1240   ok
6520 v1158 p1125    NA 1005   ok
6536   v10 p1125    NA 1445   ok
6624  v709 p1125    NA   NA   ok
~~~

### Value Missing
~~~
> length(which(is.na(sales$Val) & sales$Insp == 'ok'))
[1] 8

> sales[which(is.na(sales$Val) & sales$Insp == 'ok'),]
         ID  Prod Quant Val Insp
6365  v1039 p1125   100  NA   ok
6624   v709 p1125    NA  NA   ok
9346   v796 p1436   100  NA   ok
9475  v1043 p1437   106  NA   ok
9804  v1039 p1462   100  NA   ok
9808  v1109 p1462    NA  NA   ok
15414 v1158 p1910    NA  NA   ok
19853 v1958 p2272   101  NA   ok

~~~
