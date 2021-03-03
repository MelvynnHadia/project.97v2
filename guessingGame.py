import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
guess = int(input("Enter a Number: "))

while chances < 5:
    if guess==number:
        print("Congratulations, You Won")
        break
    elif guess < number: 
        print("Too Low")
        chances+=1
    else: 
        print("Too High")
        chances+=1
        break
if not chances < 5:
    print("You Lose, the number is", number)
