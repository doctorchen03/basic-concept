#A set is a collection which is unordered and unindexed, no duplicates.
#initialize
set1 = {'a','b','c'}
print(set1) #each run time, item sort will be in random order.
print(type(set1))
#print(set1[0]) #throw error, set doesn't support indexing.
for item in set1:
    print(item)

set1.add('A')#add one item
print(set1)
#add multiple items
set1.update(['D','E','F','D']) #duplicated items 'D' will be removed, keep the first one.
print(set1)
#remove an item
set1.remove('D')
print(set1)
#clear all item
set1.clear()
print(set1)