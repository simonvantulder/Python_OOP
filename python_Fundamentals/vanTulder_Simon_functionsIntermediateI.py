#1
import random

def randInt(min=0, max=100):
    temp=0
    if min>max:
        temp=min
        min=max
        max=temp
    num = random.random() * (max-min) + min
    return round(num)
print(randInt(max=50,min=-20))


#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500