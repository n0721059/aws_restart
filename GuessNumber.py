import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")





number = random.randint(1,10)

guess = input("enter a number between 1 and 10: ") 
# print("the number user has chosen is {} and of type {}".format(guess, type(guess)))


isGuessRight = False

casted= int(guess)
print("the number randomly chosen is {} and of type {}".format(number, type(number)))
# print("the number user has chosen is {} and of type {}".format(guess, type(guess)))

while isGuessRight != True:
    if casted == number:
        print("Congratulations **** {} is the right guess".format(number))
        isGuessRight = True
    else:
            print("{} was unlucky Guess.. you may try again".format(guess))
            guess = input("enter a number between 1 and 10: ") 
            
            
            
            

