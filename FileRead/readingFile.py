# inFile = open('FileRead/test.txt')

# for line in inFile:
#     print(line.rstrip())
# inFile.close();

list = []
with open('FileRead/test.txt') as inFile:
    line = inFile.readlines()
    list.append(line)

for i in list:
    print(i)
    