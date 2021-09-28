'''WAP to compute factorialss of a given number . 
eg. factors of 5  is 120. ie. 1*2*3*4*5= 120
'''
def factorials(a):
    m=1
    n=a+1
    for i in range(1,n):
        m=m*i
    print("the factorial of "+str(a)+" is "+str(m))  
factorials(9)    