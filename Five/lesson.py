
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

