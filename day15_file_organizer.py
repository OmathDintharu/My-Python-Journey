import os
import shutil

path = r'C:\Users\MyPlusComputers\Pictures\project_01'

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if extension in ["png", "jpg", "jpeg"]:
        folder_name = "Images"
    elif extension in ["py", "html", "js"]:
        folder_name = "Codes"
    else:
        folder_name = "Others"

    if not os.path.exists(path + '/' + folder_name):
        os.makedirs(path + '/' + folder_name)

    shutil.move(path + '/' + file, path + '/' + folder_name + '/' + file)

print("\nYou are all set!")


input("\nPress Enter to exit...")
