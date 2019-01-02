#A dictionary is a collection which is unordered, changeable and indexed
#initialize
dict1 = {
    'key1':'val1',
    'key2':'val2',
    'key3':'val3'
    }
print(dict1)
#get type
print(type(dict1))
#get the item value
print(dict1['key1'])
print(dict1.get('key1'))
#update item value
dict1['key1'] = 'VAL1'
print(dict1)
#add an item
dict1['key4'] = 'VAL4'
print(dict1)
#loop through all keys
for key in dict1:
    print(key)
#loop through all values
for key in dict1:
    print(dict1[key])
for val in dict1.values():
    print(val)
#loop through all keys and values
for key,val in dict1.items():
    print(key,val)
#remove an item
del dict1['key1']
print(dict1)
#clean all dictionary object
dict1.clear()
print(dict1)