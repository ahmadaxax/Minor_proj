import random
import math 


lower=int(input("enter the lower bound"))
upper=int(input("enter the upper bound"))

x=random.randint(lower,upper)
print("\n\tyou've only ",
      round(math.log(upper -lower + 1,2)),
      "chances to guess the integer")

count=0

while count < math.log(upper -lower + 1,2):
     count+=1
     guess =int(input("guess the number"))
    
     if x==guess:
         print("congractulations you did it in",count,"try")
         break
     elif x>guess:
         print("you guessed to high")
     elif x<guess:    
         print("you guessed to small")
    
     if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")