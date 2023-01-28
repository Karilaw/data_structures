# def are_you_playing_banjo(name):
#     if name[0] == 'R' or name[0] == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'


# test1 = are_you_playing_banjo("Rawrence")
# print(test1)
# test2 = are_you_playing_banjo("Andrew")
# print(test2)

def smash(words):
    string = ' '.join(words)
    return string


words = ['hello', 'world', 'this', 'is', 'great']
test = smash(words)
print(test)
