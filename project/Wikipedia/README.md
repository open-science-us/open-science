## [Page view statistics](https://dumps.wikimedia.org/other/pagecounts-raw/)

### Downloading gzip files

~~~
cd /Wikipedia/2016/2

# download gzip files individually

curl -OL http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-000000.gz
curl -OL http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-010000.gz
curl -OL http://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/pagecounts-20160201-020000.gz


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


# download monthly gzip files

vi monthlyWiki.sh

for i in {"01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"}; do where=`pwd`; $where/downloadWiki.sh 2015 10 $i; done

or 

for i in {"01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"}; do where=`pwd`; $where/downloadWiki.sh 2015 11 $i; done

or 

for i in {"01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"}; do where=`pwd`; $where/downloadWiki.sh 2016 02 $i; done


# check monthly gzip file count under monthly folders

ls -l 2016/2/*.gz | grep -v ^l | wc -l

# check monthly gzip file size under monthly folders

ls -Sl 2016/2/*.gz
~~~
