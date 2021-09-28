'''to count the number of even and odd numbers from a series of numbers. 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5'''
def checker():
    e=0
    o=0
    numbers = [12, 14, 11, 85, 74, 89, 16, 57, 100, 96]

    for i in numbers:
        r=i % 2
        if r==0:
            e=e+1
        else:
            o=o+1 
    print("Number of even numbers :"+str(e))
    print("Number of odd numbers :"+str(o)) 
checker()    
