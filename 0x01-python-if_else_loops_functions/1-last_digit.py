#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num_digit = abs(number) % 10
if number < 0:
    last_num_digit = -last_num_digit
print(f"Last digit of {number} is {last_num_digit} ", end="")
if last_num_digit > 5:
    print("and is greayer than 5")
elif last_num_digit == 0:
    print("and is 0")
elif last_num_digit < 6 && last_num_digit != 0:
    print("and is less than 6 and not 0")
