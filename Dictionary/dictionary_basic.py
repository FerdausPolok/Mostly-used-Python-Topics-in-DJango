#key value pair

myDict={
    "name": "Polok",
    "age": 24,
    "location": "Dhaka"
}
print(myDict)

#define empty dict
my_empty_dict={}

print(my_empty_dict)
print(type(my_empty_dict))

my_empty_dict= dict()

print(my_empty_dict)
print(type(my_empty_dict))

my_empty_dict['key1'] = "Zaman"

print(my_empty_dict)

#value change - > reqrite korlei hobe


my_empty_dict['key1'] = "Ferdaus"

print(my_empty_dict)

my_empty_dict['key2'] = "YoYo"

print(my_empty_dict)

#removing

del my_empty_dict["key2"]

print(my_empty_dict)