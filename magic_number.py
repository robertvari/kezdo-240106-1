import random

max_number = 10

# Game intro
print("*"*50, "MAGIC NUMBER GAME", "*"*50)

print("-"*50)
# Game rules
print(f"I have number between 1 and {max_number}. Can you guess it?")
print("-"*50)

magic_number = random.randint(1, max_number)
player_number = input("What is my magic number?")