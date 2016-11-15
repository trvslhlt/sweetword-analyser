import enchant
import re

def containsWords(s):
    if len(s) == 1 and s.isalpha():
        return True
    d = enchant.Dict("en_US")
    s = s.lower()
    for start in range(len(s) - 1):
        for end in range(start + 2, len(s) + 1):
            if d.check(s[start:end]):
                return True
    return False


def containsAllWords(s):
    d = enchant.Dict("en_US")
    s = s.lower()
    checked = set()
    def helper(s):
        if len(s) == 1 and s.isalpha():
            return True
        if d.check(s):
            return True
        for end in range(2, len(s) + 1):
            if d.check(s[:end]) and not s[end:] in checked and helper(s[end:]):
                return True
        checked.add(s)
        return False
    return helper(s)
    

def getScore(s):
    d = enchant.Dict("en_US")
    s = s.lower()
    score_dict = {}
    def helper(s):
        if len(s) == 0:
            return 0
        if s in score_dict:
            return score_dict[s]
        if d.check(s):
            score_dict[s] = len(s)
            return len(s)
        scores = []
        for start_idx in range(len(s) - 1):
            for end_idx in range(start_idx + 2, len(s) + 1):
                if d.check(s[start_idx:end_idx]):
                    score = (end_idx - start_idx) + helper(s[end_idx:])
                    scores.append(score)
        return max(scores) if scores else 0
    return helper(s) / float(len(s)) if len(s) > 0 else 0.0


def getProbabilities(sweetwords):
    # can not deal with sweetword that contains no letters
    result = []
    for s in sweetwords:
        words = re.findall(r"[a-zA-Z']+", s)
        if not words:
            result.append(0.0)
        else:
            result.append(sum([getScore(w) for w in words]) / float(len(words)))
    return result
