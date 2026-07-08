#from math_utils import add, subtract, multiply, divide, factorial, PI, Calculator
import math_utils

#result1 = add(5, 3)
result1 = math_utils.add(5, 3)
print(f"Addition: 5 + 3 = {result1}")

#result2 = subtract(10, 4)
result2 = math_utils.subtract(10, 4)
print(f"Subtraction: 10 - 4 = {result2}")

#result3 = multiply(6, 7)
result3 = math_utils.multiply(6, 7)
print(f"Multiplication: 6 * 7 = {result3}")

#result4 = divide(20, 5)
result4 = math_utils.divide(20, 5)
print(f"Division: 20 / 5 = {result4}")

#result5 = factorial(5)
result5 = math_utils.factorial(5)
print(f"Factorial: 5! = {result5}")

#print(f"Value of PI: {PI}")
print(f"Value of PI: {math_utils.PI}")

###############################################################################
#libraries
# import os
# import sys
# import datetime
# import random

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # now = datetime.datetime.now()
# # today = datetime.date.today()
# # formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# now = datetime.datetime.now()
# today = datetime.date.today()
# formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")

# print(f"Now Date: {now}")
# print(f"Today's Date: {today}")
# print(f"Formatted Date: {formatted_date}")

# random_number = random.randint(1, 100)
# random_choice = random.choice(['apple', 'banana', 'cherry'])
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)

# print(f"Random Number: {random_number}")
# print(f"Random Choice: {random_choice}")
# print(f"Shuffled Numbers: {numbers}")
