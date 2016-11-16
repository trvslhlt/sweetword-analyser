import statistics


paddingCharacter = '*'


def getMedianWordLength(words):
    lengths = map(lambda x: len(x), words)
    return statistics.median(lengths)


def getMedianWord(words):
    maxWordLength = reduce(lambda currentMax, w: max(currentMax, w), map(lambda w: len(w), words))
    lettersAtIndexLists = [[] for _ in range(0, maxWordLength)]
    for word in words:
        while len(word) < maxWordLength:
            word += paddingCharacter
        for letterIdx in range(0, maxWordLength):
            letter = word[letterIdx]
            lettersAtIndexLists[letterIdx].append(word[letterIdx])
    medianWord = []
    for letterList in lettersAtIndexLists:
        letter = getMostCommonElement(letterList)
        medianWord.append(letter)
    return ''.join(medianWord)


def getIndexSensitiveCharacterDiffCount(comparisonWord, words):
    diffCounts = []
    for word in words:
        diffCount = 0
        while len(word) > len(comparisonWord):
            diffCount += 1
            word = word[:-1]
        while len(word) < len(comparisonWord):
            word += paddingCharacter
        for letterIdx in range(0, len(comparisonWord)):
            if word[letterIdx] != comparisonWord[letterIdx]:
                diffCount += 1
        diffCounts.append(diffCount)
    return diffCounts

# can be split to more general util if needed
def getMostCommonElement(l):
    return max(set(l), key=l.count)
