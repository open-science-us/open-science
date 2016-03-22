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

# sudo ln -s $(/usr/libexec/java_home)/jre/lib/server/libjvm.dylib /usr/local/lib, re-start R, still does not work so far

> install.packages('RWeka')

> library('RWeka')

> c45Fit <- train(class ~ ., data = train, method = "J48", metric="ROC", trControl = ctrl)


> resamp <- resamples(list(rf=rfFit, svm=svmFit))

> print(summary(resamp))

Call:
summary.resamples(object = resamp)

Models: rf, svm 
Number of resamples: 50 

ROC 
      Min. 1st Qu. Median   Mean 3rd Qu. Max. NA's
rf  0.9981  0.9998 0.9999 0.9998       1    1    0
svm 0.9988  0.9996 0.9999 0.9997       1    1    0

Sens 
      Min. 1st Qu. Median   Mean 3rd Qu. Max. NA's
rf  0.9893  0.9947 0.9973 0.9959  0.9973    1    0
svm 0.9893  0.9947 0.9973 0.9964  0.9993    1    0

Spec 
      Min. 1st Qu. Median   Mean 3rd Qu. Max. NA's
rf  0.9893  0.9947 0.9973 0.9962  0.9973    1    0
svm 0.9840  0.9927 0.9973 0.9954  0.9973    1    0


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
