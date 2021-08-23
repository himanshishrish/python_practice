import random
randomNumber=random.randrange(1,100)
print(randomNumber)
if(randomNumber%3==0 and randomNumber%5==0):
        print("Fizz Buzz")
elif(randomNumber%3==0 or randomNumber%5==0):       
    if(randomNumber%3==0)  :
        print("FiZZ")
    else:
        print("BUzz")  
else:
    print("Keep on Trying ")