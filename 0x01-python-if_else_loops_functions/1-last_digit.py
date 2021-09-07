#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
digit = number % 10
if exe == 1:
    number *= -1
if digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, digit))
elif digit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, digit))
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, digit))
