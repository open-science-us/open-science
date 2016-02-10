## Outlier Ranking

### Data Preparing
~~~
> setwd("/work/R/example")

> load('salesClean.rdata')

> knownSales <- sales[sales$Insp == 'fraud' | sales$Insp == 'ok',]

> data <- knownSales[, c("ID", "Prod", "Uprice", "Insp")]

> data$Insp <- factor(data$Insp, levels = c("ok", "fraud"))

> library(DMwR)

> sData <- SMOTE(Insp ~ ., data, perc.over = 700)
~~~

### Box Plot
~~~
bp_mi <- function(x) { 
  bp <- boxplot.stats(x)$stats 
  c(median = bp[3], iqr = bp[4]-bp[2])
}

> bp_ms <- tapply(sales$Uprice, list(Prod=sales$Prod), bp_mi)

> bp_m <- matrix(unlist(bp_ms),length(bp_ms),2,byrow=T,dimnames=list(names(bp_ms),c('median','iqr')))

> bp_m[which(bp_m[,'iqr']==0),'iqr'] <- bp_m[which(bp_m[,'iqr']==0),'median']

> bp_ORscore <- abs(sales$Uprice - bp_m[sales$Prod,'median']) / bp_m[sales$Prod,'iqr']

> bp_sales <- cbind(sales, bp_ORscore)

> bp_knownSales <- bp_sales[bp_sales$Insp == 'fraud' | bp_sales$Insp == 'ok',]

> bp_knownSales$Label <- 0

> bp_knownSales[bp_knownSales$Insp == 'fraud', 'Label'] <- 1
~~~

### Local Outlier Factor
~~~
> setwd("/work/R/example")

> lofs <- read.csv('lofData.csv', header=TRUE)

> knownLofs <- lofs[lofs$Insp == 'fraud' | lofs$Insp == 'ok',]

> knownLofs$Label <- 0

> knownLofs[knownLofs$Insp == 'fraud', 'Label'] <- 1
~~~

### Naive Baye classification
~~~
> knownSales <- sales[sales$Insp == 'fraud' | sales$Insp == 'ok',]

> data <- knownSales[, c("ID", "Prod", "Uprice", "Insp")]

> data$Insp <- factor(data$Insp, levels = c("ok", "fraud"))

> library(DMwR)

> sData <- SMOTE(Insp ~ ., data, perc.over = 700)

> require(e1071, quietly = T)

> nb_model <- naiveBayes(Insp ~ ., sData)

> nb_preds <- predict(nb_model, data, type = "raw")

> nb_data <- cbind(data, nb_preds)

> nb_data$Label <- 0

> nb_data[nb_data$Insp == 'fraud', 'Label'] <- 1
~~~

### Deep Learning with H2O
~~~
> h2o_pred <- h2o.getFrame("prediction-565cf316-f434-498d-8dbb-28ebd3562bc8")

> h2o_df <- as.data.frame(h2o_pred)

> h2o_data <- cbind(data, h2o_df)

> h2o_data$Label <- 0

> h2o_data[h2o_data$Insp == 'fraud', 'Label'] <- 1
~~~

### PR charts
~~~
> library(ROCR)

CRchart <- function(preds, trues, ...) {
  require(ROCR, quietly = T)

  pd <- prediction(preds, trues)
  pf <- performance(pd, "rec", "rpp")

  plot(pf, ...)
}

> CRchart(knownSales$bp_ORscore, knownSales$Label, main = "Cumulative Recall Chart", lty=1, xlim=c(0,1), ylim=c(0,1))


> CRchart(knownLofs$LOF, knownLofs$Label, col='grey', add=T)


> CRchart(nb_data$fraud, nb_data$Label, col='grey', lty=2, add=T)


> CRchart(h2o_data$fraud, h2o_data$Label, lty=2, add=T)

> legend('bottomright',c('BoxPlot', 'LOF', 'NaiveBayes', 'H2O'), lty=c(1,1,2,2),col=c('black','grey','grey','black'))
~~~
![PR_Charts](../images/PR_charts.png)


### Conclusion

Deep Learning with H2O outpeforms others (Box Plot, Local Outlier Factor and Naive Bayes) and achives 80% Recall fastest.


