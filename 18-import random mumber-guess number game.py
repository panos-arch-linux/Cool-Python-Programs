#imports random lib and creates a random number between one and a one million
import random 
a=random.randint(1,1000000)
attempt = 0
print("One-Million-To-One")
while True:
    guess = int(input("What is your guess?")) 
    if guess < a:
        print("Too small")
        attempt = attempt + 1   # adds one failed attempt
        continue
    elif guess > a:
        print("Too high")
        attempt = attempt + 1   # adds one failed attempt
        continue
    elif guess == a:
        print("Correct!")
        print("It took you" ,attempt, "guesses to get it correct!") # congrats and print how many attempts it took
        break
