# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print('Your final bill is: $18.')
        else:
            print('Your final bill is: $17.')
    else:
        if extra_cheese == 'Y':
            print('Your final bill is: $16.')
        else:
            print('Your final bill is: $15.')
elif size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print('Your final bill is: $24.')
        else:
            print('Your final bill is: $23.')
    else:
        if extra_cheese == 'Y':
            print('Your final bill is: $21.')
        else:
            print('Your final bill is: $20.')
else:
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print('Your final bill is: $29.')
        else:
            print('Your final bill is: $28.')
    else:
        if extra_cheese == 'Y':
            print('Your final bill is: $26.')
        else:
            print('Your final bill is: $25.')

# Angela worked it out like this
# bill = 0;
#
# if size == 'S':
#     bill += 15
#     if add_pepperoni == 'Y':
#         bill += 2
# elif size == 'M':
#     bill += 20
#     if add_pepperoni == 'Y':
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == 'Y':
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1
#
# print(f'Your final bill is: ${bill}')