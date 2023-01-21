dictionary = {"cat": "Котейка"}
print(dictionary)
print(dictionary["cat"])

animal = "cat"
dictionary[animal] = "kot"

print(dictionary[animal])

del dictionary["cat"]

print(dictionary)

stupid_list = {"Name": "Alex", "Age": "33", "Address": "Himki"}
print(stupid_list.keys())
print(stupid_list.values())

for key in stupid_list:
    print(key)

for key, item in stupid_list.items():
    print(key,item)
