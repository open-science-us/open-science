## Feature Selection using Random Forest with R

~~~
> library('caret')

> set.seed(1492)

> ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = twoClassSummary, classProbs = TRUE)


> install.packages('pROC')

> library('pROC')

> rfFit <- train(class ~ ., data = train, metric = "ROC", method = "rf", trControl = ctrl)

> importance <- varImp(rfFit, scale=F)

> plot(importance)
~~~
![feature_importance](images/feature_importance.png)

~~~
> rfFit2 <- train(class ~ ., data = train2, metric = "ROC", method = "rf", trControl = ctrl)

> importance2 <- varImp(rfFit2, scale=F)

> plot(importance2)
~~~
![feature_importance2](images/feature_importance2.png)


~~~
> resamp12 <- resamples(list(rf1=rfFit, rf2=rfFit2))

> diff12 <- diff(resamp12)
 
> print(diff12$statistics$ROC$rf1.diff.rf2)

	One Sample t-test

data:  x
t = 2.3858, df = 49, p-value = 0.02095
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 4.863889e-05 5.682235e-04
sample estimates:
   mean of x 
0.0003084312 
~~~
