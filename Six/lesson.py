print('Hello')
num_char = len('Hello')
print(num_char)

def my_function(): # creating / defining function
    print('Hello')
    print('Good Bye')

my_function() # call the function

# Reeborg's World (reeborg.ca)
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

# or using a while loop instead of for loop
hurdles = 6
while hurdles > 0:
    jump()
    hurdles -= 1
# if we used at_goal() which is set to true...
while not at_goal():
    jump()

# Reeborg's World Hurdles 3
while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()

# Reeborg's World Hurdle 4
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()
# Reeborg's World Maze ---- Infinite Loop issue in some cases
# Come back after Day 15 and debug all possibilities
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()