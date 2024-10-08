import random

easy = random.randint(1, 10)
medium = random.randint(1,20)
hard = random.randint(1,50)
extreme = random.randint(1,100)

guessTaken = 0
difficulty = input(("Welcome to the number guessing game! Type your difficulty level ->    ") + ("EASY / MEDIUM / HARD / EXTREME: "))

if difficulty == "easy":
    number = easy
    print("Okay, I'm thinking of a number 1 and 10...")
if difficulty == "medium":
    number = medium
    print("Okay, I'm thinking of a number 1 and 20!...")
if difficulty == "hard":
    number = hard
    print("Okay, I'm thinking of a number 1 and 50!...")
if difficulty == "extreme":
    number = extreme
    print("Okay, I'm thinking of a number 1 and 100!...")


while guessTaken < 6:
    guess = int(input('You have 6 tries. What number am I thinkeing of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Incredible! you guessed the number in {guessTaken} tries!")
        break

    guess = int(input('You have 5 tries left. What number am I thinkeing of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Nice! you guessed the number in {guessTaken} tries!")
        break

    guess = int(input('You have 4 tries left. What number am I thinkeing of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Amazing! you guessed the number in {guessTaken} tries!")
        break

    guess = int(input('You have 3 tries left. What number am I thinkeing of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Sick! you guessed the number in {guessTaken} tries!")
        break

    guess = int(input('You have 2 tries left. What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Good job! you guessed the number in {guessTaken} tries!")
        break
    break
 
if guessTaken != 5:
    int(input("Last try! What number am I thinking of?: "))
elif guess < number:
        print('Your guess is too low.')
elif guess > number:
        print('Your guess is too high.')
else:
    guessTaken == 6 and guess != number
    print(f"Sorry, no more tries! The number I was thinking of was {number}!")
    
