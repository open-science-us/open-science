## English Wikipedia

### Downloading XML files compressed in bz2

~~~
cd /work/wiki2vec

curl -OL https://dumps.wikimedia.org/enwiki/20160820/enwiki-20160820-pages-articles-multistream.xml.bz2
~~~


### Converting XML files into text files readable for Spark

~~~
// Downloading source code from https://github.com/idio/wiki2vec

cd /work/wiki2vec

unzip wiki2vec-master.zip

cd wiki2vec-master

{SBT_HOME}/bin/sbt assembly

java -Xmx4G -Xms4G -cp /work/wiki2vec/wiki2vec-master/target/scala-2.10/wiki2vec-assembly-1.0.jar org.idio.wikipedia.dumps.CreateReadableWiki enwiki-20160820-pages-articles-multistream.xml.bz2 /work/wiki2vec/enwiki-20160820-pages-articles-multistream.txt

bzip2 enwiki-20160820-pages-articles-multistream.txt
~~~
