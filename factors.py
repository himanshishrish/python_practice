#WAP to compute factors of a given number . 
#eg. factors of 12 are : 1, 2, 3, 4, 6, 12 because they have remainder 0 while dividing 12 
def factors(a):
    print("the factors of "+str(a)+" are:")
    v=a+1
    for i in range(1,v):
        if a % i==0:
            print(i)
factors(15)    