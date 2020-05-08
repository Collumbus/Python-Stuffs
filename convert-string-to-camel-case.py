'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''

import re

def to_camel_case(text):
    words = re.findall(r'[^-_]+', text)
    return print(''.join([words[x] if x == 0 else words[x].title() for x in range(len(words))]))

a = "the-stealth-warrior"
b = "The_stealth_warrior"

for i in [a, b]:
    to_camel_case(i)