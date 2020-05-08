'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example:

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

import random

def create_phone_number(n):
    #your code here
    c = ''.join([str(x) for x in n])
    return f'({c[:3]}) {c[3:6]}-{c[6:]}'

'''
CLEVER METHOD
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
'''

for n in range(5):
    print(create_phone_number([ random.randint(0,9) for i in range(0,10)]))
