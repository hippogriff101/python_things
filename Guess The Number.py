import random
import time

text = "Welcome to Python Things."
topvalue = 99
timesplayed = 0
totalguesses = 0

time.sleep(1)
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)
time.sleep(1)
print("\nThis game is called 'Guess the Number!'\n")
time.sleep(1)
print(" The aim of the game is to: ")
time.sleep(1)
print("  1. Guess a number.")
time.sleep(1)
print("  2. Use the directions 'Too high'/'Too low' to narrow your guess.")
time.sleep(1)
print("  3. Play again to increase your score.")
time.sleep(1)
print("  4. When you close the game, via the end screen, get your very own 'score' document.")
time.sleep(1)
print("\nLet's Play...\n")

while True:
    dice = random.randint(1, topvalue)
    guesses = 0
    
    while True:
        try:
            guess = int(input("I am thinking of a number between 1 and 99. What do you think it is? "))
            guesses += 1
            totalguesses += 1

            if guess == dice:
                print("You Win!")
                print("")
                break
            elif guess > (topvalue * 2):
                print("WAAAAAAAAY too high")
            elif guess > dice:
                print("Too High")
            elif guess < dice:
                print("Too Low")
        except ValueError:
            print("That's not a valid number. Please try again.")
    
    print(f"You used {guesses} guesses this round.")
    timesplayed += 1
    print("")
    
    while True:
        playagain = input("Do you want to play again? (yes or no): ").lower()

        if playagain == "yes":
            print("")
            break
        elif playagain == "no":
            print("Thanks for playing!")
            
            with open("Scores.txt", "w") as file:
                file.write("Thank you for playing Guess the Number:\n")
                file.write("This is part of my project Python Things.")
                file.write("You can find more projects like this on my GitHub profile:\n")
                file.write("\nhttps://github.com/hippogriff101\n\n")
                file.write("Thank you to arcade for the opportunity to advance my coding knowledge.\n")
                file.write("Find this on the repo called 'quiz_time'.\n\n")
                file.write(f"Scores:\nTimes Played: {timesplayed}\nTotal Guesses: {totalguesses}\n")
            exit()
        else:
            print("Sorry, what was that?")
