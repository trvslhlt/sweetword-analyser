import numpy as np
import random

class PasswordPredictor(object):

    def getPasswordIndexPrediction(self, sweetwordList):
        preliminaryPasswordProbabilities = []

        predictionModels = [PredictionModel()]
        for predictionModel in predictionModels:
            predictions = predictionModel.getPasswordProbabilities(sweetwordList)
            if len(predictions) is not len(sweetwordList):
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
        return preliminaryPasswordIndexPredictions[0]

class PredictionModel(object):
    '''
    Subclass and add an instance to PaswordPredictor.getPasswordIndexPrediction list
    '''

    def getPasswordProbabilities(self, sweetwords):
        passwordProbabilities = [0.0] * len(sweetwords)
        randomIndex = random.randint(0, len(sweetwords) - 1)
        passwordProbabilities[randomIndex] = 1.0
        return passwordProbabilities
