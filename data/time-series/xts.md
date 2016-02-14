## [xts](https://cran.r-project.org/web/packages/xts/index.html)

~~~
> install.packages('xts')

> library(xts)
~~~

### Loading S&P500 daily data from Yahoo finance with R package "tseries"
~~~
> library(tseries)

> GSPC <- as.xts(get.hist.quote("^GSPC",start="1970-01-01",end="2016-02-10",quote=c("Open", "High", "Low", "Close","Volume","AdjClose")))

> mode(GSPC)
[1] "numeric"

> class(GSPC)
[1] "xts" "zoo"

> colnames(GSPC)
[1] "Open"     "High"     "Low"      "Close"    "Volume"   "AdjClose"

> dim(GSPC)
[1] 11634     6
~~~

### Handling S&P500 daily data
~~~
> GSPC[as.POSIXlt("2016-02-10")]

             Open   High     Low   Close     Volume AdjClose
2016-02-10 1857.1 1881.6 1850.32 1851.86 4471170000  1851.86

> GSPC["2016-02-10"]

             Open   High     Low   Close     Volume AdjClose
2016-02-10 1857.1 1881.6 1850.32 1851.86 4471170000  1851.86

> GSPC["2016-02"]

              Open    High     Low   Close     Volume AdjClose
2016-02-01 1936.94 1947.20 1920.30 1939.38 4322530000  1939.38
2016-02-02 1935.26 1935.26 1897.29 1903.03 4463190000  1903.03
2016-02-03 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53
2016-02-04 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86

> GSPC["2016-02-05/"]

              Open    High     Low   Close     Volume AdjClose
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86

> GSPC["2016-02-01/2016-02-10"]

              Open    High     Low   Close     Volume AdjClose
2016-02-01 1936.94 1947.20 1920.30 1939.38 4322530000  1939.38
2016-02-02 1935.26 1935.26 1897.29 1903.03 4463190000  1903.03
2016-02-03 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53
2016-02-04 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86

> tail(index(GSPC))

[1] "2016-02-03" "2016-02-04" "2016-02-05" "2016-02-08" "2016-02-09" "2016-02-10"

> min(index(GSPC))
[1] "1970-01-02"

> max(index(GSPC))
[1] "2016-02-10"

> tail(coredata(GSPC))

            Open    High     Low   Close     Volume AdjClose
[11629,] 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53
[11630,] 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45
[11631,] 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05
[11632,] 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44
[11633,] 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21
[11634,] 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86
~~~


### Loading Bitcoin daily data from a CSV file
~~~
> Bitstamp <- as.xts(read.zoo("/work/R/example/stocks/bitstamp-daily.csv", sep=",", header=T))

> mode(Bitstamp)
[1] "numeric"

> class(Bitstamp)
[1] "xts" "zoo"

> colnames(Bitstamp)
[1] "Open"   "High"   "Low"    "Close"  "Volume"

> dim(Bitstamp)
[1] 1569    5
~~~


### Conclusion

In summary, xts objects are adequate to store stock quotes data, as they allow to store multiple time series with irregular time tags, and provide powerful indexing schemes.





