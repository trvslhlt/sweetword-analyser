from collections import defaultdict
from string_descriptions import Tokenizer

class PasswordProcessor(object):

    def __init__(self, passwordsWithCounts):
        self.tokenCountDict = defaultdict(int)
        self.tokenizer = Tokenizer()
        self.processPasswordsAndCounts(passwordsWithCounts)

    def processPasswordsAndCounts(self, passwordsWithCounts):
        for password, count in passwordsWithCounts:
            tokens = self.tokenizer.tokenize(password)
            for token in tokens:
                self.tokenCountDict[token.lower()] += int(count)

    def getTotalTokenFrequencyForWord(self, word):
        tokens = self.tokenizer.tokenize(word)
        totalScore = 0
        for token in tokens:
            tokenScore = self.tokenCountDict[token.lower()]
            totalScore += tokenScore
        return totalScore
