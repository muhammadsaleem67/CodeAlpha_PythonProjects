import os
import shutil

# define our folders
# "." where script is running
source_folder = "."
destination_folder = "jpg_images"
# creat destination folder 
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created new folder : {destination_folder}\n")
moved_count = 0
# os and loop: look at every file in the source folder
for filename in os.listdir(source_folder):
    # check if the file is jpg or jpeg
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        # build the full paths for the move command
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        # shutil - move the file from source to destination
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
        moved_count += 1
        print(f"\nTask Complete! Successfully moved {moved_count}, image files.")