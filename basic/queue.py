from collections import deque

class Que:
    def __init__(self):
        self.que = deque()
    
    def enque(self,val):
        self.que.append(val)

    def deque(self):
        self.que.popleft()
    
    def size(self):
        return len (self.que)

    def isEmpty(self):
        return self.size()==0

    
    def printQue(self):
        print(self.que)
    


que = Que()
que.enque(1)
que.enque(2)
que.enque(3)
que.printQue()
print('size = ',que.size())    
que.deque()
que.printQue()
print('size = ',que.size())  
if que.isEmpty():
    print('empty')
else:
    print ('not empty')
que.deque()
que.printQue()
que.deque()
que.printQue()
print('size = ',que.size())  
if que.isEmpty():
    print('empty')
else:
    print ('not empty')