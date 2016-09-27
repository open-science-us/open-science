## English Wikipedia

### Downloading XML files compressed in bz2

~~~
cd /mnt/wiki2vec

curl -OL https://dumps.wikimedia.org/enwiki/20160820/enwiki-20160820-pages-articles-multistream.xml.bz2
~~~


### Converting XML files into text files readable for Spark

Downloading source code from https://github.com/idio/wiki2vec and building the jar wiki2vec-assembly-1.0.jar

~~~

cd /mnt/wiki2vec

java -Xmx10G -Xms10G -cp org.idio.wikipedia.dumps.ReadableWiki wiki2vec-assembly-1.0.jar enwiki-20160820-pages-articles-multistream.xml.bz2 /mnt/wiki2vec/

bzip2 enwiki-20160820-pages-articles-multistream.txt

~~~
