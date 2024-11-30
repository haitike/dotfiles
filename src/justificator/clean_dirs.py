import os
import shutil

# Define the base directories
images_folder = "justificacion/images"
images_justificated_folder = "justificacion/images_justificated"
images_old_folder = "justificacion/images_old"
images_justificated_old_folder = "justificacion/images_justificated_old"



# Define the destination directories based on the prompt
destination_images_folder = images_old_folder
destination_images_justificated_folder = images_justificated_old_folder

# Check if the destination folders already exist
if os.path.exists(destination_images_folder) or os.path.exists(destination_images_justificated_folder):
    print(f"Error: The folder already exists in images_old or images_justificated_old. No files were moved.")
else:
    # Function to move files and preserve structure
    def move_files_and_preserve_structure(source_folder, destination_folder):
        for root, dirs, files in os.walk(source_folder, topdown=False):
            # For each directory, create the same structure in the destination folder
            relative_path = os.path.relpath(root, source_folder)
            new_directory = os.path.join(destination_folder, relative_path)
            os.makedirs(new_directory, exist_ok=True)

            # Move files to the new directory
            for filename in files:
                source_file = os.path.join(root, filename)
                destination_file = os.path.join(new_directory, filename)
                shutil.move(source_file, destination_file)

    # Move files from images/ to images_old/prompt_input
    move_files_and_preserve_structure(images_folder, destination_images_folder)

    # Move files from images_justificated/ to images_justificated_old/prompt_input
    move_files_and_preserve_structure(images_justificated_folder, destination_images_justificated_folder)

    # At this point, all files are moved, and the subfolder structure is preserved in both images/ and images_justificated/
    print(f"All subfolders and files have been moved to {destination_images_folder} and {destination_images_justificated_folder}. The original structure is preserved in both images/ and images_justificated/ without the files.")
