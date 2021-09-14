'''to create a set.
to create a union of sets.'''
set1={1,2,3}
set2={1,4,5,6}
set3=set1.union(set2)
print(type(set1))
print(set1)
print(set2)
print(set3)
print("---------------------------------------------------------------")
'''to add member(s) in a set.
to remove item(s) from a given set.'''
set3.remove(5)
set3.add(13)
print (set3)
print("---------------------------------------------------------------")
#to create an intersection of sets.
x=set1.intersection(set2)
print(x)
print("---------------------------------------------------------------")
#to remove all elements from a given set.
set3.clear()
print (set3)
