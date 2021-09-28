'''to find those numbers which are divisible by 7 and multiple of 5,
 between 1500 and 2700 (both included). '''
def functi_on():
    e=0
    o=0
    for i in range(1500,2700):
        r=i % 7 + i%5
        if r==0:
            print(i)
functi_on() 