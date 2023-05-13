"""Carrot in a Box
A silly bluffing game between two human players. Based on the game
from the show, 8 Out of 10 Cats.
Tags: large, beginner, game, two-player"""

import random

print('''Carrot in a Box,

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this.) The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')


def get_player_names():
    p1_name = input('Human player 1, enter your name: ')
    p2_name = input('Human player 2, enter your name: ')
    return p1_name, p2_name


def display_boxes(message, first_box='RED ', second_box='GOLD'):
    print(f'''{message}:
    __________     __________
    /         /|   /         /|
    +---------+ |  +---------+ |
    |   {first_box}  | |  |   {second_box}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/''')


def display_carrot(player_names, carrot_in_first_box):
    if carrot_in_first_box:
        print('''
    ___VV____
    |   VV    |
    |   VV    |
    |___||____|    __________
    /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
    (carrot!)''')
        print(player_names)
    else:
        print('''
    _________
    |         |
    |         |
    |_________|    __________
    /         /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
    (no carrot!)''')
        print(player_names)


def get_swap_decision(p1_name, p2_name):
    while True:
        response = input(
            f'{p2_name}, do you want to swap boxes with {p1_name}? YES/NO\n').upper()
        if response.startswith('Y') or response.startswith('N'):
            return response
        print(f'{p2_name}, please enter "YES" or "NO".')


def reveal_winner(carrot_in_first_box, first_box, second_box):
    if carrot_in_first_box:
        print(f'''
    ___VV____      _________
    |   VV    |    |         |
    |   VV    |    |         |
    |___||____|    |_________|
    /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   {first_box}  | |  |   {second_box}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/''')

    else:
        print(f'''
    _________      ___VV____
    |         |    |   VV    |
    |         |    |   VV    |
    |_________|    |___||____|
    /         /|   /    ||   /|
    +---------+ |  +---------+ |
    |   {first_box}  | |  |   {second_box}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/''')


def main():
    input('Press Enter to begin...')
    p1_name, p2_name = get_player_names()
    player_names = f'{p1_name[:11].center(11)}    {p2_name[:11].center(11)}'
    display_boxes("HERE ARE TWO BOXES:")
    print(f'\n{player_names}\n')
    print(f'{p1_name}, you have a RED box in front of you.')
    print(f'{p2_name}, you have a GOLD box in front of you.\n')
    print(f'{p1_name}, you will get to look into your box.')
    print(f'{p2_name.upper()}, close your eyes and don\'t look!!!')
    input(f'When {p2_name} has closed their eyes, press Enter...\n')

    print(f'{p1_name} here is the inside of your box:')

    carrot_in_first_box = random.choice([True, False])
    display_carrot(player_names, carrot_in_first_box)

    input('Press Enter to continue...\n')

    print('\n' * 100)  # Clear the screen by printing several newlines.
    print(f'{p1_name}, tell {p2_name} to open their eyes.')
    input('Press Enter to continue...\n')

    print(f'\n{p1_name}, say one of the following sentences to {p2_name}.')
    print('  1) There is a carrot in my box.')
    print('  2) There is not a carrot in my box.')
    input('Then press Enter to continue...\n')
    response = get_swap_decision(p1_name, p2_name)
    first_box = 'RED '  # Note the space after the "D".
    second_box = 'GOLD'

    if response.startswith('Y'):
        carrot_in_first_box = not carrot_in_first_box
        first_box, second_box = second_box, first_box

    display_boxes("HERE ARE THE TWO BOXES:", first_box, second_box)

    input('Press Enter to reveal the winner...')
    reveal_winner(carrot_in_first_box, first_box, second_box)
    print(player_names)

    # This modification made possible through the 'carrotInFirstBox variable
    if carrot_in_first_box:
        print(p1_name + ' is the winner!')
    else:
        print(p2_name + ' is the winner!')

    print('Thanks for playing!')


if __name__ == '__main__':
    main()
