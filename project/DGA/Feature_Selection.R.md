## Feature Selection using Random Forest with R

~~~
> library('caret')

> set.seed(1492)

> ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = twoClassSummary, classProbs = TRUE)


> library(rpart)

> rpFit <- train(class ~ ., data = traindga, metric = "ROC", method = "rpart", trControl = ctrl)

> rpImp <- varImp(rpFit, scale=F)

> plot(rpImp)
~~~
![rp_feature_importance](images/rp_feature_importance.png)

~~~
> library('kernlab')

> svmFit <- train(class ~ ., data = traindga, method = "svmRadial", preProc = c("center", "scale"), metric = "ROC", tuneLength = 10, trControl = ctrl)

> svmImp <- varImp(svmFit, scale=F)

> plot(svmImp)
~~~
![svm_feature_importance](images/svm_feature_importance.png)

~~~
> install.packages('pROC')

> library('pROC')

> rfFit <- train(class ~ ., data = traindga, metric = "ROC", method = "rf", trControl = ctrl)

> rfImp <- varImp(rfFit, scale=F)

> plot(rfImp)
~~~
![rf_feature_importance](images/rf_feature_importance.png)

~~~
> rfFit2 <- train(class ~ ., data = traindga2, metric = "ROC", method = "rf", trControl = ctrl)

> rfImp2 <- varImp(rfFit2, scale=F)

> plot(rfImp2)
~~~
![rf_feature_importance2](images/rf_feature_importance2.png)


~~~
> resamp12 <- resamples(list(rf1 = rfFit, rf2 = rfFit2))

> diff12 <- diff(resamp12)
 
> print(diff12$statistics$ROC$rf1.diff.rf2)

	One Sample t-test

data:  x
t = 2.1105, df = 49, p-value = 0.03994
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 0.0000103543 0.0004227226
sample estimates:
   mean of x 
0.0002165384 
~~~
