import os
import sys

def filter_files(current_dir, other_dir):
    # Get a list of allowed file extensions
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.mov', '.mp4']

    # Iterate through all files in current_dir
    for file_name in os.listdir(current_dir):
        file_path = os.path.join(current_dir, file_name)

        # Check if file is not a directory and its extension is not allowed or it contains "_E" in its name
        if os.path.isfile(file_path) and (
                not file_name.lower().endswith(tuple(allowed_extensions)) or "_E" in file_name):
            # Delete the file from current_dir
            os.remove(file_path)
            print(
                f"Deleted file '{file_name}' from {current_dir} because it has an invalid extension or contains '_E' in its name.")
        else:
            # Check if the file exists in other_dir
            file_exists, other_path = check_file_exists(file_name, other_dir)
            if file_exists:
                # Delete the file from current_dir
                os.remove(file_path)
                print(f"Deleted file '{file_name}' from {current_dir} because it exists in {other_path}.")

def check_file_exists(file_name, other_dir):
    # Check if the file exists in other_dir or its subdirectories
    for root, _, files in os.walk(other_dir):
        if file_name in files:
            return True, root
    return False, ""

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py current_directory other_directory")
    else:
        current_dir = sys.argv[1]
        other_dir =sys.argv[2]

        # Check if current_dir exists
        if not os.path.isdir(current_dir):
            print(f"Current directory '{current_dir}' does not exist.")
        else:
            # Check if other_dir exists
            if not os.path.isdir(other_dir):
                print(f"Other directory '{other_dir}' does not exist.")
            else:
                # Filter files from current_dir
                filter_files(current_dir, other_dir)

if __name__ == "__main__":
    main()
