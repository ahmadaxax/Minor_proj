import random 

name=input ("what is your name ?")

print("good luck!",name)

words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(words)

print("guess the characters")

guesses=''

turns=12

while turns >0 :
    failed=0
    
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
                print("\n_")
                failed+=1
    if failed==0:
        print("you win")
        print("\nthe word is",word)
        break
    
    print()
    guess=input("guess the character:\t")                  
    guesses+=guess
    
    if guess not in word:
        turns-=1
        print("wrong")
        print("you have,",+ turns,"more guesses")
        if turns==0:
          print("you loose")    