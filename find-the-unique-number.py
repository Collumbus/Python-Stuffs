def find_uniq(arr):
    uniques = set(arr)
    return  [n for n in uniques if arr.count(n) == 1][0]


'''
###ANOTHER WAY###
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
'''
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
