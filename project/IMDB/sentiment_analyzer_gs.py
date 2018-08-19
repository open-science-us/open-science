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
from sklearn.model_selection import GridSearchCV

from sentiment_analyzer import SentimentAnalyzer

class SentimentAnalyzerGS(SentimentAnalyzer):
  def __init__(self, json_fn):
    with open(json_fn) as f:
      params = json.load(f)
#
    vectorizer = TfidfVectorizer(stop_words=params['tfidf'].get('stop_words', None))
    logger.info("TfidfVectorizer\tstop_words:\t{}".format(params['tfidf'].get('stop_words', None)))
    logger.info("TfidfVectorizer\tngram_range:\t{}".format(params['tfidf'].get('ngram_range', None)))
    logger.info("TfidfVectorizer\tuse_idf:\t{}".format(params['tfidf'].get('use_idf', None)))
    logger.info("TfidfVectorizer\tsmooth_idf:\t{}".format(params['tfidf'].get('smooth_idf', None)))
    logger.info("TfidfVectorizer\tsublinear_tf:\t{}".format(params['tfidf'].get('sublinear_tf', None)))
#
    classifier = RandomForestClassifier(random_state=params['rf'].get('random_state', None), n_jobs=params['rf'].get('n_jobs', None))
    logger.info("RandomForestClassifier\tn_estimators:\t{}".format(params['rf'].get('n_estimators', None)))
    logger.info("RandomForestClassifier\tmin_samples_leaf:\t{}".format(params['rf'].get('min_samples_leaf', None)))
    logger.info("RandomForestClassifier\tmin_samples_split:\t{}".format(params['rf'].get('min_samples_split', None)))
    logger.info("RandomForestClassifier\trandom_state:\t{}".format(params['rf'].get('random_state', None)))
    logger.info("RandomForestClassifier\tn_jobs:\t{}".format(params['rf'].get('n_jobs', None)))
#
    self.rf_pl = Pipeline([('tfidf', vectorizer), ('rf', classifier)])
#
    rf_gs_parameters = {'tfidf__ngram_range': params['tfidf']['ngram_range'], 'tfidf__use_idf': params['tfidf']['use_idf'], 'rf__n_estimators': params['rf']['n_estimators'], 'rf__min_samples_split': params['rf']['min_samples_split'], 'rf__min_samples_leaf': params['rf']['min_samples_leaf']}
    self.rf_gs = GridSearchCV(self.rf_pl, rf_gs_parameters, n_jobs=params['rf'].get('n_jobs', None))

  def train(self, X_train, Y_train, X_test, Y_test, rf_model_fn, res_json_fn):
    start = time.time()
    self.rf_model = self.rf_gs.fit(X_train, Y_train)
    end = time.time()
    pickle.dump(self.rf_model, open(rf_model_fn, 'wb'))
#
    rf_predicted = self.rf_model.predict(X_test)
    rf_validated = rf_predicted == Y_test
    accuracy = np.mean(rf_validated)
#
    logger.info("training takes %f seconds and accuracy is %f" % (end - start, accuracy))
#
    res = self.rf_model.best_params_.copy()
    res['elapse'] = end - start
    res['best_score'] = self.rf_model.best_score_
    res['accuracy'] = accuracy
    with open(res_json_fn, 'w') as f:
      json.dump(res, f, ensure_ascii=False)

# nohup python3.6 sentiment_analyzer_gs.py params_gs.json train_pos.txt train_neg.txt test_pos.txt test_neg.txt rf_model_gs.pkl res_gs.json > sentiment_analyzer_gs.log &

def main():
  sa = SentimentAnalyzerGS(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain(sys.argv[2], sys.argv[3])
  X_test, Y_test = sa.prepareTest(sys.argv[4], sys.argv[5])
#
  sa.train(X_train, Y_train, X_test, Y_test, sys.argv[6], sys.argv[7])

if __name__ == "__main__":
  main()
