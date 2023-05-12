"""Displays a text message according to the provided bitmap image.
Tags: tiny, beginner, artistic"""

import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
BITMAP = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


def main():
    message = input('Enter the message to display with the bitmap.\n> ')
    if message == '':
        sys.exit()

    for line in BITMAP.splitlines():
        print(''.join(message[i % len(message)] if bit !=
              ' ' else ' ' for i, bit in enumerate(line)))


if __name__ == '__main__':
    main()
