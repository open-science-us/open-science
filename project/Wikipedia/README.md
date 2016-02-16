## [Page view statistics](https://dumps.wikimedia.org/other/pagecounts-raw/)

### Download compressed gzip files
~~~
cd /work/R/example/Wikipedia

wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-000000.gz
wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-010000.gz
wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-020000.gz

for i in {0..9}; do addr=http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-0; addr+=$i; addr+=0000.gz; echo $addr; wget $addr; done

for i in {10..23}; do addr=http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-; addr+=$i; addr+=0000.gz; echo $addr; wget $addr; done

zgrep Bitcoin  *.gz > pagecounts-20160201.txt
~~~
