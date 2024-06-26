# dictionary of grammemes

grammemes_dict = {
    'A1': [['NOUN', 'sing'], ['NOUN', 'plur', 'nomn'], ['NOUN', 'accs', 'sing'], ['NOUN', 'loct', 'sing'],
           ['NOUN', 'voct'], ['ADJF', 'sing'], ['ADJF', 'plur'], ['ADJF', 'nomn'], ['ADJF', 'accs'], ['ADJF', 'loct'],
           ['NPRO', 'pers'], ['NPRO'], ['VERB', 'plur'], ['VERB', 'perf', 'futr'], ['VERB', 'impr']],
    'A2': [['NOUN'], ['ADJF', 'sing'], ['ADJF', 'plur'], ['NPRO', 'pers'], ['NPRO'], ['VERB', 'pres'], ['VERB', 'pres'],
           ['VERB', 'past'], ['VERB', 'futr'], ['ADJF', 'COMP'], ['ADJF', 'Supr'], ['ADJF', 'COMP'], ['ADJF', 'Supr']],
    'B1': [['NOUN'], ['ADJF'], ['NUMR'], ['NPRO'], ['VERB', 'Refl', 'pres'], ['VERB', 'pres'], ['VERB', 'past', 'impf'],
           ['VERB', 'past', 'perf'], ['VERB', 'futr', 'impf'], ['VERB', 'futr', 'perf'], ['VERB', 'impr'],
           ['ADJF', 'COMP'], ['ADJF', 'Supr'], ['ADVB', 'COMP'], ['ADVB', 'Supr']],
    'B2': [['NOUN'], ['NOUN', 'Abbr'], ['ADJF'], ['VERB', 'impf', 'pres'], ['VERB', 'impf', 'futr'], ['VERB', 'pres'],
           ['VERB', 'futr'], ['VERB', 'perf'], ['VERB', 'impr'], ['ADJF', 'COMP'], ['ADJF', 'Supr'], ['ADVB', 'COMP'],
           ['ADVB', 'Supr']],
    'C1': [['NOUN'], ['NOUN', 'Abbr'], ['ADJF'], ['ADJF', 'COMP'], ['ADJF', 'Supr']],
    'C2': [['NOUN'], ['ADJF'], ['NPRO']]
}

lemmas_dict = {
    'A2': ['боротися', 'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'],
    'B1': ['себе', 'соб', 'той', 'цей', 'один', 'два', 'три', 'чотири', 'багато', 'кілька', 'декілька', 'більш', 'менш',
           'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'],
    'B2': ['їхній', 'себе', 'соб', 'дати', 'їсти', 'хай', 'нехай', 'нехаяти', 'би', 'б', 'більш', 'менш', 'більше',
           'менше', 'найбільш', 'найменш', 'найбільше', 'найменше', 'якщо', 'хоч', 'якби'],
    'C1': ['себе', 'соб', 'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'],
    'C2': ['cебе', 'соб']
}


# define the level of the grammemes
def check_grammemes_level(df):
    """
    calculate cefr levels for each word in the word table.
    :param df: DataFrame, word table
    :return: DataFrame, word table with cefr_level column
    """
    level_list = []
    for index in df.index:
        temp_level_list = []
        # check grammemes level
        for grammeme in grammemes_dict['A1']:
            if set(grammeme) in df['grammeme'][index]:
                temp_level_list.append(1)
        for grammeme in grammemes_dict['A2']:
            if set(grammeme) in df['grammeme'][index]:
                temp_level_list.append(2)
        for grammeme in grammemes_dict['B1']:
            if set(grammeme) in df['grammeme'][index]:
                temp_level_list.append(3)
        for grammeme in grammemes_dict['B2']:
            if set(grammeme) in df['grammeme'][index]:
                temp_level_list.append(4)
        for grammeme in grammemes_dict['C1']:
            if set(grammeme) in df['grammeme'][index]:
                temp_level_list.append(5)
        for grammeme in grammemes_dict['C2']:
            if set(grammeme) in df['grammeme'][index]:
                temp_level_list.append(6)
        # check lemmas level
        for lemma in lemmas_dict['A2']:
            if df['lemma'][index] == lemma:
                temp_level_list.append(2)
        for lemma in lemmas_dict['B1']:
            if df['lemma'][index] == lemma:
                temp_level_list.append(3)
        for lemma in lemmas_dict['B2']:
            if df['lemma'][index] == lemma:
                temp_level_list.append(4)
        for lemma in lemmas_dict['C1']:
            if df['lemma'][index] == lemma:
                temp_level_list.append(5)
        for lemma in lemmas_dict['C2']:
            if df['lemma'][index] == lemma:
                temp_level_list.append(6)
        # check if no levels were found
        if not temp_level_list:
            temp_level_list.append(0)
        # append token level
        level_list.append(min(temp_level_list))
    return df.assign(cefr_level=level_list)


from statistics import mean, mode


def interpret_cefr_list(level_list):
    """
    create a dictionary of max, average and mode interpretations of level lists
    :param level_list: list of level indices converted to integer values
    :return: dictionary of max, average and mode interpretations
    """
    level_list_no_zeros = list(filter(lambda x: x != 0, level_list))
    if not level_list_no_zeros:
        level_list_no_zeros.append(1)
    interpretation_list = {
        'max': max(level_list),
        'mode': mode(level_list_no_zeros),
        'avg': mean(level_list_no_zeros)
    }
    return interpretation_list
