
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
    Calculate CEFR level based on grammar index
    :param grammemes: string containing morhpological categories in pymorphy2 format
    :return: CEFR level based on the grammeme dictionary
    '''
    if grammemes not in grammemes_dict:
        return None
    elif grammemes in grammemes_dict['A1']:
