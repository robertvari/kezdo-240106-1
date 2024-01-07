import os

# r = raw string
dir_path = input("Give me a folder path where you store photos:")

# check folder validity
while not os.path.exists(dir_path):
    print(f"Path does not exist: {dir_path}")
    dir_path = input("Give me a folder path where you store photos:")

# Collect files in this folder
file_list = os.listdir(dir_path)

print(file_list)