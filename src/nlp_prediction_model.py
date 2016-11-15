from prediction_model import PredictionModel
import util.nlp as nlp
import re


class NLPPredictionModel(object):

    def getPasswordProbabilities(self, sweetwordList):
        # can not deal with sweetword that contains no letters

        result = []
        for s in sweetwordList:
            words = re.findall(r"[a-zA-Z']+", s)
            if not words:
                result.append(0.0)
            else:
                result.append(sum([nlp.getScore(w) for w in words]) / float(len(words)))
        sum_result = sum(result)
        return [r / float(sum_result) for r in result]
