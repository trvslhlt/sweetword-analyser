import random
from prediction_model import PredictionModel


class TravisPredictionModel(object):
    '''
    Subclass and add an instance to PaswordPredictor.getPasswordIndexPrediction list
    '''

    def getPasswordProbabilities(self, sweetwords):
        passwordProbabilities = [0.0] * len(sweetwords)
        randomIndex = random.randint(0, len(sweetwords) - 1)
        passwordProbabilities[randomIndex] = 1.0
        return passwordProbabilities
