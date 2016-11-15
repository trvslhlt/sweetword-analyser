import sys
import csv
from password_predictor import PasswordPredictor


def main(sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath):
    sweetwordLists = readSweetwords(sweetwordsListsFilepath, sweetwordListCount, sweetwordsPerList)
    passwordIndices = getPasswordIndicesForSweetwordLists(sweetwordLists)
    outputIndices = getFormattedIndicesForOutput(passwordIndices)
    print outputIndices


def readSweetwords(sweetwordsListsFilepath, expectedListCount, expectedSweetwordsPerList):
    sweetwordLists = []
    with open(sweetwordsListsFilepath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            assert len(row) is expectedSweetwordsPerList, 'The number of sweetwords in the list was unexpected'
            sweetwordLists.append(row)
    assert len(sweetwordLists) is expectedListCount, 'The number of sweetword lists was unexpected'
    return sweetwordLists


def getPasswordIndicesForSweetwordLists(sweetwordLists):
    passwordIndices = []
    pp = PasswordPredictor()
    for sweetwordList in sweetwordLists:
        passwordIndices.append(pp.getPasswordIndexPrediction(sweetwordList))
    return passwordIndices

def getFormattedIndicesForOutput(indices):
    return ','.join([str(i) for i in indices])

if __name__ == '__main__':
    assert len(sys.argv) is 4, 'Args: number of lists, sweetwords per list, sweetword list filepath'
    [_, sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath] = sys.argv
    main(int(sweetwordListCount), int(sweetwordsPerList), sweetwordsListsFilepath)
