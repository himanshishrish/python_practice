#to remove the intersection of a 2nd set from the 1st set.
set1={1,2,3,13}
set2={1,3,4,5}
x=set1.intersection(set2)
set1=set1-x
print(set1)
