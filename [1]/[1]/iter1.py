#an iterator is an object implemented the iterator protocol, consisting of the methods __iter__() and __next__().
#all values in an iterator object can be traversed.
#String, Lists, tuples, dictionaries, and sets are all iterable.

#String
str1 = 'abcDEFG'
iter1 = iter(str1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
#print(next(iter1)) #throw error, stop iteration.
del iter1
#Lists
list1 = ['a','b','c']
iter1 = iter(list1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
del iter1
#tuples
tuple1 = ('A','B','C')
iter1 = iter(tuple1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
del iter1
#dictionaries
dict1 = {
    'key1':'val1',
    'key2':'val2',
    'key3':'val3'
    }
iter1 = iter(dict1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
del iter1