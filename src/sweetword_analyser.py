import sys
import csv


def main(sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath):
    sweetwordLists = readSweetwords(sweetwordsListsFilepath)
    print(sweetwordLists)
    # passwordIndices = getPasswordIndicesForSweetwordLists(sweetwordsLists)
    # print(passwordIndices)


def readSweetwords(sweetwordsListsFilepath):
    sweetwordsLists = []
    with open(sweetwordsListsFilepath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            sweetwords = row.split(',')
            sweetwordLists.append(sweetwords)
    return sweetwordsLists


def getPasswordIndicesForSweetwordLists(sweetwordLists):
    return passwordIndices


if __name__ == '__main__':
    assert len(sys.argv) is 4, 'Args: number of lists, sweetwords per list, sweetword list filepath'
    [_, sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath] = sys.argv
    main(sweetwordListCount, sweetwordsPerList, sweetwordsListsFilepath)
