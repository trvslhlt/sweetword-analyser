import codecs


def readTrainingPasswords(numberOfPasswords=None):
    '''
    by default the password reader will read all of the passwords and counts
    '''
    filename = './input_data/rockyou_top_10000.txt'
    numberOfPasswords = numberOfPasswords if (numberOfPasswords is not None) else -1
    lines = read(filename, numberOfPasswords)
    passwordsWithCounts = []
    for line in lines:
        try:
            passwordWithCount = _convertLineToPasswordWithCount(line)
            passwordsWithCounts.append(passwordWithCount)
        except Exception:
            pass
    return passwordsWithCounts


def _convertLineToPasswordWithCount(line):
    strippedLine = line.strip()
    substrings = strippedLine.split()
    if len(substrings) is not 2:
        raise Exception
    count = substrings[0]
    password = substrings[1]
    return password, count


def read(filename, numberOfLines=-1):
    '''
    if numberOfLines < 0, read all lines
    '''
    lines = []
    f = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
    for line in f:
        if len(lines) >= numberOfLines and numberOfLines >= 0:
            break
        lines.append(line.strip('\n'))
    f.close()
    return lines
