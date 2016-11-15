import sys
import csv


def main(sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath):
    sweetwordLists = readSweetwords(sweetwordsListsFilepath, sweetwordListCount, sweetwordsPerList)
    passwordIndices = getPasswordIndicesForSweetwordLists(sweetwordLists)
    print(passwordIndices)


def readSweetwords(sweetwordsListsFilepath, expectedListCount, expectedSweetwordsPerList):
    print(expectedListCount, expectedSweetwordsPerList)
    sweetwordLists = []
    with open(sweetwordsListsFilepath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            print len(row), expectedSweetwordsPerList
            assert len(row) is expectedSweetwordsPerList, 'The number of sweetwords in the list was unexpected'
            sweetwordLists.append(row)
    print len(sweetwordLists)
    assert len(sweetwordLists) is expectedListCount, 'The number of sweetword lists was unexpected'
    return sweetwordLists


def getPasswordIndicesForSweetwordLists(sweetwordLists):
    passwordIndices = []
    for sweetwordList in sweetwordLists:
        passwordIndices.append(0)
    return passwordIndices


if __name__ == '__main__':
    assert len(sys.argv) is 4, 'Args: number of lists, sweetwords per list, sweetword list filepath'
    [_, sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath] = sys.argv
    main(int(sweetwordListCount), int(sweetwordsPerList), sweetwordsListsFilepath)
