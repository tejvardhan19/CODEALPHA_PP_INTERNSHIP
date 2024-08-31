import os
import shutil


def organize_files(directory):
    """
    Organize files in the specified directory into subdirectories based on file extensions.
    """
    # List all files in the directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension[1:] or 'no_extension'

            # Create a subdirectory for the file extension if it doesn't exist
            extension_dir = os.path.join(directory, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            # Move the file into the appropriate subdirectory
            shutil.move(file_path, os.path.join(extension_dir, filename))

            print(f"Moved {filename} to {extension_dir}")


if __name__ == "__main__":
    # Specify the directory you want to organize
    target_directory = 'path/to/your/directory'
    organize_files(target_directory)
