#declaring 
list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}
dictionary = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
}

#inserting single value
list.append(5)
# tuple.append(5) -> can not be done as it's tuple
set.add(5)
dictionary[5] = 'e'

#inserting multiple values
list.extend([6,7])
set.update([6,7])
dictionary.update(
    {
        6: 'f',
        7: 'g'
    }
)

#delete by value
list.remove(3)
set.remove(3)
dictionary.pop(3)

#delete by index
list.pop(1)

#print all 
print("The type ", type(list),"value : ",list)
print("The type ", type(tuple),"value : ",tuple)
print("The type ", type(set),"value : ",set)
print("The type ", type(dictionary),"value : ",dictionary)


#certain value print
print("The type ", type(list),"value : ",list[0])
print("The type ", type(tuple),"value : ",tuple[0])
print("if 1 is in the set ", type(set),"value : ",1 in set)
print("The type ", type(dictionary),"value : ",dictionary[1])

