#to check if two given sets have no elements in common.
set1={1,2,3}
set2={3,4,5}
i=set1.intersection(set2)
if (i==set()):
    print("No Common")
else:
    print("Common")
#cannot change items but can add