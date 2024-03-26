import os
import sys
from exifread import process_file


def filter_files(current_dir, other_dir=None):
    num_files = len(os.listdir(current_dir))
    print(f"Found {num_files} files in {current_dir}")

    # Get a list of allowed file extensions
    allowed_extensions = ['.heic', '.jpg', '.jpeg', '.png', '.mov', '.mp4']

    # Iterate through all files in current_dir
    for file_name in os.listdir(current_dir):
        file_path = os.path.join(current_dir, file_name)

        # Check if file is not a directory and its extension is not allowed or it contains "_E" in its name
        if os.path.isfile(file_path) and (
                not file_name.lower().endswith(tuple(allowed_extensions)) or "_E" in file_name):
            # Delete the file from current_dir
            os.remove(file_path)
            print(
                f"Deleted file '{file_name}' from {current_dir} because it has an invalid extension "
                f"or contains '_E' in its name.")

        # If a HEIC file with the same name and date taken exists
        elif file_name.lower().endswith(('.jpg', '.jpeg')):
            jpg_date_taken = get_date_taken(file_path)
            if jpg_date_taken:
                heic_file_name = file_name.split('.')[0] + '.heic'
                heic_file_path = os.path.join(current_dir, heic_file_name)
                if os.path.exists(heic_file_path):
                    heic_date_taken = get_date_taken(heic_file_path)
                    if jpg_date_taken == heic_date_taken:
                        # Delete the file from current_dir
                        os.remove(file_path)
                        print(f"Deleted JPEG file '{file_name}' from {current_dir} because a same HEIC file '{heic_file_name}' exists.")

        # If other_dir is given
        elif other_dir:
            # Check if the file exists in other_dir
            file_exists, other_path = check_file_exists(file_path, other_dir)
            if file_exists:
                # Delete the file from current_dir
                os.remove(file_path)
                print(f"Deleted file '{file_name}' from {current_dir} because it exists in {other_path}.")

    num_files = len(os.listdir(current_dir))
    print(f"There are now {num_files} files in {current_dir}")


def check_file_exists(file_path, other_dir):
    file_name = os.path.basename(file_path)
    date_taken = get_date_taken(file_path)

    # Check if the file exists in other_dir or its subdirectories
    for root, _, files in os.walk(other_dir):
        # If the file with the same name exists
        if file_name in files:
            other_file_path = os.path.join(root, file_name)
            # Get date taken from file in the other directory
            other_date_taken = get_date_taken(other_file_path)
            # Compare the dates taken
            if date_taken and date_taken == other_date_taken:
                print(
                    f"File '{file_name}' with the same name and date taken {date_taken} already exists in {root}.")
                return True, root
    return False, ""


def get_date_taken(file_path):
    # Extract the "Date taken" metadata from the file
    with open(file_path, 'rb') as f:
        try:
            # Require exifread version < 3.0.0 (python -m pip install "exifread<3")
            # Currently using exifread-2.3.2
            tags = process_file(f)
            date_taken = tags.get('EXIF DateTimeOriginal')
            if date_taken is not None:
                return str(date_taken)
            else:
                return None
        except:
            return None


def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py current_directory [other_directory]")
    else:
        current_dir = sys.argv[1]

        # Check if current_dir exists
        if not os.path.isdir(current_dir):
            print(f"Current directory '{current_dir}' does not exist.")
        else:
            if len(sys.argv) == 3:
                other_dir = sys.argv[2]
                if not os.path.isdir(other_dir):
                    print(f"Other directory '{other_dir}' does not exist.")
                else:
                    filter_files(current_dir, other_dir)
            else:
                filter_files(current_dir)


if __name__ == "__main__":
    main()
