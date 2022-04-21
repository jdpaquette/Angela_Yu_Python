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
num2 = int(input('What is the second number? '))
for keys, values in symbols.items():
    print(f'{keys} {values}')
operator = input('Pick an operation symbol from above: ')


print(f'{num1} {operator} {num2} = {answer}')
