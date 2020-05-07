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
