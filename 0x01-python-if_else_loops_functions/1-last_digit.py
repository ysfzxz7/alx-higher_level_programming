#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last = 0
if number > 0:
    last = number % 10
if number < 0:
    last = number % -10

string = ""
if last > 5:
    string = "and is not greater than 5"
elif last == 0:
    string == "and is 0"
else:
    string = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {last:d} {string}")
