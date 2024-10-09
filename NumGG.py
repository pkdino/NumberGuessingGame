import random

easy = random.randint(1, 10)
medium = random.randint(1,50)
hard = random.randint(1,100)
extreme = random.randint(1,1000)

guessTaken = 0
difficulty = input(("Welcome to the number guessing game! Type your difficulty level ->  ") + ("EASY / MEDIUM / HARD / EXTREME: "))

if difficulty == "easy":
    number = easy
    print("Okay, I'm thinking of a number between 1 and 10...")
if difficulty == "medium":
    number = medium
    print("Great, I'm thinking of a number between 1 and 50!...")
if difficulty == "hard":
    number = hard
    print("Let's make it more challenging. I'm thinking of a number between 1 and 100...")
if difficulty == "extreme":
    number = extreme
    print("You asked for it! I'm thinking of a number between 1 and 1000...")


while guessTaken < 6:
    guess = int(input('You have 6 tries. What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Incredible! you guessed the number {number} in {guessTaken} tries!")
        break

    guess = int(input('You have 5 tries left. What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Nice! you guessed the number {number} in {guessTaken} tries!")
        break

    guess = int(input('You have 4 tries left. What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Amazing! you guessed the number {number} in {guessTaken} tries!")
        break

    guess = int(input('You have 3 tries left. What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Sick! you guessed the number {number} in {guessTaken} tries!")
        break

    guess = int(input('You have 2 tries left. What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        print(f"Good job! you guessed the number {number} in {guessTaken} tries!")
        break
    
    guess = int(input('Last try! What number am I thinking of? TYPE HERE ->: '))
    guessTaken = guessTaken + 1
    if guess < number:
        print(f'Sorry! Your guess was too low. I was thinking of the number {number}!')
    elif guess > number:
        print (f'Unfortunately, your guess was too high. I was thinking of the number {number}!')
    else:
        print(f"Outstanding! You guessed the number {number} in all {guessTaken} tries!")
        break
    break
