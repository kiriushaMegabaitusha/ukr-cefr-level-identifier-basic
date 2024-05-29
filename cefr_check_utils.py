# dictionary of grammemes

'''
A1	['NOUN', 'sing'],
	['NOUN', 'plur', 'nomn'],
	['NOUN', 'accs', 'sing'], ['NOUN', 'loct', 'sing'],





	['NOUN', 'voct'],
	['ADJF', 'sing'], ['ADJF', 'plur'],
	['ADJF', 'nomn'], ['ADJF', 'accs'], ['ADJF', 'loct']
	['NPRO', 'pers'], ['NPRO']

	['VERB', 'plur']
	['VERB', 'perf', 'futr']
	['VERB', 'impr']
A2	 ['NOUN']
	['ADJF', 'sing'], ['ADJF, 'plur']
	['NPRO', 'pers']
	['NPRO']
	['VERB', 'pres']
	боротися' ['VERB', 'pres']
	['VERB', 'past']
	['VERB', 'futr']
	['ADJF', 'COMP']
	['ADJF', 'Supr']
	більш', 'менш', 'більше', 'менше'
	найбільш', 'найменш', 'найбільше', 'найменше'
	['ADJF', 'COMP'], [ADJF, 'Supr']
B1	['NOUN']
	['ADJF']
	один', 'два', 'три', 'чотири', ['NUMR']
	багато', 'кілька', 'декілька'
	['NPRO']
	себе', 'соб'
	той', 'цей'
	['VERB', 'Refl', 'pres']
	дати', 'їсти' ['VERB', 'pres']
	['VERB', 'past', 'impf'], ['VERB', 'past', 'perf']
	['VERB', 'futr', 'impf']
	['VERB', 'futr', 'perf']
	['VERB' 'impr'] 'хай', 'нехай', 'нехаяти'
	би', 'б'
	['ADJF' 'COMP']
	['ADJF' 'Supr']
	більш', 'менш', 'більше', 'менше'
	найбільш', 'найменш', 'найбільше', 'найменше'
	['ADVB' 'COMP']
	['ADVB' 'Supr']
	більш', 'менш', 'більше', 'менше'
	найбільш', 'найменш', 'найбільше', 'найменше'
B2	['NOUN']
	['NOUN' 'Abbr']
	['ADJF']
	їхній'
	себе', 'соб'
	['VERB' 'impf', 'pres']
	['VERB' 'impf', 'futr']
	дати', 'їсти', ['VERB', 'pres'], ['VERB', 'futr']
	['VERB' 'perf']
	['VERB' 'impr'] 'хай', 'нехай', 'нехаяти'
	би', 'б'
	['ADJF' 'COMP']
	['ADJF' 'Supr']
	більш', 'менш', 'більше', 'менше'
	найбільш', 'найменш', 'найбільше', 'найменше'
	['ADVB' 'COMP']
	['ADVB' 'Supr']
	'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше', 'якщо', 'хоч', 'якби'
C1	['NOUN']
	['NOUN' 'Abbr']
	['ADJF']
	себе', 'соб'
	['ADJF' 'COMP'] ['ADJF' 'Supr']
	більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'
C2	['NOUN']
	['ADJF']
	['NPRO']
	cебе', 'соб'
'''

grammemes_dict = {
    'A1': [['NOUN', 'sing'], ['NOUN', 'plur', 'nomn'], ['NOUN', 'accs', 'sing'], ['NOUN', 'loct', 'sing'], ['NOUN', 'voct'], ['ADJF', 'sing'], ['ADJF', 'plur'], ['ADJF', 'nomn'], ['ADJF', 'accs'], ['ADJF', 'loct'], ['NPRO', 'pers'], ['NPRO'], ['VERB', 'plur'], ['VERB', 'perf', 'futr'], ['VERB', 'impr']],
    'A2': [['NOUN'], ['ADJF', 'sing'], ['ADJF', 'plur'], ['NPRO', 'pers'], ['NPRO'], ['VERB', 'pres'], ['VERB', 'pres'], ['VERB', 'past'], ['VERB', 'futr'], ['ADJF', 'COMP'], ['ADJF', 'Supr'], ['ADJF', 'COMP'], ['ADJF', 'Supr']],
    'B1': [['NOUN'], ['ADJF'], ['NUMR'], ['NPRO'], ['VERB', 'Refl', 'pres'], ['VERB', 'pres'], ['VERB', 'past', 'impf'], ['VERB', 'past', 'perf'], ['VERB', 'futr', 'impf'], ['VERB', 'futr', 'perf'], ['VERB' 'impr'], ['ADJF' 'COMP'], ['ADJF' 'Supr'], ['ADVB' 'COMP'], ['ADVB' 'Supr']],
    'B2': [['NOUN'], ['NOUN' 'Abbr'], ['ADJF'], ['VERB' 'impf', 'pres'], ['VERB' 'impf', 'futr'], ['VERB', 'pres'], ['VERB', 'futr'], ['VERB' 'perf'], ['VERB' 'impr'], ['ADJF' 'COMP'], ['ADJF' 'Supr'], ['ADVB' 'COMP'], ['ADVB' 'Supr']],
    'C1': [['NOUN'], ['NOUN' 'Abbr'], ['ADJF'], ['ADJF' 'COMP'], ['ADJF' 'Supr']],
    'C2': [['NOUN'], ['ADJF'], ['NPRO']]
}

lemmas_dict = {
    'A2': ['боротися', 'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'],
    'B1': ['себе', 'соб', 'той', 'цей', 'один', 'два', 'три', 'чотири',	'багато', 'кілька', 'декілька', 'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'],
    'B2': ['їхній', 'себе', 'соб', 'дати', 'їсти', 'хай', 'нехай', 'нехаяти', 'би', 'б', 'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше', 'якщо', 'хоч', 'якби'],
    'C1': ['себе', 'соб', 'більш', 'менш', 'більше', 'менше', 'найбільш', 'найменш', 'найбільше', 'найменше'],
    'C2': ['cебе', 'соб']
}

#define the level of the grammemes
de[check_grammemes_level(grammemes):
    '''
    Get highest available CEFR level based on grammar indices
    :param grammemes: string containing morhpological categories in pymorphy2 format
    :return: integer, the highest available CEFR level based on grammar indices
    '''
    if grammemes in grammemes_dict['C2']:
        return 1
    elif grammemes in grammemes_dict['C1']:
        return 2
    elif grammemes in grammemes_dict['B2']:
        return 3
    elif grammemes in grammemes_dict['B1']:
        return 4
    elif grammemes in grammemes_dict['A2']:
        return 5
    elif grammemes in grammemes_dict['A1']:
        return 6
    else:
        return 0

def interpret_cefr_list(level_list):
    '''
    create a dictionary of max, average and mode interpretations of level lists
    :param level_list: list of level indices converted to integer values
    :return: dictionary of max, average and mode interpretations
    '''
    interpretation_list = {
        'max': str(),
        'mode': str(),
        'avg': str()
    }
    interpretation_list['max'] = max(level_list)
    interpretation_list['mode'] = max(level_list, key=level_list.count)
    interpretation_list['avg'] = round(sum(level_list) / len(level_list))
    return interpretation_list