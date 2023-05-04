"""git Explore the surprising probabilities of the "Birthday Paradox".
Tags: short, math, simulation"""

import timeit
import datetime
import random
import sys


def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""
    _birthdays = []
    for _ in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        _birthday = start_of_year + random_number_of_days
        _birthdays.append(_birthday)
    return _birthdays


def get_match(_birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    unique_birthdays = set(_birthdays)
    if len(unique_birthdays) == len(_birthdays):
        return None  # All birthdays are unique, so return None.
    return next((_birthday for _birthday in unique_birthdays if _birthdays.count(_birthday) > 1), None)


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
        number_birth_day = int(response)
        break
else:
    print('Invalid input. Exiting program.')
    sys.exit(1)
print()

# Generate and display the birthdays:
print('Here are', number_birth_day, 'birthdays:')
birthdays = get_birthdays(number_birth_day)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', number_birth_day, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')

NUM_SIMS = 100000
start_time = timeit.default_timer()
simMatch = sum(get_match(get_birthdays(number_birth_day))
               is not None for _ in range(NUM_SIMS))
elapsed_time = timeit.default_timer() - start_time

probability = round(simMatch / NUM_SIMS * 100, 2)
print(f'Out of {NUM_SIMS} simulations of {number_birth_day} people, there was a')
print(f'matching birthday in that group {simMatch} times. This means')
print(f'that {number_birth_day} people have a {probability} % chance of')
print('having a matching birthday in their group.')
print(f'This simulation took {elapsed_time:.2f} seconds.')
