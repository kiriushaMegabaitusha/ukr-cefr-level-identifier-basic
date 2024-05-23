
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
        return 'C2'
    elif grammemes in grammemes_dict['C1']:
        return 'C1'
    elif grammemes in grammemes_dict['B2']:
        return 'B2'
    elif grammemes in grammemes_dict['B1']:
        return 'B1'
    elif grammemes in grammemes_dict['A2']:
        return 'A2'
    elif grammemes in grammemes_dict['A1']:
        return 'A1'

