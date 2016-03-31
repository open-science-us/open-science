## Data Preparation using R

~~~
> alex <- read.csv('/work/dga/alex_good_legit.csv', header = F, sep = ",")

> colnames(alex) <- c("host", "domain", "tld", "length")

> alex$host <- NULL
> alex$tld <- NULL
> alex$class <- 0

> head(alex)

    domain length class
1   google      6     0
2  youtube      7     0
3 facebook      8     0
4    baidu      5     0
5    yahoo      5     0
6   amazon      6     0

> tail(alex)

              domain length class
956968          ning      4     0
956969 azurewebsites     13     0
956970   squarespace     11     0
956971       blogsky      7     0
956972          blog      4     0
956973           163      3     0


> dga <- read.csv('/work/dga/dga_domains2.csv', header = F, sep = ",")

> colnames(dga) <- c("host", "domain", "class", "subclass")

> dga$host <- NULL
> dga$class <- NULL
> dga$subclass <- NULL

> dga$domain <- as.character(dga$domain)
> dga$length <- nchar(dga$domain)

> dga$class <- 1

> head(dga)

                        domain length class
1  1002n0q11m17h017r1shexghfqf     27     1
2    1002ra86698fjpgqke1cdvbk5     25     1
3  1008bnt1iekzdt1fqjb76pijxhr     27     1
4  100f3a11ckgv438fpjz91idu2ag     27     1
5 100fjpj1yk5l751n4g9p01bgkmaf     28     1
6  100nio91ra2kuteap7eh1o1qk69     27     1


> total <- rbind(alex, dga)


~~~
