import string


lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
letters = lowercase_letters + uppercase_letters
digits = string.digits
punctuation = string.punctuation
punctuation = punctuation.replace(',', '')
whitespace = ' '#string.whitespace <- don't know how to handle some of the new-line-ish characters
allStandardCharacters = lowercase_letters + uppercase_letters + digits + punctuation + whitespace
allCharacters = allStandardCharacters


def getCharacterGroup(character):
    if character in lowercase_letters:
        return lowercase_letters
    elif character in uppercase_letters:
        return uppercase_letters
    elif character in digits:
        return digits
    elif character in punctuation:
        return punctuation
    elif character in whitespace:
        return whitespace
    else:
        raise Exception('character case not handled')


def areInSameGroup(a, b):
    aGroup = getCharacterGroup(a)
    bGroup = getCharacterGroup(b)
    return aGroup == bGroup


# def getCharacterGroupName(c):
#     group = getCharacterGroup(c)
#
#     if group == lowercase_letters:
#         return 'lowercase_letters'
#     elif group == uppercase_letters:
#         return 'uppercase_letters'
#     elif group == digits:
#         return 'digits'
#     elif group == punctuation:
#         return 'punctuation'
#     elif group == whitespace:
#         return 'whitespace'


# def getRemainingStandardCharacters(characterGroups):
#     standardAscii = [chr(i) for i in range(0, 127)]
#     remainingStandardCharacters = ''.join(standardAscii)
#     for characterGroup in characterGroups:
#         for character in characterGroup:
#             remainingStandardCharacters = remainingStandardCharacters.replace(character, '')
#     return str(remainingStandardCharacters)
