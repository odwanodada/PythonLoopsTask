import random
random_number = random.randint(1,10)
myGuess = 3
while  myGuess <= 3:
    guess = int(input("Please enter a random number\n"))
    if guess==random_number:
       print("you won!")
       continue
    else:
       print("You lose!")
       myGuess = myGuess-1
       break

