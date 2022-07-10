import json

data_filename = 'card_data.json'
database = json.load(open(data_filename))

def major_arcana():
    return list(filter(lambda it: it['type'] == 'major', database['cards']))

def major_arcana_names():
    major = major_arcana()
    major.sort(key = lambda it: it['value_int'])
    return list(map(lambda it: it['name'], major))

def get_card_info_major(major_num):
    major = major_arcana()

    def filter_by_num(card):
        return card['value'] == major_num

    found = list(filter(filter_by_num, major))
    if len(found) == 1:
        return found[0]
    else:
        return None


def minor_arcana_by_suit(suit):
    return list(filter(
        lambda it: it['type'] == 'minor' and it['suit'] == suit,
        database['cards']
    ))


def minor_arcana_names(suit):
    minor = minor_arcana_by_suit(suit)
    minor.sort(key = lambda it: it['value_int'])
    return list(map(lambda it: it['name'], minor))

def get_card_info_minor(suit, minor_num):
    minor = minor_arcana_by_suit(suit)

    def filter_by_num(card):
        return str(card['value_int']) == minor_num

    found = list(filter(filter_by_num, minor))
    if len(found) == 1:
        return found[0]
    else:
        return None
