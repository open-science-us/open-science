import sys

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

from sklearn.ensemble import RandomForestClassifier

from sentiment_analyzer_gs import SentimentAnalyzerGS

class SentimentAnalyzerGS_RF(SentimentAnalyzerGS):
  def __init__(self, json_fn):
    super().__init__(json_fn)
#
    self.classifier = RandomForestClassifier(random_state=self.params['rf'].get('random_state', None), n_jobs=self.params['rf'].get('n_jobs', None))
    logger.info("RandomForestClassifier\tn_estimators:\t{}".format(self.params['rf'].get('n_estimators', None)))
    logger.info("RandomForestClassifier\tmin_samples_leaf:\t{}".format(self.params['rf'].get('min_samples_leaf', None)))
    logger.info("RandomForestClassifier\tmin_samples_split:\t{}".format(self.params['rf'].get('min_samples_split', None)))
    logger.info("RandomForestClassifier\trandom_state:\t{}".format(self.params['rf'].get('random_state', None)))
    logger.info("RandomForestClassifier\tn_jobs:\t{}".format(self.params['rf'].get('n_jobs', None)))
#
    self.gs_parameters.update({'clf__n_estimators': self.params['rf']['n_estimators'], 'clf__min_samples_split': self.params['rf']['min_samples_split'], 'clf__min_samples_leaf': self.params['rf']['min_samples_leaf']})

# nohup python3.6 sentiment_analyzer_gs_rf.py params_gs_rf.json > sentiment_analyzer_gs_rf.log &

def main():
  sa = SentimentAnalyzerGS_RF(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain()
  X_test, Y_test = sa.prepareTest()
#
  sa.train(X_train, Y_train, X_test, Y_test)

if __name__ == "__main__":
  main()
