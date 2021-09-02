import random
randomNumber=random.randrange(1,100)
print(randomNumber)
if(randomNumber%3==0 and randomNumber%5==0):
        print("Fizz Buzz")
else:       
    if(randomNumber%3==0)  :
        print("FiZZ")
    elif(randomNumber%5==0):
        print("BUzz")  
    else:
        print("Keep on Trying ")