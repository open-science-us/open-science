## [Domain Generation Algorithm] (https://en.wikipedia.org/wiki/Domain_generation_algorithm)

### Using R package 'dga'

~~~
> install.packages('devtools')

> library('devtools')

> remove.packages('nlme')

> install.packages("nlme",repos="http://cran.r-project.org",type="binary")

> install.packages('caret')

> library('caret')

> devtools::install_github("jayjacobs/tldextract")

> devtools::install_github("jayjacobs/dga")

> library(dga)

> good <- c("facebook.com", "google.com", "sina.com.cn", "twitter.com", "yandex.ru", "msn.com")

> bad <- c("kqcrotywqigo.ru", "rlvukicfjceajm.ru", "ibxaoddvcped.ru", "tntuqxxbvxytpif.ru", "heksblnvanyeug.ru", "kbmqwdsrfzfqpdp.ru")

> dgaPredict(c(good, bad))

              name class prob
1         facebook legit 1.00
2           google legit 1.00
3             sina legit 1.00
4          twitter legit 1.00
5           yandex legit 1.00
6              msn legit 1.00
7     kqcrotywqigo   dga 1.00
8   rlvukicfjceajm   dga 1.00
9     ibxaoddvcped   dga 1.00
10 tntuqxxbvxytpif   dga 1.00
11  heksblnvanyeug   dga 0.98
12 kbmqwdsrfzfqpdp   dga 1.00
~~~

### Data Source

(1) [Top 1 Million Alexa domains](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip)

(2) [OpenDNS 10,000 Top Domains](https://raw.githubusercontent.com/opendns/public-domain-lists/master/opendns-top-domains.txt)

(3) [OpenDNS 10,000 Random Domains](https://raw.githubusercontent.com/opendns/public-domain-lists/master/opendns-random-domains.txt)

(4) [Example from click security](https://github.com/ClickSecurity/data_hacking/blob/master/dga_detection/data/dga_domains.txt)


### References

(1) [Building a DGA Classifier: Part 1, Data Preparation](http://datadrivensecurity.info/blog/posts/2014/Sep/dga-part1/)

(2) [Building a DGA Classifier: Part 2, Feature Engineering](http://datadrivensecurity.info/blog/posts/2014/Oct/dga-part2/)

(3) [Building a DGA Classifier: Part 3, Model Selection](http://datadrivensecurity.info/blog/posts/2014/Oct/dga-part3/)

(4) [7 Important Model Evaluation Error Metrics Everyone should know](http://www.analyticsvidhya.com/blog/2016/02/7-important-model-evaluation-error-metrics/)

(5) [Model Training and Tuning](http://topepo.github.io/caret/training.html)

(6) [Comparing a Random Forest to a CART model (Part 2)](http://www.analyticsvidhya.com/blog/2014/06/comparing-random-forest-simple-cart-model/)
