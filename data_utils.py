import pandas as pd
from tokenize_uk import tokenize_words, tokenize_sents
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='uk')

def sentence_subdivide(text):
    sents = tokenize_sents(text)
    df = pd.DataFrame(sents, columns=['sentence'])

def word_subdivide(text):
    '''

    :param text:
    :return: df containing all words and their grammemes and lemmas
    '''
    tokens = tokenize_words(text)
    # get gramemes
    grameme_list = []
    for token in tokens:
        grameme_list.append(morph.parse(token)[0].tag)
    # get lemmas
    lemma_list = []
    for token in tokens:
        lemma_list.append(morph.parse(token)[0].normal_form)
    return pd.DataFrame({'token': tokens, 'grameme': grameme_list, 'lemma': lemma_list})

