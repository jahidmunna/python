import csv
# open the file in universal line ending mode
with open("G:/CodePracticing/pythonCode/DataResources/playerData(BaseBall).csv", 'rU') as infile:
    # read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]
# extract the variables you want
names = data['Name']
ages = data['Age']
ages = list(map(float,ages))
print(type(ages))

# print(names)
# print(ages)
