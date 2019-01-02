#A tuple is a collection which is ordered and unchangeable
#initialize
tuple1 = ('a','b','c')
print(tuple1)
#get the list data type.
print(type(tuple1))
print(tuple1[0])
#tuple1[0] = 'A' #throw error, value assignment isn't allowed.
#print(tuple1)
#loop through the tuple
for i in range(0,len(tuple1)):
    print(tuple1[i])

#delete the specified item.
#del tuple1[0] #throw error, value deletion isn't allowed.
del tuple1 #still, the whole tuple object can be removed.
#print(tuple1)