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


### Preparing Corpus




### Reference


#### Word2Vec against English Wikipedia

(1) [Training Word2Vec Model on English Wikipedia by Gensim](http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim)

(2) [Wiki2Vec](https://github.com/idio/wiki2vec)

(3) [Training word2vec on full Wikipedia](https://groups.google.com/forum/#!topic/gensim/MJWrDw_IvXw)


#### Word2Vec on Spark

(1) [Word2Vec on Spark](http://spark.apache.org/docs/latest/ml-features.html#word2vec)

(2) [Spark Word2vec vector mathematics](http://stackoverflow.com/questions/34172242/spark-word2vec-vector-mathematics)

(3) [Clustering the News with Spark and MLLib](http://bigdatasciencebootcamp.com/posts/Part_3/clustering_news.html)

(4) [Sentence Similarity using Word2Vec and Word Movers Distance](http://sujitpal.blogspot.com/2015/09/sentence-similarity-using-word2vec-and.html)



#### Word2Vec







