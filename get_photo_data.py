import os

# ----------------------------- Collect image files (.jpg, .jpeg) from folder ------------------------
# r = raw string
dir_path = r"D:\Work\_PythonSuli\kezdo-240106\alapok_1\photos"

# check folder validity
while not os.path.exists(dir_path):
    print(f"Path does not exist: {dir_path}")
    dir_path = input("Give me a folder path where you store photos:")

# Collect files in this folder
file_list = os.listdir(dir_path)

# filter out unwanted files
allowed_extensions = [".jpg", ".jpeg"]
photos = []  # create a container for storing only photo files
for file_name in file_list:
    # unpacking values from splittext()
    name, ext = os.path.splitext(file_name)  # os.path.splittext() = IMG_1069, .JPG
    
    # check if extension in allowed_extension
    if not ext.lower() in allowed_extensions:
        continue

    # add this file to photos
    photos.append(os.path.join(dir_path, file_name))


# ----------------------------- Collect meta data (exif data) from image files ------------------------
for image_file in photos:
    print(image_file)