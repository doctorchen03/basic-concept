
list1 = ['a','b','c']
print(list1)
print(type(list1))
list1[0] = 'A'
print(list1)

for index in range(0,len(list1)):
    print(list1[index])

list1.append('D')
print(list1)
list1.insert(0,'e')
print(list1)
del list1[1]
print(list1)
list1.clear()
print(list1)