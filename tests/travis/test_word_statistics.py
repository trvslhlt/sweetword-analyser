from src.util import word_statistics as WS


def test_get_median_word_length():
    words = ['1', '22', '22', '333']
    median = WS.getMedianWordLength(words)
    assert(median == 2)


def test_get_most_common_element():
    l = [1, 1, 2]
    e = WS.getMostCommonElement(l)
    assert(e == 1)


def test_get_median_word_from_words_of_equal_length():
    words = ['ab_', 'a_c', '_bc']
    medianWord = WS.getMedianWord(words)
    assert(medianWord == 'abc')


def test_get_median_word_from_words_of_equal_length():
    words = ['_X', '_', '_']
    medianWord = WS.getMedianWord(words)
    assert(medianWord == '_' + WS.paddingCharacter)


def test_get_index_sensitive_character_diff_count():
    comparisonWord = 'abcde'
    words = ['', 'xxxxx', 'abcde', 'abcdex', 'xabcde']
    expectedDiffCounts = [5, 5, 0, 1, 6]
    actualDiffCounts = WS.getIndexSensitiveCharacterDiffCount(comparisonWord, words)
    assert(expectedDiffCounts == actualDiffCounts)
