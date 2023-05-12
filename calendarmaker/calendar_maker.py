"""Calendar Maker
Create monthly calendars, saved to a text file and fit for printing.
Tags: short"""

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')


def main():
    # Loop to get a valid year from the user
    while True:
        response = input('Enter the year for the calendar: ')
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        print('Please enter a numeric year, like 2023.')

    # Loop to get a valid month from the user
    while True:
        response = input('Enter the month for the calendar, 1-12: ')
        if response.isdecimal():
            month = int(response)
            if 1 <= month <= 12:
                break
        print('Please enter a number from 1 to 12.')

    calendar_text = get_calendar_for(year, month)
    print(calendar_text)  # Display the calendar.

    # Save the calendar to a text file:
    calendar_file_name = f"calendar_{year}_{month}.txt"
    with open(calendar_file_name, 'w', encoding="utf-8") as file_obj:
        file_obj.write(calendar_text)

    print('Saved to ' + calendar_file_name)


def get_calendar_for(year, month):
    calendar_text = ''  # calText will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calendar_text += f"{' ' * 34}{MONTHS[month - 1]} {year}\n"

    # Add the days of the week labels to the calendar:
    # Using abbreviations: SUN, MON, TUE, etc.
    day_labels = ' '.join(day[:3].center(10) for day in DAYS)
    calendar_text += f"...{day_labels}..\n"

    # The horizontal line string that separates weeks:
    week_separator = '+----------' * 7 + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blank_row = ('|          ' * 7) + '|\n'

    # Get the first date in the month.
    current_date = datetime.date(year, month, 1)

    # Roll back current_date until it is Sunday.
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        calendar_text += week_separator

        # Generate the row with day number labels
        day_number_row = ''
        for _ in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)  # Go to next day.
        calendar_text += f"{day_number_row}|\n"

        # Add the blank rows
        for _ in range(3):
            calendar_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calendar_text += week_separator

    return calendar_text


# Run the main function
if __name__ == "__main__":
    main()
