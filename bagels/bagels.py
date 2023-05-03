"""
A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.


def main():
    print('''Bagels, a deductive logic game.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask player if they want to play again.
        if input('Do you want to play again? (yes or no)\n> ').lower() != 'yes':
            break
    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = random.sample(
        range(10), NUM_DIGITS)  # Select NUM_DIGITS unique digits from 0 to 9.
    return ''.join(map(str, numbers))


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')

    return 'Bagels' if not clues else ' '.join(sorted(clues))


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
