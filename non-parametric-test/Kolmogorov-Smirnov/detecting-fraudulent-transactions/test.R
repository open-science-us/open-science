// package

install.packages('DMwR')


// data

library(DMwR)

data(sales)

attach(sales)


// data - adding unit price

sales$Uprice <- sales$Val / sales$Quant



// data - removing dual missing values

detach(sales)

sales <- sales[-which(is.na(sales$Quant) & is.na(sales$Val)),]

attach(sales)


// data - removing  "p2442" and "p2443”, all of their transactions that do not have quantity

detach(sales)

sales <- sales[!sales$Prod %in% c("p2442", "p2443"), ]

sales$Prod <- factor(sales$Prod)

attach(sales)


// data - inputiing single missing value

sales$Uprice <- sales$Val / sales$Quant

tPrice <- tapply(sales[sales$Insp != "fraud", "Uprice"], list(sales[sales$Insp != "fraud", "Prod"]), median, na.rm=T)

noQuant <- which(is.na(sales$Quant))

sales[noQuant,'Quant'] <- ceiling(sales[noQuant, 'Val'] / tPrice[sales[noQuant,"Prod"]])

noVal <- which(is.na(sales$Val))

sales[noVal, 'Val'] <- sales[noVal,'Quant'] * tPrice[sales[noVal, 'Prod']]


// data - saving clean data to a csv file

sales$Uprice <- sales$Val/sales$Quant

setwd("/work/R/example")

write.csv(sales, "salesClean.csv", row.names=TRUE)





