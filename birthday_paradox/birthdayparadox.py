"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
Tags: short, math, simulation"""

import timeit
import datetime
import random
import sys


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    unique_birthdays = set(birthdays)
    if len(unique_birthdays) == len(birthdays):
        return None  # All birthdays are unique, so return None.
    else:
        return next((birthday for birthday in unique_birthdays if birthdays.count(birthday) > 1), None)


# Display the intro:
print('''The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

for _ in range(3):
    response = input('How many birthdays shall I generate? (Max 100)\n> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
else:
    print('Invalid input. Exiting program.')
    sys.exit(1)
print()

# Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')

num_sims = 100000
start_time = timeit.default_timer()
simMatch = sum(getMatch(getBirthdays(numBDays))
               is not None for _ in range(num_sims))
elapsed_time = timeit.default_timer() - start_time

probability = round(simMatch / num_sims * 100, 2)
print(f'Out of {num_sims} simulations of {numBDays} people, there was a')
print(f'matching birthday in that group {simMatch} times. This means')
print(f'that {numBDays} people have a {probability} % chance of')
print('having a matching birthday in their group.')
print(f'This simulation took {elapsed_time:.2f} seconds.')
