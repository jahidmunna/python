from random import shuffle

def rearrange(word):
    wordInAList = list(word)
    print('word in list:  ',wordInAList)
    shuffle(wordInAList)
    return ''.join(wordInAList)

names = ['tiger','monkey','bear','elephant']
rearrangedName = []
for name in names:
    rearrangedName.append(rearrange(name))

print(rearrangedName)    

rearrangedName2 = [rearrange(name) for name in names]
print(rearrangedName2)

rearrangedName3 = list(map(rearrange,names))
print(rearrangedName3)
