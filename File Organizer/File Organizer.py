# Organizes files in a folder into subfolders based on their type.

import os
import shutil

print("📂 Welcome to the File Organizer!")
folder_path = input("Enter the full path of the folder you want to organize: ")

if not os.path.exists(folder_path):
    print("The folder path does not exist. Please check and try again.")
else:
    # Define file categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Archives": [".zip", ".rar", ".tar", ".gz"]
    }

    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files found in the folder to organize.")
    else:
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    category_path = os.path.join(folder_path, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    shutil.move(os.path.join(folder_path, file), os.path.join(category_path, file))
                    moved = True
                    break
            if not moved:
                # Move other files to "Others"
                other_path = os.path.join(folder_path, "Others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                shutil.move(os.path.join(folder_path, file), os.path.join(other_path, file))

        print("Folder has been organized successfully!")
