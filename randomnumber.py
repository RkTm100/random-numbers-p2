import random
#winner=random.randint(1,9)

chance=5

print("Number guessing game")
winner=random.randint(1,9)

while chance<=5:
  guess=int(input("What is the number: "))

  if guess==winner:
    print("you Win")
    break
  elif guess!=winner and chance<=5 and guess<winner:
    print("Incorrect, try again. Guess a number higher than " + str(guess))
    chance=chance-1
  else:
    print("Incorrect, try again. Guess a number lower than " + str(guess))
    chance=chance-1

  if  chance<=0:
    print("You lose, the correct number is:  " + winner)
    break
