import sys
import tempfile
import random
import os
import subprocess
import codecs
import csv

# GOALS:
# validate program interface
# - input: python your_program.py m n filename
# - output: ???

sweetwordLists = [
    ['notThePassword', 'maybeThePassword', 'definitelyThePassword'],
    ['Monday', 'Tuseday', 'Wednesday'],
    ['colorless', 'green', 'ideas']
]

sweewordListCount = len(sweetwordLists)
sweetwordsInList = len(sweetwordLists[0])

def main():
    #create a temp directory
    tempDirectoryPath = tempfile.gettempdir() + '/' + str(random.randint(0,9999999))
    print('tempDirectoryPath:', tempDirectoryPath)
    os.mkdir(tempDirectoryPath)

    # create sample sweetwords list file
    sweetwordsListsFilepath = tempDirectoryPath + '/sweetwords.csv'
    with open(sweetwordsListsFilepath, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(sweetwordLists)





if __name__ == '__main__':
    assert len(sys.argv) is 2, 'Please pass in the path to your sweetword analyser (and nothing else).'
    main()
