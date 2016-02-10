## Deep Learning with R on H2O

### Starting with R
~~~
# Data Preparing

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

> library(DMwR)

> sData <- SMOTE(Insp ~ ., data, perc.over = 700)

> nrow(sData)
[1] 27896

> length(which(sData$Insp == 'ok'))
[1] 17752

> length(which(sData$Insp == 'fraud'))
[1] 10144


# As H2O

> library(h2o)

> h2o.init()

> testH2O <- as.h2o(data)

> trainH2O <- as.h2o(sData)
~~~

### Deep Learning with H2O
~~~
(1) Goto http://127.0.0.1:54321/flow/index.html

(2) Click "getFrames" under "Assistance"

(3) Choose the frame "filea1599182bf_csv_2.hex_3" and click "Build Model"

(4) Select an algorithm: "Deep Learning"

(5) training_frame: "filea1599182bf_csv_2.hex_3"; response_column: "Insp"; activation: "RectifierWithDropout"; hidden: 100,100; epochs: 5

(6) Click "Build Model"

(7) Click "View" and "Predict"

(8) Choose Frame: "filea11990b1b0_csv_4.hex_5" and click "Predict"

(9) Click "getFrames" under "Assistance" to see the new frame: "prediction-565cf316-f434-498d-8dbb-28ebd3562bc8"
~~~

### Going back to R
~~~
# As Data Frame

> pred <- h2o.getFrame("prediction-565cf316-f434-498d-8dbb-28ebd3562bc8")

> head(pred)

  predict       fraud        ok
1      ok 0.005882522 0.9941175
2      ok 0.003928889 0.9960711
3      ok 0.005871750 0.9941283
4      ok 0.003940178 0.9960598
5      ok 0.004764471 0.9952355
6      ok 0.006162240 0.9938378

> nrow(pred)
[1] 15726

> mode(pred)
[1] "environment"

> class(pred)
[1] "Frame"


> df <- as.data.frame(pred)

> data <- cbind(data, df)

> head(data)

    ID Prod   Uprice Insp predict       fraud        ok
53 v42  p11 6.082157   ok      ok 0.005882522 0.9941175
56 v45  p11 7.403846   ok      ok 0.003928889 0.9960711
68 v42  p11 5.436020   ok      ok 0.005871750 0.9941283
77 v50  p11 6.001428   ok      ok 0.003940178 0.9960598
82 v46  p12 5.473684   ok      ok 0.004764471 0.9952355
84 v48  p12 7.840647   ok      ok 0.006162240 0.9938378


# PR charts with R

> library(ROCR)

> data$Label <- 0

> data[data$Insp == 'fraud', 'Label'] <- 1

> head(data)

    ID Prod   Uprice Insp predict       fraud        ok Label
53 v42  p11 6.082157   ok      ok 0.005882522 0.9941175     0
56 v45  p11 7.403846   ok      ok 0.003928889 0.9960711     0
68 v42  p11 5.436020   ok      ok 0.005871750 0.9941283     0
77 v50  p11 6.001428   ok      ok 0.003940178 0.9960598     0
82 v46  p12 5.473684   ok      ok 0.004764471 0.9952355     0
84 v48  p12 7.840647   ok      ok 0.006162240 0.9938378     0

> par(mfrow= c(2,2))

> pred <- prediction(data$fraud, data$Label)

> perf <- performance(pred, "prec", "rec")

> plot(perf, main = "PR Chart")

IPRcurve <- function(preds, trues, ...) {
  require(ROCR, quietly = T)

  pd <- prediction(preds, trues)
  pf <- performance(pd, "prec", "rec")
  pf@y.values <- lapply(pf@y.values, function(x) rev(cummax(rev(x))))

  plot(pf, ...)
}

> IPRcurve(data$fraud, data$Label, main = "Interpolated PR Chart")

> perf <- performance(pred, "lift", "rpp")

> plot(perf, main = "Lift Chart")

CRchart <- function(preds, trues, ...) {
  require(ROCR, quietly = T)

  pd <- prediction(preds, trues)
  pf <- performance(pd, "rec", "rpp")

  plot(pf, ...)
}

> CRchart(data$fraud, data$Label, main = "Cumulative Recall Chart")
~~~
![DL_PR_Charts](../images/DL_PR_charts.png)
