'''
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
'''
from collections import defaultdict

def find_uniq(arr):
    str = {}
    freq = defaultdict(int)

    for s in arr:
        chars = frozenset(s.strip().lower())
        str[chars] = s
        freq[chars] += 1
    print(str[next(filter(lambda x: freq[x] == 1, freq))])

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
#find_uniq([ '', '', '', 'b', 'Bdb', '', 'Harry Potter' ])