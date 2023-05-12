"""Caesar Cipher
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
Tags: short, beginner, cryptography, math"""
import sys


def main():
    print("Caesar Cipher")
    print("The Caesar cipher encrypts letters by shifting them over by a")
    print("key number. For example, a key of 2 means the letter A is")
    print("encrypted into C, the letter B encrypted into D, and so on.")
    print()
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    _mode = input('> ').lower()

    while _mode not in ['e', 'd']:
        print('Please enter the letter e or d.')
        _mode = input('> ').lower()
    if _mode.startswith('e'):
        _mode = "encrypt"
    else:
        _mode = "decrypt"

    while True:  # Keep asking until the user enters a valid key.
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input('> ').upper()
        if not response.isdecimal():
            continue

        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

    print(f"Enter the message to {_mode}.")
    message = input('> ').upper()

    _translate = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if _mode == 'encrypt':
                num = (num + key) % len(SYMBOLS)
            elif _mode == 'decrypt':
                num = (num - key) % len(SYMBOLS)
            _translate += SYMBOLS[num]
        else:
            _translate += symbol

    print(f"The Translate message : {_translate}")
    return _translate, _mode


try:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translate, mode = main()
    import pyperclip
    pyperclip.copy(translate)
    print(f"Full {mode}ed text copied to clipboard.")
except ImportError:
    print('This program requires the pyperclip module, for copy translate message to clipboard.')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()
