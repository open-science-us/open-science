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


// data - inputing single missing values

sales$Uprice <- sales$Val / sales$Quant

tPrice <- tapply(sales[sales$Insp != "fraud", "Uprice"], list(sales[sales$Insp != "fraud", "Prod"]), median, na.rm=T)

noQuant <- which(is.na(sales$Quant))

sales[noQuant,'Quant'] <- ceiling(sales[noQuant, 'Val'] / tPrice[sales[noQuant,"Prod"]])

noVal <- which(is.na(sales$Val))

sales[noVal, 'Val'] <- sales[noVal,'Quant'] * tPrice[sales[noVal, 'Prod']]


// data - saving clean data to a rdata file for R and a csv file for Spark

sales$Uprice <- sales$Val/sales$Quant

setwd("/work/R/example")

save(sales, file='salesClean.rdata')

write.csv(sales, "salesClean.csv", row.names=TRUE)



// outliers

setwd("/work/R/example")

load('salesClean.rdata')

attach(sales)

mi <- function(x) { 
  bp <- boxplot.stats(x)$stats 
  c(median = bp[3], iqr = bp[4]-bp[2])
}

notF <- which(Insp != 'fraud')

ms <- tapply(Uprice[notF], list(Prod=Prod[notF]), mi)

m <- matrix(unlist(ms), length(ms), 2, byrow=T, dimnames=list(names(ms), c('median', 'iqr')))

par(mfrow= c(1,2))

plot(m[,1], m[,2], xlab="Median", ylab="IQR", main="")

plot(m[,1], m[,2], xlab="Median", ylab="IQR", main="", col="grey", log="xy")


smalls <- which(table(Prod) < 20)

points(log(m[smalls,1]), log(m[smalls,2]), pch="+")


// less than 20 transactions by Kolmogorov-Smirnov test

nm <- scale(m)

similar <- matrix(NA, length(smalls), 7, dimnames = list(names(smalls), c("Simil", "ks.stat", "ks.p", "medP", "iqrP", "medS", "iqrS")))

for (i in seq(along = smalls)) {  d <- scale(nm, nm[smalls[i], ], FALSE)  d2 <- sqrt(drop(d^2 %*% rep(1, ncol(d))))  stat <- ks.test(prods[[smalls[i]]], prods[[order(d2)[2]]])  similar[i, ] <- c(order(d)[2], stat$statistic, stat$p.value, m[smalls[i], ], m[order(d2)[2], ])}

sum(similar[, "ks.p"] >= 0.9)

save(similar, file = "similarProducts.Rdata")










