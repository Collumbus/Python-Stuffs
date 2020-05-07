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
