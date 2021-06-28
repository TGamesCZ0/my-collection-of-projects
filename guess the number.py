import random
print("I am thinking of a number between 1 and 69. Try to guess the number in less than 10 guesses")
ranNumber = random.randint(1, 50)
numGuess = 0
while True:
    if numGuess == 10:
        print("You lost. Better luck next time!")
        break
    numGuess = numGuess + 1
    print ("Take a guess")
    guess = input()
    if int(guess) == ranNumber:
        print("You Win! You guessed your number in " + str(numGuess) + " guesses!")
        break
    if int(guess) < ranNumber:
        print("Your guess is too low")
    if int(guess) > ranNumber:
        print("Your guess is too high")
input()
