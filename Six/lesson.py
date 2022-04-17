print('Hello')
num_char = len('Hello')
print(num_char)

def my_function(): # creating / defining function
    print('Hello')
    print('Good Bye')

my_function() # call the function

# Reeborg's World
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()