marks=[10,20,30,70,5]
marks.sort()
print('Data in ascending order are')
for item in marks:
    print(item)
#marks.reverse()
print('Data in descending order are')
for i in range(len(marks)-1,-1):
    print(marks[i])
