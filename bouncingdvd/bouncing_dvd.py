import sys
import random
import time
from bext import goto, clear, fg, size

# Set up the constants:
WIDTH, HEIGHT = 30, 30
if WIDTH > size()[0]:
    WIDTH = size()[0]
if HEIGHT > size()[1]:
    HEIGHT = size()[1]
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT = DIRECTIONS = (
    'ur', 'ul', 'dr', 'dl')

# Key names for logo dictionaries:
COLOR, X, Y, DIR = 'color', 'x', 'y', 'direction'


def main():
    clear()

    # Generate some logos.
    logos = []
    for _ in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      # Make sure X is even so it can hit the corner.
                      X: random.randint(2, WIDTH - 3) // 2 * 2,
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})

    corner_bounces = 0
    while True:
        for logo in logos:
            goto(logo[X], logo[Y])
            print('   ', end='')

            original_direction = logo[DIR]
            # See if the logo bounces off the corners:
            if (logo[X], logo[Y]) == (0, 0):
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif (logo[X], logo[Y]) == (0, HEIGHT - 1):
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif (logo[X], logo[Y]) == (WIDTH - 3, 0):
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif (logo[X], logo[Y]) == (WIDTH - 3, HEIGHT - 1):
                logo[DIR] = UP_LEFT
                corner_bounces += 1

            elif logo[X] == 0 and logo[DIR] in (UP_LEFT, DOWN_LEFT):
                logo[DIR] = opposite_direction_x(logo[DIR])
            elif logo[X] >= WIDTH - 3 and logo[DIR] in (UP_RIGHT, DOWN_RIGHT):
                logo[DIR] = opposite_direction_x(logo[DIR])
            elif logo[Y] == 0 and logo[DIR] in (UP_LEFT, UP_RIGHT):
                logo[DIR] = opposite_direction_y(logo[DIR])
            elif logo[Y] == HEIGHT - 1 and logo[DIR] in (DOWN_LEFT, DOWN_RIGHT):
                logo[DIR] = opposite_direction_y(logo[DIR])

            if logo[DIR] != original_direction:
                logo[COLOR] = random.choice(COLORS)

            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        goto(5, 0)
        fg('white')
        print('Corner bounces:', corner_bounces, end='')

        for logo in logos:
            goto(logo[X], logo[Y])
            fg(logo[COLOR])
            print('DVD', end='')

        goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


def opposite_direction_x(direction):
    if direction == UP_RIGHT:
        return UP_LEFT
    elif direction == UP_LEFT:
        return UP_RIGHT
    elif direction == DOWN_RIGHT:
        return DOWN_LEFT
    elif direction == DOWN_LEFT:
        return DOWN_RIGHT


def opposite_direction_y(direction):
    if direction == UP_RIGHT:
        return DOWN_RIGHT
    elif direction == UP_LEFT:
        return DOWN_LEFT
    elif direction == DOWN_RIGHT:
        return UP_RIGHT
    elif direction == DOWN_LEFT:
        return UP_LEFT


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo')
        sys.exit()
