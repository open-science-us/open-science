## Model Selection using R

~~~
> library('caret')

> set.seed(1492)

> ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = twoClassSummary, classProbs = TRUE)


> library(rpart)

> rpFit <- train(class ~ ., data = train, metric = "ROC", method = "rpart", trControl = ctrl)


> install.packages('pROC')

> library('pROC')

> rfFit <- train(class ~ ., data = train, metric = "ROC", method = "rf", trControl = ctrl)


> install.packages('kernlab')

> library('kernlab')

> svmFit <- train(class ~ ., data = train, method = "svmRadial", preProc = c("center", "scale"), metric = "ROC", tuneLength = 10, trControl = ctrl)


# sudo ln -s $(/usr/libexec/java_home)/jre/lib/server/libjvm.dylib /usr/local/lib, re-start R, still does not work so far

> install.packages('RWeka')

> library('RWeka')

> c45Fit <- train(class ~ ., data = train, method = "J48", metric="ROC", trControl = ctrl)


> resamp <- resamples(list(rp = rpFit, rf = rfFit, svm = svmFit))

> print(summary(resamp))

Call:
summary.resamples(object = resamp)

Models: rp, rf, svm 
Number of resamples: 50 

ROC 
      Min. 1st Qu. Median   Mean 3rd Qu.   Max. NA's
rp  0.9607  0.9733 0.9790 0.9799  0.9874 0.9974    0
rf  0.9978  0.9997 0.9999 0.9997  1.0000 1.0000    0
svm 0.9981  0.9998 0.9999 0.9996  1.0000 1.0000    0

Sens 
      Min. 1st Qu. Median   Mean 3rd Qu. Max. NA's
rp  0.9680  0.9813 0.9867 0.9865  0.9920    1    0
rf  0.9867  0.9947 0.9960 0.9955  0.9973    1    0
svm 0.9787  0.9947 0.9973 0.9959  0.9973    1    0

Spec 
      Min. 1st Qu. Median   Mean 3rd Qu.   Max. NA's
rp  0.9413  0.9495 0.9613 0.9668  0.9860 0.9973    0
rf  0.9867  0.9947 0.9973 0.9960  0.9973 1.0000    0
svm 0.9813  0.9920 0.9947 0.9950  0.9973 1.0000    0


> pred2 <- predict(rfFit2, test)

> print(confusionMatrix(pred2, test$class))

Confusion Matrix and Statistics

          Reference
Prediction legit  dga
     legit  1240    8
     dga      10 1240
                                          
               Accuracy : 0.9928          
                 95% CI : (0.9886, 0.9957)
    No Information Rate : 0.5004          
    P-Value [Acc > NIR] : <2e-16          
                                          
                  Kappa : 0.9856          
 Mcnemar's Test P-Value : 0.8137          
                                          
            Sensitivity : 0.9920          
            Specificity : 0.9936          
         Pos Pred Value : 0.9936          
         Neg Pred Value : 0.9920          
             Prevalence : 0.5004          
         Detection Rate : 0.4964          
   Detection Prevalence : 0.4996          
      Balanced Accuracy : 0.9928          
                                          
       'Positive' Class : legit           
~~~
