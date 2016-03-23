## Model Selection using R

~~~
> library('caret')

> set.seed(1492)

> ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = twoClassSummary, classProbs = TRUE)

> library('pROC')


> library(rpart)

> rpFit <- train(class ~ ., data = traindga, metric = "ROC", method = "rpart", trControl = ctrl)


> rfFit <- train(class ~ ., data = traindga, metric = "ROC", method = "rf", trControl = ctrl)


> install.packages('kernlab')

> library('kernlab')

> svmFit <- train(class ~ ., data = traindga, method = "svmRadial", preProc = c("center", "scale"), metric = "ROC", tuneLength = 10, trControl = ctrl)


> install.packages('deepnet')

> library('deepnet')

grid <- expand.grid(layer1 = 1:5, layer2 = 0:3, layer3 = 0:3)
grid$hidden_dropout <- 0
grid$visible_dropout <- 0

> dnnFit <- train(class ~ ., data = traindga, method = "dnn", metric = "ROC", tuneGrid = grid, numepochs = 10, trControl = ctrl)

# Error in { : 
#  task 80 failed - "arguments imply differing number of rows: 0, 750"
# In addition: There were 50 or more warnings (use warnings() to see the first 50)

# dnnFit <- train(class ~ ., data = traindga, method = "dnn", preProc = c("center", "scale"), metric = "ROC", tuneGrid = grid, numepochs = 500, trControl = ctrl)


# sudo ln -s $(/usr/libexec/java_home)/jre/lib/server/libjvm.dylib /usr/local/lib, re-start R, still does not work so far

> install.packages('RWeka')

> library('RWeka')

> c45Fit <- train(class ~ ., data = train, method = "J48", metric="ROC", trControl = ctrl)


> resamp <- resamples(list(rp = rpFit, rf = rfFit, svm = svmFit, dnn = dnnFit))

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


> rpPred2 <- predict(rpFit2, testdga)

> print(confusionMatrix(rpPred2, testdga$class, positive = 'dga'))

Confusion Matrix and Statistics

          Reference
Prediction legit  dga
     legit  1238   64
     dga      12 1184
                                         
               Accuracy : 0.9696         
                 95% CI : (0.9621, 0.976)
    No Information Rate : 0.5004         
    P-Value [Acc > NIR] : < 2.2e-16      
                                         
                  Kappa : 0.9391         
 Mcnemar's Test P-Value : 4.913e-09      
                                         
            Sensitivity : 0.9487         
            Specificity : 0.9904         
         Pos Pred Value : 0.9900         
         Neg Pred Value : 0.9508         
             Prevalence : 0.4996         
         Detection Rate : 0.4740         
   Detection Prevalence : 0.4788         
      Balanced Accuracy : 0.9696         
                                         
       'Positive' Class : dga            


> rfPred2 <- predict(rfFit2, testdga)

> print(confusionMatrix(rfPred2, testdga$class, positive = 'dga'))

Confusion Matrix and Statistics

          Reference
Prediction legit  dga
     legit  1241   13
     dga       9 1235
                                          
               Accuracy : 0.9912          
                 95% CI : (0.9867, 0.9945)
    No Information Rate : 0.5004          
    P-Value [Acc > NIR] : <2e-16          
                                          
                  Kappa : 0.9824          
 Mcnemar's Test P-Value : 0.5224          
                                          
            Sensitivity : 0.9896          
            Specificity : 0.9928          
         Pos Pred Value : 0.9928          
         Neg Pred Value : 0.9896          
             Prevalence : 0.4996          
         Detection Rate : 0.4944          
   Detection Prevalence : 0.4980          
      Balanced Accuracy : 0.9912          
                                          
       'Positive' Class : dga             

rfSelectedIndices2 <- rfFit2$pred$mtry == 2

plot.roc(rfFit2$pred$obs[rfSelectedIndices2], rfFit2$pred$M[rfSelectedIndices2])


> svmPred2 <- predict(svmFit2, testdga)

> print(confusionMatrix(svmPred2, testdga$class, positive = 'dga'))

Confusion Matrix and Statistics

          Reference
Prediction legit  dga
     legit  1234   29
     dga      16 1219
                                         
               Accuracy : 0.982          
                 95% CI : (0.976, 0.9868)
    No Information Rate : 0.5004         
    P-Value [Acc > NIR] : < 2e-16        
                                         
                  Kappa : 0.964          
 Mcnemar's Test P-Value : 0.07364        
                                         
            Sensitivity : 0.9768         
            Specificity : 0.9872         
         Pos Pred Value : 0.9870         
         Neg Pred Value : 0.9770         
             Prevalence : 0.4996         
         Detection Rate : 0.4880         
   Detection Prevalence : 0.4944         
      Balanced Accuracy : 0.9820         
                                         
       'Positive' Class : dga            
~~~
