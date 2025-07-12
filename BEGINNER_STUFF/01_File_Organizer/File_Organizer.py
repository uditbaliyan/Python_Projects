import os
import shutil
from datetime import datetime

# Path to the folder you want to organize
TARGET_FOLDER = (
    "/home/udit/Documents/Github/Python_Projects/BEGINNER_STUFF/01_File_Organizer/test"
)


def organize_by_type(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            ext = item.split(".")[-1].lower()
            if ext == item:  # No extension
                ext = "no_extension"

            dest_dir = os.path.join(folder_path, ext.upper())
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_dir, item))


def organize_by_date(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            mod_time = os.path.getmtime(item_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

            dest_dir = os.path.join(folder_path, date_folder)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_dir, item))


def main():
    print("Choose organization method:")
    print("1. By file type")
    print("2. By modified date")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        organize_by_type(TARGET_FOLDER)
    elif choice == "2":
        organize_by_date(TARGET_FOLDER)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
