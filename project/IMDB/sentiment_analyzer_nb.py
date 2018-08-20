import sys

import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

from sklearn.naive_bayes import MultinomialNB

from sentiment_analyzer import SentimentAnalyzer

class SentimentAnalyzerNB(SentimentAnalyzer):
  def __init__(self, json_fn):
    super().__init__(json_fn)
#
    self.classifier = MultinomialNB(alpha=self.params['nb'].get('alpha', 1.0), fit_prior=self.params['nb'].get('fit_prior', True))
    logger.info("MultinomialNB\talpha:\t{}".format(self.params['nb'].get('alpha', 1.0)))
    logger.info("MultinomialNB\tfit_prior:\t{}".format(self.params['nb'].get('fit_prior', True)))

# python3.6 sentiment_analyzer_nb.py params_nb.json

def main():
  sa = SentimentAnalyzerNB(sys.argv[1])
#
  X_train, Y_train = sa.prepareTrain()
  X_test, Y_test = sa.prepareTest()
#
  sa.train(X_train, Y_train, X_test, Y_test)

if __name__ == "__main__":
  main()
