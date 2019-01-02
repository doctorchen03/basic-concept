#List is a collection which is ordered and changeable. Allows duplicate members.
#initialize
list1 = ['a','b','c']
print(list1)
#get the list data type.
print(type(list1))
#update the item value.
list1[0] = 'A'
print(list1)
#loop through the list
for index in range(0,len(list1)):
    print(list1[index])
#add an item to the end of the list.
list1.append('D')
print(list1)
#add an item to the specified index position.
list1.insert(0,'e')
print(list1)
#delete the specified item.
del list1[1]
print(list1)
#format the list
list1.clear()
print(list1)
