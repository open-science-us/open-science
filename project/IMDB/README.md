## Kaggle-IMDB: Sentiment Analysis of Movie Reviews

## Public Dataset
(1) Large Movie Review Dataset, Stanford University,  http://ai.stanford.edu/~amaas/data/sentiment/

~~~
curl -OL http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz

tar -xvzf aclImdb_v1.tar.gz

find aclImdb/train/pos/ -name "*.txt" | while read F; do (cat "${F}"; echo) >> train_pos.txt; done
find aclImdb/train/neg/ -name "*.txt" | while read F; do (cat "${F}"; echo) >> train_neg.txt; done
find aclImdb/test/pos/ -name "*.txt" | while read F; do (cat "${F}"; echo) >> test_pos.txt; done
find aclImdb/test/neg/ -name "*.txt" | while read F; do (cat "${F}"; echo) >> test_neg.txt; done
~~~

## Data Preprocessing

I follow the data proprcessing approach, including data cleansing, from Reference (3)

~~~
pos_reviews = [re.sub(r"([\.\",\(\)!\?;:])", " \\1 ", review.lower().replace('\n','').replace('<br />', ' ')) for review in pos_reviews]
neg_reviews = [re.sub(r"([\.\",\(\)!\?;:])", " \\1 ", review.lower().replace('\n','').replace('<br />', ' ')) for review in neg_reviews]
~~~

## Reference
(1) [Sentiment Analysis for Movie Reviews](https://cseweb.ucsd.edu/~jmcauley/cse255/reports/fa15/003.pdf)

(2) [Deep learning for sentiment analysis of movie reviews](https://cs224d.stanford.edu/reports/PouransariHadi.pdf)

(3) [Gensim Doc2Vec Tutorial on the IMDB Sentiment Dataset](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-IMDB.ipynb)
