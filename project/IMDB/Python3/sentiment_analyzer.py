import sys
import time
import numpy as np
import re
import json
import pickle

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

class SentimentAnalyzer():
  def __init__(self, json_fn):
    with open(json_fn) as f:
      self.params = json.load(f)
#
    nr = self.params['tfidf'].get('ngram_range', None)
    if (nr is None):
      nr = (1,1)
    else:
      nr = tuple(nr)
#
    self.vectorizer = TfidfVectorizer(stop_words=self.params['tfidf'].get('stop_words', None), ngram_range=nr, use_idf=self.params['tfidf'].get('use_idf', None), smooth_idf=self.params['tfidf'].get('smooth_idf', None), sublinear_tf=self.params['tfidf'].get('sublinear_tf', None))
    logger.info("TfidfVectorizer\tstop_words:\t{}".format(self.params['tfidf'].get('stop_words', None)))
    logger.info("TfidfVectorizer\tngram_range:\t{}".format(nr))
    logger.info("TfidfVectorizer\tuse_idf:\t{}".format(self.params['tfidf'].get('use_idf', None)))
    logger.info("TfidfVectorizer\tsmooth_idf:\t{}".format(self.params['tfidf'].get('smooth_idf', None)))
    logger.info("TfidfVectorizer\tsublinear_tf:\t{}".format(self.params['tfidf'].get('sublinear_tf', None)))

  def __getattr__(self, attr):
    return None

  def preparePair(self, pos_fn, neg_fn):
    with open(pos_fn,'r') as infile:
      pos_reviews = infile.readlines()
    with open(neg_fn,'r') as infile:
      neg_reviews = infile.readlines()
#
    pos_reviews = [re.sub(r"([\.\",\(\)!\?;:])", " \\1 ", review.lower().replace('\n','').replace('<br />', ' ')) for review in pos_reviews]
    neg_reviews = [re.sub(r"([\.\",\(\)!\?;:])", " \\1 ", review.lower().replace('\n','').replace('<br />', ' ')) for review in neg_reviews]
#
    logger.info("preprocess %d positive reviews from %s" % (len(pos_reviews), pos_fn))
    logger.info("preprocess %d negative reviews from %s" % (len(neg_reviews), neg_fn))
# 
    X = pos_reviews + neg_reviews
    Y = np.concatenate((np.ones(len(pos_reviews)), np.zeros(len(neg_reviews))))
#
    return X, Y

  def prepareTrain(self):
    return self.preparePair(self.params['in']['train'][0], self.params['in']['train'][1])

  def prepareTest(self):
    return self.preparePair(self.params['in']['test'][0], self.params['in']['test'][1])

  def train(self, X_train, Y_train, X_test, Y_test):
    if (self.pl is None):
      self.pl = Pipeline([('tfidf', self.vectorizer), ('clf', self.classifier)])
#
    start = time.time()
    self.model = self.pl.fit(X_train, Y_train)
    end = time.time()
    pickle.dump(self.model, open(self.params['out']['model'], 'wb'))
#
    rf_predicted = self.model.predict(X_test)
    rf_validated = rf_predicted == Y_test
    accuracy = np.mean(rf_validated)
#
    logger.info("training takes %f seconds and accuracy is %f" % (end - start, accuracy))
#
    res = {}
    res['elapse'] = end - start
    res['accuracy'] = accuracy
    with open(self.params['out']['metrics'], 'w') as f:
      json.dump(res, f, ensure_ascii=False, indent=2)

  def predict(self, X):
    return self.model.predict(X)

# python3.6 sentiment_analyzer.py params.json

def main():
  sa = SentimentAnalyzer(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain()
  X_test, Y_test = sa.prepareTest()

if __name__ == "__main__":
  main()
