# Functions with Outputs April 21, 2022 - Joseph D. Paquette

def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't provide valid names!"
    new_fname = f_name.title()
    new_lname = l_name.title()
    return f'Result: {new_fname} {new_lname}'


print(format_name(input('What is your first name? '),
      input('What is your last name? ')))
