def ARI_index(sent_count, word_count, char_count):
    """
    Calculate ARI index from sentence count and word count and character count.
    :param sent_count: integer, total number of sentences
    :param word_count: integer, total number of words
    :param char_count: integer, total number of characters
    :return: integer, ARI index
    """
    return 4.71 * (char_count / word_count) + 0.5 * (word_count / sent_count) - 21.43


def Flesh_Kincaid_grade_level(sentence_count, word_count, syllable_count):
    """
    Calculate Flesh Kincaid grade level.
    :param sentence_count: integer, total number of sentences
    :param word_count: integer, total number of words
    :param syllable_count: integer, total number of syllables
    :return: integer, Flesh Kincaid grade level
    """
    return 0.39 * (word_count / sentence_count) + 11.8 * (syllable_count / word_count) - 15.59


def interpret_ARI(index):
    rounded_index = round(index)
    if rounded_index == 2 or rounded_index == 1:
        return 'A1'
    elif rounded_index == 3 or rounded_index == 4:
        return 'A2'
    elif rounded_index == 5 or rounded_index == 6 or rounded_index == 7:
        return 'B1'
    elif rounded_index == 8 or rounded_index == 9 or rounded_index == 10:
        return 'B2'
    elif rounded_index == 11 or rounded_index == 12:
        return 'C1'
    elif rounded_index == 13 or rounded_index == 14:
        return 'C2'
    else:
        return '?'


def interpret_Flesh_Kincaid_grade(index):
    if index < 3:
        return 'A1'
    elif index < 6:
        return 'A2'
    elif index < 9:
        return 'B1'
    elif index < 12:
        return 'B2'
    elif index < 15:
        return 'C1'
    else:
        return 'C2'
