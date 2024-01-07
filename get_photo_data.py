import os

# r = raw string
dir_path = r"D:\Work\_PythonSuli\kezdo-240106\alapok_1\photos"

# check folder validity
while not os.path.exists(dir_path):
    print(f"Path does not exist: {dir_path}")
    dir_path = input("Give me a folder path where you store photos:")

# Collect files in this folder
file_list = os.listdir(dir_path)

allowed_extensions = [".jpg", ".jpeg"]

for file_name in file_list:
    # unpacking values from splittext()
    name, ext = os.path.splitext(file_name)  # IMG_1069.JPG = IMG_1069, .JPG
    
    if not ext.lower() in allowed_extensions:
        continue

    print(file_name)