# stack using list

class stack:
    def __init__(self):
        self.list = []
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        self.list.pop()
    
    def size(self):
        return  len(self.list)
    
    def isEmpty(self):
        return self.size()==0
    
    def printStack(self):
        print(self.list)    


list  = stack()
list.push(1)
list.push(2)
list.push(3)
list.printStack()
list.pop()
list.printStack()
list.pop()
list.printStack() 
if list.isEmpty():
    print('empty')
else:
    print ('not empty')

print('size = ',list.size())    
list.pop()

if list.isEmpty():
    print('empty')
else:
    print ('not empty')

print('size = ',list.size())  