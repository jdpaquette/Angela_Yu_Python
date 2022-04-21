# Functions with Outputs April 21, 2022 - Joseph D. Paquette

def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't provide valid names!"
    new_fname = f_name.title()
    new_lname = l_name.title()
    return f'Result: {new_fname} {new_lname}'


print(format_name(input('What is your first name? '),
      input('What is your last name? ')))

# Coding Rooms Day 10 -- Leap Year


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Please enter a number between 1 and 12"
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year) and month == 2:
            return 29
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Doctrings
length = len(formatted_name)

# Return as an early exit


def format_name(f_name. l_name):
    """Take a first name and last name and format it
    to return the turle case version of the name. """
    if f_name == '' or l_name == '':
        return 'Please provide valid inputs'
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Result: {formated_f_name} {formated_l_name}'
