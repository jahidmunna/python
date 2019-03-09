inFile = open('filetest.txt','r')

# oneLine = inFile.readline()
# print(oneLine)

# fileInAsingleString = inFile.read() 
# print(fileInAsingleString)

# # line by line
# for line in inFile:
#     print(line)


# line by line read and write
outFile = open('fileWriteTest.txt','w')
for line in inFile:
    outFile.write(line)
