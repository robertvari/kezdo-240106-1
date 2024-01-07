import random

# globals
max_number = 10
max_tries = 3

# Game intro
print("*"*50, "MAGIC NUMBER GAME", "*"*50)

print("-"*50)
# Game rules
print(f"I have number between 1 and {max_number}. Can you guess it?")
print("-"*50)

magic_number = random.randint(1, max_number)
print(f"DEBUG magic_number: {magic_number}")

player_number = int( input("What is my magic number?") )

while magic_number != player_number:
    max_tries -= 1

    if max_tries == 0:
        print("Game Over :(")
        exit()

    print(f"Wrong, try again. You have {max_tries} left.")
    player_number = int( input("What is my magic number?") )

print(f"You win! {magic_number} was my number!!!")