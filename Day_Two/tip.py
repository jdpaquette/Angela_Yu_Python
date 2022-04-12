print('Welcome to the Tip Calculator')
total = float(input('What is the total bill amount? $'))
guests = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip to give: 10, 15, 18, 20? '))
each = ((total + (total*(tip/100))) / guests)
print('Each person should pay $' + str(round(each, 2)))

# Angela's Code
# this format code specifies how many decimals even if Zeros
# print(f"Each person should pay $" + str("{:.2f}.format(each)