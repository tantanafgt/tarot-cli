import database

def print_welcome():
    print('Welcome to Tarot lookup!\n')

def select_arcana():
    print('1. Lookup in major arcana')
    print('2. Lookup in minor arcana')
    arcana_value = input("Enter your choice: ")

    if arcana_value not in ['1', '2']:
        print('You entered wrong value, input again')
        return select_arcana()

    return arcana_value

major_names = database.major_arcana_names()
major_count = len(major_names)

def select_major_arcana():
    print('Enter the number of major arcana')
    for x in range(major_count):
        print('%d. %s' % (x, major_names[x]))
    major_arcana_value = input("Enter your choice: ")

    if major_arcana_value not in ['%d' % x for x in range(major_count)]:
        print('You entered wrong value, input again')
        return select_major_arcana()

    return major_arcana_value

def select_orientation():
    print('Enter the orientation of the card')
    print('1. Upright')
    print('2. Inverted / reversed')
    orientation_value = input('Enter the orientation: ')

    if orientation_value not in ['1', '2']:
        print('You entered wrong value, input again')
        return select_orientation()

    return orientation_value


def select_suit():
    print('Enter the suit of the card')
    print('1. Wands')
    print('2. Cups')
    print('3. Swords')
    print('4. Pentacles')
    suit_value = input('Enter the suit: ')

    if suit_value not in ['1', '2','3','4']:
        print('You entered wrong value, input again')
        return select_suit()

    return suit_value

def select_pip(suit):
    print('Enter the number of minor arcana')
    # print('! 11 for Page, 12 for Knight, 13 for Queen, 14 for King')
    names = database.minor_arcana_names(suit)
    minor_count = len(names)

    for x in range(minor_count):
        print('%d. %s' % (x + 1, names[x]))
    minor_arcana_value = input("Enter your choice: ")

    if minor_arcana_value not in ['%d' % (x + 1) for x in range(minor_count)]:
        print('You entered wrong value, input again')
        return select_pip()

    return minor_arcana_value
