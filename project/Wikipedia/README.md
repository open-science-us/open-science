## [Page view statistics](https://dumps.wikimedia.org/other/pagecounts-raw/)

### Download compressed gzip files
~~~
cd /work/R/example/Wikipedia

wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-000000.gz
wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-010000.gz
wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-020000.gz

zgrep Bitcoin  *.gz > pagecounts-20160201.txt
~~~
