import sys
import time
import json
import pickle

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from sentiment_analyzer import SentimentAnalyzer

class SentimentAnalyzerGS(SentimentAnalyzer):
  def __init__(self, json_fn):
    with open(json_fn) as f:
      self.params = json.load(f)
#
    self.vectorizer = TfidfVectorizer(stop_words=self.params['tfidf'].get('stop_words', None))
    logger.info("TfidfVectorizer\tstop_words:\t{}".format(self.params['tfidf'].get('stop_words', None)))
    logger.info("TfidfVectorizer\tngram_range:\t{}".format(self.params['tfidf'].get('ngram_range', None)))
    logger.info("TfidfVectorizer\tuse_idf:\t{}".format(self.params['tfidf'].get('use_idf', None)))
    logger.info("TfidfVectorizer\tsmooth_idf:\t{}".format(self.params['tfidf'].get('smooth_idf', None)))
    logger.info("TfidfVectorizer\tsublinear_tf:\t{}".format(self.params['tfidf'].get('sublinear_tf', None)))
#
    self.gs_parameters = {'tfidf__ngram_range': self.params['tfidf']['ngram_range'], 'tfidf__use_idf': self.params['tfidf']['use_idf'], 'tfidf__smooth_idf': self.params['tfidf']['smooth_idf'], 'tfidf__sublinear_tf': self.params['tfidf']['sublinear_tf']}

  def train(self, X_train, Y_train, X_test, Y_test):
    if (self.gs is None):
      self.pl = Pipeline([('tfidf', self.vectorizer), ('clf', self.classifier)])
      self.gs = GridSearchCV(self.pl, self.gs_parameters, n_jobs=self.params['gs'].get('n_jobs', None))
#
    start = time.time()
    self.model = self.gs.fit(X_train, Y_train)
    end = time.time()
    pickle.dump(self.model, open(self.params['out']['model'], 'wb'))
#
    rf_predicted = self.model.predict(X_test)
    rf_validated = rf_predicted == Y_test
    accuracy = np.mean(rf_validated)
#
    logger.info("training takes %f seconds and accuracy is %f" % (end - start, accuracy))
#
    res = self.model.best_params_.copy()
    res['elapse'] = end - start
    res['best_score'] = self.model.best_score_
    res['accuracy'] = accuracy
    with open(self.params['out']['metrics'], 'w') as f:
      json.dump(res, f, ensure_ascii=False, indent=2)

# python3.6 sentiment_analyzer_gs.py params_gs.json

def main():
  sa = SentimentAnalyzerGS(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain()
  X_test, Y_test = sa.prepareTest()

if __name__ == "__main__":
  main()
