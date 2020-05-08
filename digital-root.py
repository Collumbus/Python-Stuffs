'''
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
'''

def digital_root(n):
    while n > 9:
        n = sum([int(d) for d in str(n)])
        print(n)
    return n

'''
CLEVER METHOD
def digital_root(n):
    return n%9 or n and 9 
'''

digital_root(325256015251651651652511261561798418521521521)
