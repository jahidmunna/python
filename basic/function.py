def oddChecker(value):
    if value%2 != 0:
        return True
    return False

evenChecker = lambda value: value%2==0

y = 11
if oddChecker(y):
    print("odd")
else:
    print("even")

if evenChecker(y):
    print ("even")
else:
    print ('odd')