import re
def song_decoder(song):
    return ' '.join([str(x) for x in re.split('WUB', song) if x != ''])

'''
CLEVER METHOD
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())
'''

a = "AWUBBWUBC"
b = "AWUBWUBWUBBWUBWUBWUBC"
c = "WUBAWUBBWUBCWUB"
d = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"

for i in [a,b,c,d]:
    print(song_decoder(i))
