import sys
import time
import numpy as np
import re
import json
import pickle

import logging
logger = logging.getLogger(__name__)
logger_hdlr = logging.StreamHandler(sys.stdout)
logger_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logger_hdlr.setLevel(logging.INFO)
logger.addHandler(logger_hdlr)
logger.setLevel(logging.INFO)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

class SentimentAnalyzer():
  def __init__(self, json_fn):
    with open(json_fn) as f:
      params = json.load(f)
#
    nr = params['tfidf'].get('ngram_range', None)
    if (nr is None):
      nr = (1,1)
    else:
      nr = tuple(nr)
    vectorizer = TfidfVectorizer(stop_words=params['tfidf'].get('stop_words', None), ngram_range=nr, use_idf=params['tfidf'].get('use_idf', None), smooth_idf=params['tfidf'].get('smooth_idf', None), sublinear_tf=params['tfidf'].get('sublinear_tf', None))
    logger.info("TfidfVectorizer\tstop_words:\t{}".format(params['tfidf'].get('stop_words', None)))
    logger.info("TfidfVectorizer\tngram_range:\t{}".format(nr))
    logger.info("TfidfVectorizer\tuse_idf:\t{}".format(params['tfidf'].get('use_idf', None)))
    logger.info("TfidfVectorizer\tsmooth_idf:\t{}".format(params['tfidf'].get('smooth_idf', None)))
    logger.info("TfidfVectorizer\tsublinear_tf:\t{}".format(params['tfidf'].get('sublinear_tf', None)))
#
    classifier = RandomForestClassifier(n_estimators=params['rf'].get('n_estimators', None), min_samples_leaf=params['rf'].get('min_samples_leaf', None), min_samples_split=params['rf'].get('min_samples_split', None), random_state=params['rf'].get('random_state', None), n_jobs=params['rf'].get('n_jobs', None))
    logger.info("RandomForestClassifier\tn_estimators:\t{}".format(params['rf'].get('n_estimators', None)))
    logger.info("RandomForestClassifier\tmin_samples_leaf:\t{}".format(params['rf'].get('min_samples_leaf', None)))
    logger.info("RandomForestClassifier\tmin_samples_split:\t{}".format(params['rf'].get('min_samples_split', None)))
    logger.info("RandomForestClassifier\trandom_state:\t{}".format(params['rf'].get('random_state', None)))
    logger.info("RandomForestClassifier\tn_jobs:\t{}".format(params['rf'].get('n_jobs', None)))
#
    self.rf_pl = Pipeline([('tfidf', vectorizer), ('rf', classifier)])

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

  def prepareTrain(self, train_pos_fn, train_neg_fn):
    return self.preparePair(train_pos_fn, train_neg_fn)

  def prepareTest(self, test_pos_fn, test_neg_fn):
    return self.preparePair(test_pos_fn, test_neg_fn)

  def train(self, X_train, Y_train, X_test, Y_test, rf_model_fn, res_json_fn):
    start = time.time()
    self.rf_model = self.rf_pl.fit(X_train, Y_train)
    end = time.time()
    pickle.dump(self.rf_model, open(rf_model_fn, 'wb'))
#
    rf_predicted = self.rf_model.predict(X_test)
    rf_validated = rf_predicted == Y_test
    accuracy = np.mean(rf_validated)
#
    logger.info("training takes %f seconds and accuracy is %f" % (end - start, accuracy))
#
    res = {}
    res['elapse'] = end - start
    res['accuracy'] = accuracy
    with open(res_json_fn, 'w') as f:
      json.dump(res, f, ensure_ascii=False)

  def predict(self, X):
    return self.rf_model.predict(X)

# python3.6 sentiment_analyzer.py params.json train_pos.txt train_neg.txt test_pos.txt test_neg.txt rf_pl.pkl res.json

def main():
  sa = SentimentAnalyzer(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain(sys.argv[2], sys.argv[3])
  X_test, Y_test = sa.prepareTest(sys.argv[4], sys.argv[5])
#
  sa.train(X_train, Y_train, X_test, Y_test, sys.argv[6], sys.argv[7])

if __name__ == "__main__":
  main()
