## [Page view statistics](https://dumps.wikimedia.org/other/pagecounts-raw/)

### Download compressed gzip files
~~~
cd /work/R/example/Wikipedia

# download gzip files individually

wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-000000.gz
wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-010000.gz
wget http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-020000.gz

# download daily gzip files

for i in {0..9}; do addr=http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-0; addr+=$i; addr+=0000.gz; echo $addr; wget $addr; done

for i in {10..23}; do addr=http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-; addr+=$i; addr+=0000.gz; echo $addr; wget $addr; done


# download daily gzip files (2)

vi downloadWiki.sh

echo "year: $1   month: $2   day: $3"

for i in {0..9}; do addr=http://dumps.wikimedia.org/other/pagecounts-raw/$1/$1-$2/pagecounts-$1$2$3-0; addr+=$i; addr+=0000.gz; wget $addr; done

for i in {10..23}; do addr=http://dumps.wikimedia.org/other/pagecounts-raw/$1/$1-$2/pagecounts-$1$2$3-; addr+=$i; addr+=0000.gz; wget $addr; done

chmod +x downloadWiki.sh

./downloadWiki.sh 2016 01 01


# check daily gzip files under monthly folders

ls -l 2016/1/*.gz | grep -v ^l | wc -l


# extract records for "Bitcoin"

zgrep Bitcoin  *.gz > pagecounts-20160201.txt

zgrep Bitcoin /Volumes/"Seagate Backup Plus Drive"/Wikipedia/2016/2/*.gz > Bitcoin-201602.txt
~~~
