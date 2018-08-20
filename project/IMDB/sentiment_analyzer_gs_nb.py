import sys
import json

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

from sklearn.naive_bayes import MultinomialNB

from sentiment_analyzer_gs import SentimentAnalyzerGS

class SentimentAnalyzerGS_NB(SentimentAnalyzerGS):
  def __init__(self, json_fn):
    super().__init__(json_fn)
#
    self.classifier = MultinomialNB()
    logger.info("MultinomialNB\talpha:\t{}".format(self.params['nb'].get('alpha', None)))
    logger.info("MultinomialNB\tfit_prior:\t{}".format(self.params['nb'].get('fit_prior', None)))
#
    self.gs_parameters.update({'clf__alpha': self.params['nb']['alpha'], 'clf__fit_prior': self.params['nb']['fit_prior']})

# nohup python3.6 sentiment_analyzer_gs_nb.py params_gs_nb.json > sentiment_analyzer_gs_nb.log &

def main():
  sa = SentimentAnalyzerGS_NB(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain()
  X_test, Y_test = sa.prepareTest()
#
  sa.train(X_train, Y_train, X_test, Y_test)

if __name__ == "__main__":
  main()
