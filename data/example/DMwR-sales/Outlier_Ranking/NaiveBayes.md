## [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

### Ranking with R
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


# Naive Baye classification

> require(e1071, quietly = T)

> model <- naiveBayes(Insp ~ ., sData)

> preds <- predict(model, sData, type = "raw")

> sData <- cbind(sData, preds)
 
> head(sData)

          ID  Prod       Uprice Insp            ok       fraud
153610 v5032 p2452 3577.9844961   ok 9.365168e-151 1.000000000
143060 v4032 p1818   10.6930693   ok  8.448004e-01 0.155199559
183384  v909 p1440    5.7188338   ok  5.494919e-01 0.450508138
168685 v5565 p3774   13.6347955   ok  8.486012e-01 0.151398841
279624   v54  p285    0.9402974   ok  9.190506e-01 0.080949391
190561  v662 p1918   36.4242424   ok  9.973105e-01 0.002689487
~~~

### PR charts with R
~~~
> library(ROCR)

> sData$Label <- 0

> sData[sData$Insp == 'fraud', 'Label'] <- 1

> head(sData)

          ID  Prod       Uprice Insp            ok       fraud Label
153610 v5032 p2452 3577.9844961   ok 9.365168e-151 1.000000000     0
143060 v4032 p1818   10.6930693   ok  8.448004e-01 0.155199559     0
183384  v909 p1440    5.7188338   ok  5.494919e-01 0.450508138     0
168685 v5565 p3774   13.6347955   ok  8.486012e-01 0.151398841     0
279624   v54  p285    0.9402974   ok  9.190506e-01 0.080949391     0
190561  v662 p1918   36.4242424   ok  9.973105e-01 0.002689487     0

> par(mfrow= c(2,2))

> pred <- prediction(sData$fraud, sData$Label)

> perf <- performance(pred, "prec", "rec")

> plot(perf, main = "PR Chart")

IPRcurve <- function(preds, trues, ...) {
  require(ROCR, quietly = T)

  pd <- prediction(preds, trues)
  pf <- performance(pd, "prec", "rec")
  pf@y.values <- lapply(pf@y.values, function(x) rev(cummax(rev(x))))

  plot(pf, ...)
}

> IPRcurve(sData$fraud, sData$Label, main = "Interpolated PR Chart")

> perf <- performance(pred, "lift", "rpp")

> plot(perf, main = "Lift Chart")

CRchart <- function(preds, trues, ...) {
  require(ROCR, quietly = T)

  pd <- prediction(preds, trues)
  pf <- performance(pd, "rec", "rpp")

  plot(pf, ...)
}

> CRchart(sData$fraud, sData$Label, main = "Cumulative Recall Chart")
~~~
![NB_PR_Charts](../images/NB_PR_charts.png)

### Conclusion

The Naive Bayes scores are very far from the best results of the unsupervised models. Despite the oversampling of the 
minority class carried out by SMOTE, Naive Bayes is still not able to correctly predict which are the fraudulent reports.
