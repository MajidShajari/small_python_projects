"""Caesar Cipher Hacker
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
Tags: tiny, beginner, cryptography, math"""


print('Caesar Cipher Hacker')


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    message = input('Enter the encrypted Caesar cipher message to hack: ')

    for key in range(len(SYMBOLS)):
        translated = ''

        for symbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                # Use modulo operator for wrap-around
                num = (num - key) % len(SYMBOLS)

                translated += SYMBOLS[num]
            else:
                translated += symbol

        print(f"Key #{key}: {translated}")


if __name__ == '__main__':
    main()
