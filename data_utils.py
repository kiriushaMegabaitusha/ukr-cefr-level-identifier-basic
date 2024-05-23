import pandas as pd
from tokenize_uk.tokenize_uk import tokenize_words, tokenize_sents
import pymorphy2
from tqdm import tqdm

morph = pymorphy2.MorphAnalyzer(lang='uk')

def create_sentence_table(text):
    sents = tokenize_sents(text)
    df = pd.DataFrame(sents, columns=['sentence'])
    # count words in sentence
    word_count_list = []
    for sent in tqdm(sents, desc='Calculating word count in sentences'):
        word_count_list.append(len(tokenize_words(sent)))
    df = df.insert(1, 'word_count', word_count_list)
    return df


def count_ukr_syllables(text):
    '''
    calculates the number of syllables (for ukrainian language) in a given text string
    :param text: string object
    :return: syllable count (integer)
    '''
    syllables = 0
    for char in text:
        if char in 'аеіоуиїяєю':
            syllables += 1
    return syllables

def create_word_table(text):
    '''

    :param text:
    :return: df containing all tokens from text and their linguistic text parameters
    '''
    tokens = tokenize_words(text)
    # get gramemes, lemmas, lengths, syllable count
    grameme_list = []
    lemma_list = []
    word_len_list = []
    syllable_count_list = []
    for token in tqdm(tokens, desc='Creating word table'):
        grameme_list.append(morph.parse(token)[0].tag)
        lemma_list.append(morph.parse(token)[0].normal_form)
        word_len_list.append(len(token))
        syllable_count_list.append(count_ukr_syllables(token))

    return pd.DataFrame({'token': tokens, 'lemma': lemma_list, 'grameme': grameme_list, 'word_len': word_len_list, 'syllable_count': syllable_count_list})

