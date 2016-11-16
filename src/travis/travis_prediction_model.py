import random
from prediction_model import PredictionModel
from util import word_statistics as WS


class TravisPredictionModel(object):
    '''
    Subclass and add an instance to PaswordPredictor.getPasswordIndexPrediction list
    '''

    def getPasswordProbabilities(self, sweetwords):
        # return methodA(sweetwords)
        return methodB(sweetwords)


def methodA(sweetwords):
    passwordProbabilities = [0.0] * len(sweetwords)
    randomIndex = random.randint(0, len(sweetwords) - 1)
    passwordProbabilities[randomIndex] = 1.0
    return passwordProbabilities


def methodB(sweetwords):
    scores = getMedianBasedScores(sweetwords)
    return getProbabilitiesFromScores(scores)


def getMedianBasedScores(sweetwords):
    medianWord = WS.getMedianWord(sweetwords)
    diffCounts = WS.getIndexSensitiveCharacterDiffCount(medianWord, sweetwords)
    scores = []
    minDiffCount = min(diffCounts)
    for diffCount in diffCounts:
        if diffCount == minDiffCount:
            scores.append(100)
        else:
            scores.append(0)
    return scores


def getProbabilitiesFromScores(scores):
    totalScores = sum(scores)
    return [float(s) / totalScores for s in scores]
