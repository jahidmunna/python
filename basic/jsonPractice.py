import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(type(y), y)

# dictionary to json
z = json.dumps(y)

# the result in json
print(type(z), z) 