import random

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# random_integer = random.randint(0, 5)
# print(random_integer)
#
# random_float = random.random()
# print(random_float)
#
# # total_random = random_integer + random_float
# # print(total_random)
#
# new_random_float = random.random() * 5
# print(random_float)
#
# coin = random.randint(0, 1)
# print(coin)
# if coin == 0:
#     print("Heads")
# else:
#     print("Tails")
