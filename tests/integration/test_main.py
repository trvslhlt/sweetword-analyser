import sys

# GOALS:
# validate program interface
# - input: python your_program.py m n filename
# - output: ???


def main():
    print('main')


if __name__ == '__main__':
    assert len(sys.argv) is 2, 'Please pass in the path to your sweetword analyser (and nothing else).'
    main()
