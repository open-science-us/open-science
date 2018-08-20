import sys

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

from sklearn.ensemble import RandomForestClassifier

from sentiment_analyzer import SentimentAnalyzer

class SentimentAnalyzerRF(SentimentAnalyzer):
  def __init__(self, json_fn):
    super().__init__(json_fn)
#
    self.classifier = RandomForestClassifier(n_estimators=self.params['rf'].get('n_estimators', 100), min_samples_leaf=self.params['rf'].get('min_samples_leaf', 1), min_samples_split=self.params['rf'].get('min_samples_split', 2), random_state=self.params['rf'].get('random_state', 42), n_jobs=self.params['rf'].get('n_jobs', -1))
    logger.info("RandomForestClassifier\tn_estimators:\t{}".format(self.params['rf'].get('n_estimators', 100)))
    logger.info("RandomForestClassifier\tmin_samples_leaf:\t{}".format(self.params['rf'].get('min_samples_leaf', 1)))
    logger.info("RandomForestClassifier\tmin_samples_split:\t{}".format(self.params['rf'].get('min_samples_split', 2)))
    logger.info("RandomForestClassifier\trandom_state:\t{}".format(self.params['rf'].get('random_state', 42)))
    logger.info("RandomForestClassifier\tn_jobs:\t{}".format(self.params['rf'].get('n_jobs', -1)))

# python3.6 sentiment_analyzer_rf.py params_rf.json

def main():
  sa = SentimentAnalyzerRF(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain()
  X_test, Y_test = sa.prepareTest()
#
  sa.train(X_train, Y_train, X_test, Y_test)

if __name__ == "__main__":
  main()
