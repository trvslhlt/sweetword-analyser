import re
import characters as Characters


class Tokenizer(object):

    def __init__(self, caseSensitive=True):
        self._caseSensitive = caseSensitive
        self._tokenClassifier = TokenClassifier(caseInsensitive=False)

    def tokenize(self, s):
        tokens = []
        token = ''
        for c in s:
            if token == '':
                token = c
            else:
                casedC = c if self._caseSensitive else c.lower()
                casedT = token[0] if self._caseSensitive else token[0].lower()
                if Characters.areInSameGroup(casedC, casedT):
                    token += c
                else:
                    tokens.append(token)
                    token = c
        if token != '':
            tokens.append(token)
        tokens = self._combineTitleCaseTokens(tokens)
        return tokens

    def _combineTitleCaseTokens(self, tokens):
        newTokens = tokens
        if len(tokens) <= 1 or not self._caseSensitive:
            return newTokens

        newTokens = []
        hasLastToken = False
        for idx in range(0, len(tokens) - 1):
            currentToken = tokens[idx]
            nextToken = tokens[idx + 1]
            if self._tokenClassifier.isUppercaseToken(currentToken) and self._tokenClassifier.isLowercaseToken(nextToken) and len(currentToken) is 1:
                newTokens.append(currentToken + nextToken)
                hasLastToken = True
            else:
                if hasLastToken:
                    hasLastToken = False
                else:
                    newTokens.append(currentToken)
                hasLastToken = False
        if not hasLastToken:
            newTokens.append(tokens[-1])
        return newTokens





class TokenClassifier(object):

    def __init__(self, caseInsensitive=True):
        self._caseInsensitive = caseInsensitive

    def isDigitToken(self, t):
        digit = Characters.digits[0]
        return Characters.areInSameGroup(t[0], digit)

    def isLetterToken(self, t):
        if self._caseInsensitive:
            t = t.lower()
        letter = Characters.letters[0]
        return Characters.areInSameGroup(t[0], letter)

    def isUppercaseToken(self, t):
        letter = Characters.uppercase_letters[0]
        return Characters.areInSameGroup(t[0], letter)

    def isLowercaseToken(self, t):
        letter = Characters.lowercase_letters[0]
        return Characters.areInSameGroup(t[0], letter)

    def isPunctuationToken(self, t):
        punctuation = Characters.punctuation[0]
        return Characters.areInSameGroup(t[0], punctuation)

    def isPossiblyDate(self, t):
        if not self.isDigitToken(t):
            return False
        if len(t) == 3:
            return self._isPossibleThreeDigitDate(t)
        if len(t) == 4:
            return self._isPossiblyFourDigitDate(t)
        else:
            return False

    def _isPossiblyFourDigitDate(self, t):
        head = int(t[:2])
        tail = int(t[2:])
        if head > 31 or tail > 31:
            return False
        elif head > 12 and tail > 12:
            return False
        elif head is 0 or tail is 0:
            return False
        else:
            return True

    def _isPossibleThreeDigitDate(self, t):
        modifiedTokens = ['0' + t, t[:2] + '0' + t[2]]
        for token in modifiedTokens:
            possibleDate = self._isPossiblyFourDigitDate(token)
            if possibleDate:
                return True
        return False

    def isAscendingDigitSequence(self, t):
        if len(t) <= 1:
            return False
        ints = [int(c) for c in t]
        for n in range(0, len(ints) - 2):
            if (ints[n + 1] - ints[n]) is not 1:
                return False
        return True

    def isWhitespace(self, t):
        for c in t:
            if c not in Characters.whitespace:
                return False
        return True


def isValidPassword(password):
    if not password:
        return False
    allWhitespace = True
    for c in password:
        if c not in Characters.whitespace:
            allWhitespace = False
            break
    if allWhitespace:
        return False
    if ',' in password:
        return False
    return True


def containsSequenceOfDigits(word, length):
    m = re.search('\d{' + str(length) + ',}', word)
    return m is not None
