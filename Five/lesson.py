
# Day Five Lessons

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + ' ' + 'Pie')

# Exercise One  -- can't use sum() or len()
# Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above 👆


#Write your code below this row 👇
total = 0
for height in student_heights:
    total += height

number = 0
for students in student_heights:
    number += 1

print(round(total/number))


# Exercise Two  -  can't use min() or max()
#  Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
#  Don't change the code above 👆

#Write your code below this row 👇
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f'The highest score in the class is: {high_score}')

# Loops using range
for number in range(1, 11): # need to go up one i.e. to 11 to get 1 through 10
    print(number)

total = 0
for number in range(2, 101, 2): # add all even number between 1 and 100 (must start at two)
    total += number
print(total)

# optional
total2 = 0
for number in range(1, 101, 2): # using modulo
    if number % 2 == 0:
        total2 += number
print(total2)

# FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
