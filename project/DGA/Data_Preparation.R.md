### Data Preparation using R
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
