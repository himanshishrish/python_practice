''' to get the largest number from a list. 
to sum all the items in a list. 
to multiply all the items in a list.'''
marks=[10,20,30,70,5]
Mul=1
marks.sort()#sort garera ascending order ma data lai rakhxa jasle garda highest vale vako data last ma hunxa
print(marks[len(marks)-1])#its because list ko data ko numbering 0 dekhi suru hunxa
i=0
Sum=0
for item in marks:
    Mul=Mul*item
    Sum=Sum+item
print(Mul)
print(Sum)