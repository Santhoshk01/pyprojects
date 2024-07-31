# import libraries
import math
import random

# taking inputs
a = int(input("Enter lower value: "))
b = int(input("Enter upper value: "))

# generate a random number
x = random.randint(a,b)
chances = math.ceil(math.log(b - a +1, 2))
print(f"You have only {chances} chances to guess!\n")

# initialize guess count
count = 0
flag = False

# guessing game
while count < chances:
    count += 1

    # guess input
    guess = int(input("Enter your guess: "))

    # conditional to be printed
    if guess == x:
        print(f"Congrats! You guessed it in {count} try")
        flag = True
        break
    elif guess < x:
        print(f"Your guess is small, Try again! \nYou have {chances-count} trails left")
    elif guess > x:
        print(f"Your guess is large, Try again! \nYou have {chances-count} trails left")
    
# when guess count exceeded
if not flag:
    print(f"\nThe number is {x}")
    print("\nBetter luck next time!")