def dirReduc(arr):
    oposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST" : "WEST",
        "WEST" : "EAST"}
    res = []
    for i in arr:
        if res and oposites[i] == res[-1]: # check if res is not empty an if oposites of i is equal the last element of res
            res.pop() # delete the last element of res
        else:
            res.append(i)
    return print(res)

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "WEST"]
b = ['NORTH']
c = ['NORTH', 'EAST', 'WEST']
d = ['NORTH', 'WEST', 'SOUTH', 'EAST']
e = ['NORTH', 'SOUTH']
f = ['NORTH', 'NORTH']
g = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
h = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST", "NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST", "NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
for i in [a,b,c,d,e,f,g,h]:
    dirReduc(i)