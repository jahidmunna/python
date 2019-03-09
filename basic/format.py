num1 = 3.14156546
num2 = 2.55666545

print('number 1 is',num1,'number 2 is',num2)

print ('number 1 is {0} number 2 is {1}'.format(num1,num2)) #produces the exact same result

print (f'number 1 is {num1} number 2 is {num2}'.format(num1,num2)) #another version that produces the same result


#{0:.4} produce total 4digits
#{0:.4f} produces 3 digits after decimal
print ('number 1 is {0:.3f} number 2 is {1:.3}'.format(num1,num2)) 
print (f'number 1 is {num1:.3f} number 2 is {num2:.3}'.format(num1,num2)) #another version that produces the same result
