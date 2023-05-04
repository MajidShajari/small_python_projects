"""
A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.


def main():
    print(f'''Bagels, a deductive logic game.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(' You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct, so break out of this loop.
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}.')

        # Ask player if they want to play again.
        if input('Do you want to play again? (yes or no)\n> ').lower() != 'yes':
            break
    print('Thanks for playing!')


def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = random.sample(
        range(10), NUM_DIGITS)  # Select NUM_DIGITS unique digits from 0 to 9.
    return ''.join(map(str, numbers))


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i, g_num in enumerate(guess):
        if g_num == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif g_num in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')

    return 'Bagels' if not clues else ' '.join(sorted(clues))


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
