import random

random_integer = random.randint(0, 5)
print(random_integer)

random_float = random.random()
print(random_float)

# total_random = random_integer + random_float
# print(total_random)

new_random_float = random.random() * 5
print(random_float)

coin = random.randint(0, 1)
print(coin)
if coin == 0:
    print("Heads")
else:
    print("Tails")
