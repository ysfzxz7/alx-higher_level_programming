#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last = str(number)
print(f"Last digit of {number} is {last[-1]}",end=" ")
if number > 0 and int(last[-1]) > 5:
    print("and is greater than 5")
elif number > 0 and int(last[-1]) == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

