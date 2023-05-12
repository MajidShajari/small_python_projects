<h1> Bagels</h1>

Bagels is a deductive logic game where the player must guess a secret number based on clues provided by the game. The game is written in Python and is a console-based application.

## Requirements

-   Python 3.x

## Usage

-   Clone or download the repository.
-   Navigate to the project directory.
-   Run `python bagels.py` script in your terminal.
-   When the game starts, the player is prompted to guess a three-digit number with no repeated digits.
-   The player has a maximum of ten guesses to guess the secret number.
-   After each guess, the game provides clues in the form of "Fermi," "Pico," or "Bagels" to help the player narrow down the possible numbers.

    **_"Fermi" means that one digit is correct and in the right position._**

    **_"Pico" means that one digit is correct but in the wrong position._**

    **_"Bagels" means that no digit is correct._**

    _For example, if the secret number is 123 and the player guesses 456, the clues would be "Bagels." If the player guesses 124, the clues would be "Fermi Pico."_

-   If the player correctly guesses the secret number, the game ends and the player wins.
-   If the player runs out of guesses without guessing the secret number, the game ends and the player loses.

## Customization

The game can be customized by changing the following constants in the code:

-   NUM_DIGITS: the number of digits in the secret number (default is 3)
-   MAX_GUESSES: the maximum number of guesses allowed (default is 10)

## Contributing

Contributions are welcome. Please feel free to open an issue or submit a pull request.
