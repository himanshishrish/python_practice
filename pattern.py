'''to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
def pattern():
    hhh="*"
    for i in range(1,6):
        print(hhh)
        hhh+="*"
    for i in range(4,0,-1):
        print(hhh[0:i])

pattern()    