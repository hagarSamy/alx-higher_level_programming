#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1 if number >= 0 else -1
last_digit = sign * int(str(number)[-1])
if last_digit == 0:
    suffix = " and is 0"
elif last_digit > 5:
    suffix = " and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    suffix = " and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit}{suffix}")
