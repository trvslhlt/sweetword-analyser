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
sweetwordListCount = len(sweetwordLists)
sweetwordsPerList = len(sweetwordLists[0])


def main(programFilepath):
    # make sure the program exists
    assert os.path.isfile(programFilepath), 'The program does not exists at the provided filepath.'

    #create a temp directory
    tempDirectoryPath = tempfile.gettempdir() + '/' + str(random.randint(0,9999999))
    print('tempDirectoryPath:', tempDirectoryPath)
    os.mkdir(tempDirectoryPath)

    # create sample sweetwords list file
    sweetwordsListsFilepath = tempDirectoryPath + '/sweetwords.csv'
    with open(sweetwordsListsFilepath, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(sweetwordLists)

    # run the program
    # python your_program.py m n filename
    command = 'python ' + programFilepath + ' ' + str(sweetwordListCount) + ' ' + str(sweetwordsPerList) + ' ' + sweetwordsListsFilepath
    print('----------- running ------------')
    print(command)
    # result = subprocess.call([command], shell=True)
    output = subprocess.check_output(
        command,
        stderr=subprocess.STDOUT,
        shell=True)
    print('----------- complete -----------')
    # print(result)
    print(output)
    print('++++')

    # check if password guess file exists
    # assert os.path.isfile(passwordsFilepath), 'The program did not output a '






if __name__ == '__main__':
    assert len(sys.argv) is 2, 'Please pass in the path to your sweetword analyser (and nothing else).'
    programFilepath = sys.argv[1]
    main(programFilepath)
