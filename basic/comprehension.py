# prices = [5,10,15,20]

# print(prices)

# newPrices = []
# for price in prices:
#     newPrices.append(price*2) #2 times higher then prev price
# #print the new prices
# # for price in newPrices:
# #     print (price)

# #same thing can be done using

# newPrices2 = [price*2 for price in prices]
# print(newPrices2)


numbers = [0,1,2,3,4,5,6,7,8,9,10]
evenNumbers = [number for number in numbers if number%2 == 0]
oddNumbers = [number for number in numbers if number%2 != 0]
print(evenNumbers)
print(oddNumbers)
