## Feature Selection using Random Forest with R

~~~
> library('caret')

> set.seed(1492)

> ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = twoClassSummary, classProbs = TRUE)


> lrFit <- train(class ~ ., data = traindga, metric = "ROC", method = "glm", family = "binomial", tuneLength = 10, trControl = ctrl)

> lrImp <- varImp(lrFit, scale = F)

> plot(lrImp)
~~~
![lr_feature_importance](images/lr_feature_importance.png)
 
~~~
> library(rpart)

> rpFit <- train(class ~ ., data = traindga, metric = "ROC", method = "rpart", tuneLength = 10, trControl = ctrl)

> rpImp <- varImp(rpFit, scale = F)

> plot(rpImp)
~~~
![rp_feature_importance](images/rp_feature_importance.png)

~~~
> rpFields2 <- c("class", "length", "entropy", "dictionary", "gram4", "gram1")

# fields <- c("class", "entropy", "length",  "dictionary", "gram1", "gram2", "gram3", "gram4", "gram5", "gram345")

> rpTraindga2 <- sampledga[trainindex, rpFields2]

> rpFit2 <- train(class ~ ., data = rpTraindga2, metric = "ROC", method = "rpart", trControl = ctrl)

> rpImp2 <- varImp(rpFit2, scale = F)

> plot(rpImp2)
~~~
![rp_feature_importance](images/rp_feature_importance2.png)

~~~
> rpResamples12 <- resamples(list(rp1 = rpFit, rp2 = rpFit2))

> rpDiff12 <- diff(rpResamples12)
 
> print(rpDiff12$statistics$ROC$rp1.diff.rp2)

	One Sample t-test

data:  x
t = -2.3784, df = 49, p-value = 0.02133
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 -0.0075613697 -0.0006355956
sample estimates:
   mean of x 
-0.004098483 
~~~

~~~
> library('kernlab')

> svmFit <- train(class ~ ., data = traindga, method = "svmRadial", preProc = c("center", "scale"), metric = "ROC", tuneLength = 10, trControl = ctrl)

> svmImp <- varImp(svmFit, scale=F)

> plot(svmImp)
~~~
![svm_feature_importance](images/svm_feature_importance.png)

~~~
> svmFields2 <- c("class", "entropy", "dictionary", "length", "gram1")

# fields <- c("class", "entropy", "length",  "dictionary", "gram1", "gram2", "gram3", "gram4", "gram5", "gram345")

> svmTraindga2 <- sampledga[trainindex, svmFields2]

> svmFit2 <- train(class ~ ., data = svmTraindga2, method = "svmRadial", preProc = c("center", "scale"), metric = "ROC", tuneLength = 10, trControl = ctrl)

> svmImp2 <- varImp(svmFit2, scale = F)

> plot(svmImp2)
~~~
![svm_feature_importance2](images/svm_feature_importance2.png)

~~~
> svmResamples12 <- resamples(list(svm1 = svmFit, svm2 = svmFit2))

> svmDiff12 <- diff(svmResamples12)
 
> print(svmDiff12$statistics$ROC$svm1.diff.svm2)

	One Sample t-test

data:  x
t = 11.817, df = 49, p-value = 5.932e-16
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 0.002664066 0.003755780
sample estimates:
  mean of x 
0.003209923 
~~~

~~~
> install.packages('pROC')

> library('pROC')

> rfFit <- train(class ~ ., data = traindga, metric = "ROC", method = "rf", trControl = ctrl)

> rfImp <- varImp(rfFit, scale=F)

> plot(rfImp)
~~~
![rf_feature_importance](images/rf_feature_importance.png)

~~~
> rfFields2 <- c("class", "dictionary", "length", "gram4", "entropy")

# fields <- c("class", "entropy", "length",  "dictionary", "gram1", "gram2", "gram3", "gram4", "gram5", "gram345")

> rfTraindga2 <- sampledga[trainindex, rfFields2]

> rfFit2 <- train(class ~ ., data = rfTraindga2, metric = "ROC", method = "rf", trControl = ctrl)

> rfImp2 <- varImp(rfFit2, scale = F)

> plot(rfImp2)
~~~
![rf_feature_importance2](images/rf_feature_importance2.png)

~~~
> rfResamples12 <- resamples(list(rf1 = rfFit, rf2 = rfFit2))

> rfDiff12 <- diff(rfResamples12)
 
> print(rfDiff12$statistics$ROC$rf1.diff.rf2)

	One Sample t-test

data:  x
t = 4.3992, df = 49, p-value = 5.854e-05
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 0.0003525197 0.0009454302
sample estimates:
   mean of x 
0.0006489749 
~~~
