import random
from prediction_model import PredictionModel
from util.password_processor import PasswordProcessor
from util import word_statistics as WS
from util import passwordReader as PR
import util.frequencyAnalysis
from util.frequencyAnalysis import FrequencyAnalyzer as FA


class TravisPredictionModel(object):

    def getPasswordProbabilities(self, sweetwords):
        methodsAndWeights = [
            (randomWinnerMethod, 8),
            (indexInsensitiveMedianMethod, 16),
            (averageCharacterFrequencyMethod, 32),
            (averageCharacterTransitionFrequencyMethod, 32),
            (wordLengthLikelihoodMethod, 64),
            (tokenMatchScoreMethod, 64)
        ]
        totalScores = [0] * len(sweetwords)
        for method, weight in methodsAndWeights:
            scores = method(sweetwords)
            for wordIdx in range(0, len(sweetwords)):
                totalScores[wordIdx] += scores[wordIdx] * weight
        ps = getProbabilitiesFromScores(totalScores)
        return ps


def tokenMatchScoreMethod(sweetwords):
    '''
    Assign ps for matching password tokens
    '''
    passwordsWithCounts = PR.readTrainingPasswords()
    passwordProcessor = PasswordProcessor(passwordsWithCounts)
    scores = []
    for word in sweetwords:
        score = passwordProcessor.getTotalTokenFrequencyForWord(word)
        scores.append(score)
    return getProbabilitiesFromScores(scores)


def wordLengthLikelihoodMethod(sweetwords):
    '''
    Assign ps based on sweetword length
    '''
    passwordsWithCounts = PR.readTrainingPasswords()
    frequencyAnalyzer = FA(passwordsWithCounts)
    ps = []
    for word in sweetwords:
        p = frequencyAnalyzer.getWordLengthProbability(word)
        ps.append(p)
    return getProbabilitiesFromScores(ps)


def averageCharacterTransitionFrequencyMethod(sweetwords):
    '''
    Assign probabilities based on avg character transition probability
    '''
    passwordsWithCounts = PR.readTrainingPasswords()
    frequencyAnalyzer = FA(passwordsWithCounts)
    avgPs = []
    for word in sweetwords:
        if len(word) == 0:
            avgPs.append(.001)
        else:
            transitionsPs = []
            for chIdx in range(0, len(word) - 1):
                firstCh, secondCh = word[chIdx], word[chIdx + 1]
                transitionP = frequencyAnalyzer.getCharacterTransitionProbability(firstCh, secondCh)
                transitionsPs.append(transitionP)
            avgPs.append(sum(transitionsPs) / len(word))
    return getProbabilitiesFromScores(avgPs)


def averageCharacterFrequencyMethod(sweetwords):
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


def indexInsensitiveMedianMethod(sweetwords):
    scores = getIndexSensitiveMedianBasedScores(sweetwords)
    return getProbabilitiesFromScores(scores)


def randomWinnerMethod(sweetwords):
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
