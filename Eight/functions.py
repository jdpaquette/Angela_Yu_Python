def greet():
    print('Hello World!')
    print('I am the best coder in the world!')
    print("maybe not...")

greet()

# function that allows for input
def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How are you today {name}')
    print("maybe not...")
# parameter is the name of the data being passed over
# argument is the actual value of the data being passed over
greet_with_name('Angela')

day = input('What is your name? ')
time = input('What is your location? ')

# functions with more than one input
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

greet_with(day, time)
