from art import logo

print(logo)

# calculator

# ADD


def add(n1, n2):
    return n1 + n2

# SUBTRACT


def subtract(n1, n2):
    return n1 - n2

# MULTIPLY


def multiply(n1, n2):
    return n1 * n2

# DIVIDE


def divide(n1, n2):
    return n1 / n2


symbols = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide',
}
num1 = int(input('What is the first number? '))
for symbol in symbols:
    print(symbol)
operator = input('Pick an operation symbol from above: ')
num2 = int(input('What is the second number? '))
calculation_function = symbols[operator]
first_answer = calculation_function(num1, num2)

print(f'{num1} {operator} {num2} = {first_answer}')

# Here we select "*" which overides the "+" we selected previously.
operator = input('Pick an operation symbol from above: ')
num3 = int(input('What is the next number? '))

# Here the calculation_function selected will be the multiply() function
calculation_function = symbols[operator]

# Here the code will be:
# second_answer = multiply(multiply(num1, num2), num3)
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
