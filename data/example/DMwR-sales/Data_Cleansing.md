## Data Cleansing

### Removing transactions with both Value and Quantity missing
~~~
> nrow(sales)
[1] 401146

> detach(sales)

> sales <- sales[-which(is.na(sales$Quant) & is.na(sales$Val)),]
 
> attach(sales)
 
> nrow(sales)
[1] 400258
~~~

### Removing transactions from product "p2442" and "p2443"
~~~
> nrow(sales)
[1] 400258

> nrow(table(Prod))
[1] 4548

> nlevels(Prod)
[1] 4548


> detach(sales)
 
> sales <- sales[-which(sales$Prod %in% c("p2442", "p2443")),]

> sales$Prod <- factor(sales$Prod)

> attach(sales)


> nrow(sales)
[1] 400204
 
> nrow(table(Prod))
[1] 4546

> nlevels(Prod)
[1] 4546
