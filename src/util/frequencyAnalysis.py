from collections import defaultdict
import characters as Characters
import random


class FrequencyAnalyzer:
    def __init__(self, trainingPasswordsAndCounts):
        self.totalNumberDict = defaultdict(int)
        self.characterFrequencyDict = defaultdict(int)
        self.characterProbailityDict = defaultdict(float)
        self.relationFrequencyDict = defaultdict(lambda : defaultdict(int))
        self.analyze(trainingPasswordsAndCounts)
        self.getCharacterProbability('a')


    def analyze(self, trainingPasswordsAndCounts):
        # for each ("password", "12345")
        for password, freqStr in trainingPasswordsAndCounts:
            freq = int(freqStr)
            # for charcter in password
            for idx, ch in enumerate(password):
                self.characterFrequencyDict[ch] += freq
                try:
                    self.totalNumberDict[Characters.getCharacterGroup(ch)] += freq
                    if idx > 0 and password[idx - 1].isalpha() and ch.isalpha():
                        self.relationFrequencyDict[password[idx - 1]][ch] += freq
                except:
                    pass
        self.totalNumberDict[Characters.letters] = self.totalNumberDict[Characters.lowercase_letters] \
            + self.totalNumberDict[Characters.uppercase_letters]
        self.totalNumberDict[Characters.allCharacters] = self.totalNumberDict[Characters.letters] \
            + self.totalNumberDict[Characters.digits] + self.totalNumberDict[Characters.punctuation] \
            + self.totalNumberDict[Characters.whitespace]
        totalLetterCount = float(sum(self.characterFrequencyDict.values()))
        for c, count in self.characterFrequencyDict.iteritems():
            self.characterProbailityDict[c] = count / totalLetterCount


    def getNextPossibleLetter(self, letter):
        if len(self.relationFrequencyDict[letter]) == 0:
            return self.getCharacterBasedOnFrequency(Characters.getCharacterGroup(letter))
        freqSum = sum([self.relationFrequencyDict[letter][nextLetter] for nextLetter in self.relationFrequencyDict[letter]])
        randNum = random.randint(1, freqSum)
        for ch in self.relationFrequencyDict[letter]:
            randNum -= self.relationFrequencyDict[letter][ch]
            if randNum <= 0:
                return ch


    def getCharacterBasedOnFrequency(self, group):
        if self.totalNumberDict[group] == 0:
            return random.choice(group)
        randNum = random.randint(1, self.totalNumberDict[group])
        for ch in group:
            randNum -= self.characterFrequencyDict[ch]
            if randNum <= 0:
                return ch


    def getCharacterProbability(self, character, caseSensitive=False):
        if caseSensitive:
            return self.characterProbailityDict[character]
        else:
            upper = self.characterProbailityDict[character.upper()]
            lower = self.characterProbailityDict[character.lower()]
            return upper + lower

    # def getChracterTransitionProbability(self, firstLetter, secondLetter):
