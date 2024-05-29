# number guessing game
# you have to input start and end number 
# and guess number between start and end number
import random
start = int(input('Enter lower bond:-'))
end = int(input('Enter upper bond:-'))
n = end - start
number_of_trials = int(7/100*n + 1)
print("you have", number_of_trials, "number of trials")
r = random.randint(start, end)
for i in range(number_of_trials):
    guess = int(input("Guess a number:-"))
    if guess == r:
        print('congratulation you won the game in', number_of_trials, 'number of trials')
        break
    elif guess < r:
        print('you guessed too small!')
    elif guess > r:
        print('you guessed too high!')
    else:
        print('your number of trials are end you lose the game')
        break