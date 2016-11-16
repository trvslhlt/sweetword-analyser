import random
from prediction_model import PredictionModel
from util import word_statistics as WS
from util import passwordReader as PR
import util.frequencyAnalysis
from util.frequencyAnalysis import FrequencyAnalyzer as FA


class TravisPredictionModel(object):
    '''
    Subclass and add an instance to PaswordPredictor.getPasswordIndexPrediction list
    '''


    def getPasswordProbabilities(self, sweetwords):
        # return methodA(sweetwords)
        # return methodB(sweetwords)
        return methodC(sweetwords)


def methodC(sweetwords):
    '''
    Assign probabilities based on avg character probability
    '''
    passwordsWithCounts = PR.readTrainingPasswords()
    frequencyAnalyzer = FA(passwordsWithCounts)
    avgPs = []
    for word in sweetwords:
        chPs = map(lambda ch: frequencyAnalyzer.getCharacterProbability(ch), word)
        avgP = sum(chPs) / len(word)
        avgPs.append(avgP)
    return getProbabilitiesFromScores(avgPs)


def methodB(sweetwords):
    scores = getIndexSensitiveMedianBasedScores(sweetwords)
    return getProbabilitiesFromScores(scores)


def methodA(sweetwords):
    '''
    Assign p of 1 to a random sweetword. Base case
    '''
    passwordProbabilities = [0.0] * len(sweetwords)
    randomIndex = random.randint(0, len(sweetwords) - 1)
    passwordProbabilities[randomIndex] = 1.0
    return passwordProbabilities


def getIndexSensitiveMedianBasedScores(sweetwords):
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
