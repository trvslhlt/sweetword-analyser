import numpy as np
# from prediction_model import PredictionModel
from travis.travis_prediction_model import TravisPredictionModel
from nlp_prediction_model import NLPPredictionModel

class PasswordPredictor(object):

    def getPasswordIndexPrediction(self, sweetwordList):
        preliminaryPasswordProbabilities = []

        predictionModels = [TravisPredictionModel(), NLPPredictionModel()]
        for predictionModel in predictionModels:
            predictions = predictionModel.getPasswordProbabilities(sweetwordList)
            if len(predictions) != len(sweetwordList):
                print('prediction model:', predictionModel)
                print('prediction count:', len(predictions))
                assert False, 'Password prediction count does not match sweetword list length'
            predictionSum = sum(predictions)
            if predictionSum < 0.99 or 1.01 < predictionSum:
                print('prediction model:', predictionModel)
                print('prediction sum:', predictionSum)
                assert False, 'Password predictions do not sum to 1'
            preliminaryPasswordProbabilities.append(predictions)

        passwordProbabilities = self._getReconciledPasswordProbabilities(preliminaryPasswordProbabilities)
        return np.argmax(passwordProbabilities)

    def _getReconciledPasswordProbabilities(self, preliminaryPasswordIndexPredictions):
        # strategies
        # - variance across prediction list
        #   discard extrema
        #   choose max or min
        # - look for consensus (how to combine this with likelihood?)
        # - pick higest p across the predictions
        # - choose random
        # - (add a confidence rating to the predictions?)
        return preliminaryPasswordIndexPredictions[0]
