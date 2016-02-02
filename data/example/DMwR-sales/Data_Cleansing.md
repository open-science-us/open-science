## Data Cleansing

### Remove product "p2442" and "p2443"
~~~
> nrow(sales)
[1] 401146

> nrow(table(Prod))
[1] 4548

> nlevels(Prod)
[1] 4548


> detach(sales)
 
> sales <- sales[-which(sales$Prod %in% c("p2442", "p2443")),]

> sales$Prod <- factor(sales$Prod)

> attach(sales)


> nrow(sales)
[1] 401092
 
> nrow(table(Prod))
[1] 4546

> nlevels(Prod)
[1] 4546
