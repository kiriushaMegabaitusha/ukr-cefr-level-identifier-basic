import pandas as pd
from tokenize_uk.tokenize_uk import tokenize_words, tokenize_sents
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='uk')

def sentence_subdivide(text):
    sents = tokenize_sents(text)
    df = pd.DataFrame(sents, columns=['sentence'])

def count_ukr_syllables(text):
    '''
    calculates the number of syllables (for ukrainian language) in a give text string
    :param text: string object
    :return: syllable count (integer)
    '''
    syllables = 0
    for char in text:
        if char in 'аеіоуиїяєю':
            syllables += 1
    return syllables

def word_subdivide(text):
    '''

    :param text:
    :return: df containing all words from text and their linguistic text parameters
    '''
    tokens = tokenize_words(text)
    # get gramemes, lemmas, lengths, syllable count
    grameme_list = []
    lemma_list = []
    word_len_list = []
    syllable_count_list = []
    for token in tokens:
        grameme_list.append(morph.parse(token)[0].tag)
        lemma_list.append(morph.parse(token)[0].normal_form)
        word_len_list.append(len(token))
        syllable_count_list.append(count_ukr_syllables(token))

    return pd.DataFrame({'token': tokens, 'grameme': grameme_list, 'lemma': lemma_list})

