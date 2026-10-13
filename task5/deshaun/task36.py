import random
n = random.randint(1, 100)
guesses = 0
guess = int(input("guess a number between 1 and 100: "))
while guess != n and guesses < 10:
    guesses += 1
    if guess > n:
        print("too high")
    else:
        print("too low")
    guess = int(input("guess again: "))

if guess == n:
    print("you win!")
else:
    print("you lost!") 