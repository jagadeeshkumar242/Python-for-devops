import os
folders = input("Please enter the folders and kindly maintian the spaces in between them: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name and that you give is an invalid folder" + folder)
        break
    print("==== listing files for a folder - " + folder)
    for file in files:
        print(file)
