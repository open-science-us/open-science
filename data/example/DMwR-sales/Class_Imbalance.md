## [Class Imbalance](http://www.chioka.in/class-imbalance-problem/)

### SMOTE
~~~
> setwd("/work/R/example")

> load('salesClean.rdata')

> knownSales <- sales[sales$Insp == 'fraud' | sales$Insp == 'ok',]

> nrow(sales)
[1] 400204

> nrow(knownSales)
[1] 15726

> data <- knownSales[, c("ID", "Prod", "Uprice", "Insp")]

> data$Insp <- factor(data$Insp, levels = c("ok", "fraud"))


# SMOTE for sampling

library(DMwR)

> sData <- SMOTE(Insp ~ ., data, perc.over = 700)

> nrow(sData)
[1] 27896

> length(which(sData$Insp == 'ok'))
[1] 17752

> length(which(sData$Insp == 'fraud'))
[1] 10144
~~~
