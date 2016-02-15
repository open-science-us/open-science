## Overall
~~~
> attach(sales)

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
~~~
