'''Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'''
list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del list[0]
del list[3:5]
print(list)
''' Write a Python program to extend a list without append.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]'''
data1= [10, 20, 30]
data2=[40, 50, 60,70]
print(data1+data2)
'''Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1'''
sample=[1, 1, 2, 3, 4, 4, 5, 1]
sample[1:2]=[1,12]
print(sample)