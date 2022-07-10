import menu
import database

Major = '1'
Minor = '2'

def suit_from_selection(menu_selection):
    mapping = {
        '1': 'wands',
        '2': 'cups',
        '3': 'swords',
        '4': 'pentacles',
    }
    return mapping[menu_selection]


def print_card_info(card, orientation):
    print(card['name'])

    print('\nCard description:')
    print(card['desc'])

    if orientation == '1':
        print('\nUpright meaning:')
        print(card['meaning_up'])
    else:
        print('\nReversed meaning:')
        print(card['meaning_rev'])


if __name__ == '__main__':
    menu.print_welcome()
    arcana = menu.select_arcana()

    if arcana == Major: # major
        major = menu.select_major_arcana()
        orientation = menu.select_orientation()
        card = database.get_card_info_major(major)
        print_card_info(card, orientation)

    elif arcana == Minor: # minor
        suit = suit_from_selection(menu.select_suit())
        pip = menu.select_pip(suit)
        orientation = menu.select_orientation()
        card = database.get_card_info_minor(suit, pip)
        print_card_info(card, orientation)

    # print_thanks()
