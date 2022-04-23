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
answer = calculation_function(num1, num2)

print(f'{num1} {operator} {num2} = {answer}')
