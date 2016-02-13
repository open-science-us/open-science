### Using R and xts
~~~
> head(GSPC)

            Open  High   Low Close   Volume AdjClose
1970-01-02 92.06 93.54 91.79 93.00  8050000    93.00
1970-01-05 93.00 94.25 92.53 93.46 11490000    93.46
1970-01-06 93.46 93.81 92.13 92.82 11460000    92.82
1970-01-07 92.82 93.38 91.93 92.63 10010000    92.63
1970-01-08 92.63 93.47 91.99 92.68 10670000    92.68
1970-01-09 92.68 93.25 91.82 92.40  9380000    92.40

> tail(GSPC)

              Open    High     Low   Close     Volume AdjClose
2016-02-03 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53
2016-02-04 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86

> nrow(GSPC)
[1] 11634

# All Adjusted Close prices are equal to Close prices

> nrow(GSPC[GSPC$Close != GSPC$AdjClose,])
[1] 0

# All Adjusted Close prices are equal to Close prices so it is not necessary to use Adjusted Close prices to calculate average prices

> avgPrice <- function(p) apply(p[,c("High","Low","Close")], 1, mean)

> GSPC$HLC <- avgPrice(GSPC)

> tail(GSPC)

              Open    High     Low   Close     Volume AdjClose      HLC
2016-02-03 1907.07 1918.01 1872.23 1912.53 5172950000  1912.53 1900.923
2016-02-04 1911.67 1927.35 1900.52 1915.45 5193320000  1915.45 1914.440
2016-02-05 1913.07 1913.07 1872.65 1880.05 4929940000  1880.05 1888.590
2016-02-08 1873.25 1873.25 1828.46 1853.44 5636460000  1853.44 1851.717
2016-02-09 1848.46 1868.25 1834.94 1852.21 5183220000  1852.21 1851.800
2016-02-10 1857.10 1881.60 1850.32 1851.86 4471170000  1851.86 1861.260


# Indicator of the tendency, related to the confidence whether the target margin is attainable, in the next k days

# T.ind is directly copied from the book "Data Mining with R"

T.ind <- function(quotes, tgt.margin = 0.025, n.days = 10) {
  v <- apply(HLC(quotes), 1, mean)
  r <- matrix(NA, ncol = n.days, nrow = NROW(quotes))
  for (x in 1:n.days) r[, x] <- Next(Delt(v, k = x), x)
  x <- apply(r, 1, function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x, time(quotes))
  else x
}

# T.ind2 is the corrected one, derivated from formulas in the book "Data Mining with R"

T.ind2 <- function(quotes, tgt.margin = 0.025, n.days = 10) {
  r <- matrix(NA, ncol = n.days, nrow = NROW(quotes))
  for (x in 1:n.days) r[, x] <- Next(Delt(quotes[, "HLC"], quotes[, "Close"], k = x), x)
  x <- apply(r, 1, function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x, time(quotes))
  else x
}

> setwd("/work/R/example/stocks")
> png(file = "GSPC_3m.png", width = 960, height = 720, bg = "transparent")

> candleChart(last(GSPC, "3 months"), theme = "white", TA = NULL)

> addAvgPrice <- newTA(FUN = avgPrice, col = 1, legend = "AvgPrice")
> addAvgPrice(on = 1)

> addT.ind <- newTA(FUN = T.ind, col = "blue", legend = "tgtRet")
> addT.ind()

> addT.ind2 <- newTA(FUN = T.ind2, col = "red", legend = "tgtRet2")
> addT.ind2()

dev.off()
~~~
![GSPC_3m](../images/GSPC_3m.png)
