#to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
student={}
l=15
i=1
while i<l:
    j=i*i
    student.update({i:j})
    i=i+1
print(student)