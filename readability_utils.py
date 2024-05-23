def ARI_index(sent_count, word_count, char_count):
    '''
    Calculate ARI index from sentence count and word count and character count.
    :param sent_count: integer, total number of sentences
    :param word_count: integer, total number of words
    :param char_count: integer, total number of characters
    :return: ARI index, integer
    '''
    return 4.71 * (char_count / word_count) + 0.5 * (word_count / sent_count) - 21.43

def Flesh_Kincaid_grade_level(sentence_count, word_count, syllable_count):
    return 0.39 * (word_count / sentence_count) + 11.8 * (syllable_count / word_count) - 15.59