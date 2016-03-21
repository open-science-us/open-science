## Model Selection using R

~~~
> install.packages('caret')

> library('caret')

> set.seed(1492)

> ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = twoClassSummary, classProbs = TRUE)


> install.packages('pROC')

> library('pROC')

> rfFit <- train(class ~ ., data = train, metric = "ROC", method = "rf", trControl = ctrl)


> install.packages('kernlab')

> library('kernlab')

> svmFit <- train(class ~ ., data = train, method = "svmRadial", preProc = c("center", "scale"), metric = "ROC", tuneLength = 10, trControl = ctrl)


> install.packages('RWeka')

> library('RWeka')

> c45Fit <- train(class ~ ., data = train, method = "J48", metric="ROC", trControl = ctrl)


~~~
