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
~~~


### Inputing single missing values
~~~
> detach(sales)

> length(which(is.na(sales$Val)))
[1] 294

> length(which(is.na(sales$Quant)))
[1] 12900


> sales$Uprice <- sales$Val / sales$Quant

> tPrice <- tapply(sales[Insp != "fraud", "Uprice"], list(sales[Insp != "fraud", "Prod"]), median, na.rm=T)

> naQ <- which(is.na(sales$Quant))

> sales[naQ, 'Quant'] <- ceiling(sales[naQ, 'Val'] / tPrice[sales[naQ, "Prod"]])

> naV <- which(is.na(sales$Val))

> sales[naV, 'Val'] <- sales[naV, 'Quant'] * tPrice[sales[naV, 'Prod']]

> sales$Uprice <- sales$Val / sales$Quant


> attach(sales)

> length(which(is.na(Quant)))
[1] 0
 
> length(which(is.na(Val)))
[1] 0
~~~

### Saving the work
~~~
> setwd("/work/R/example")

> save(sales, file='salesClean.rdata')

> write.csv(sales, "salesClean.csv", row.names=TRUE)
~~~
