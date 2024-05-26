
grammemes_dict = {
    'A1': {},
    'A2': {},
    'B1': {},
    'B2': {},
    'C1': {},
    'C2': {}
}
def check_grammemes_level(grammemes):
    '''
    Get highest available CEFR level based on grammar indices
    :param grammemes: string containing morhpological categories in pymorphy2 format
    :return: string signifying highest available CEFR level
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

def interpret_cefr_list(level_list):
    interpretation_list = {
        'max': str(),
        'mode': str(),
        'avg': str()
    }
    interpretation_list['max'] = max(level_list)
    interpretation_list['mode'] = max(level_list, key=level_list.count)
    interpretation_list['avg'] = round(sum(level_list) / len(level_list))
    return interpretation_list