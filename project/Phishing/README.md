## Phishing Email Detection

### Data Set

(1) Phishing Email Dataset: J. Nazario, “Phishingcorpus homepage,” 2006, http://monkey.org/%7Ejose/wiki/doku.php?id=PhishingCorpus
~~~
// download mbox files to /work/phishing/jose from http://monkey.org/%7Ejose/wiki/doku.php?id=PhishingCorpus

// download mb2md-3.20.pl to /work/phishing from http://batleth.sapienti-sat.org/projects/mb2md/

cd /work/phishing

chmod +x mb2md-3.20.pl

./mb2md-3.20.pl -s /work/phishing/jose/phishing0.mbox -d /work/phishing/jose/phishing0
./mb2md-3.20.pl -s /work/phishing/jose/phishing1.mbox -d /work/phishing/jose/phishing1
./mb2md-3.20.pl -s /work/phishing/jose/phishing2.mbox -d /work/phishing/jose/phishing2
./mb2md-3.20.pl -s /work/phishing/jose/phishing3.mbox -d /work/phishing/jose/phishing3
./mb2md-3.20.pl -s /work/phishing/jose/private-phishing4.mbox -d /work/phishing/jose/private-phishing4
./mb2md-3.20.pl -s /work/phishing/jose/20051114.mbox -d /work/phishing/jose/20051114
~~~
(2) Good or Ham Email Dataset: Apache SpamAssassin, https://spamassassin.apache.org/publiccorpus/
(3) TREC 2005 Email Dataset: http://plg.uwaterloo.ca/cgi-bin/cgiwrap/gvcormac/foo


### Reference

(1) [Phishing Detection Using Neural Network](http://cs229.stanford.edu/proj2012/ZhangYuan-PhishingDetectionUsingNeuralNetwork.pdf)
(2) [Classification of Phishing Email Using Random Forest Machine Learning Technique](https://www.hindawi.com/journals/jam/2014/425731/)
(3) [H2O Ensemble Tree](http://ethen8181.github.io/machine-learning/h2o/h2o_ensemble_tree/h2o_ensemble_tree.html)
