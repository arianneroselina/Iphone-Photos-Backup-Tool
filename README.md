# Iphone Photos Backup Tool

Iphone Photos Backup Tool is a Python script designed to clean up files in a specified directory based on certain criteria.
It deletes
1. files with unallowed file extensions,
2. files containing "_E" in their names,
3. JPEG/JPG files if a HEIC file with the same name and "Date taken" metadata exists in the same directory,
4. files that already exist in another directory (recursively) while comparing their file name and "Date taken" metadata,

Permitted file extensions are '.heic', '.jpg', '.jpeg', '.png', '.mov', '.mp4'.

## Requirements
- Python 3
- exifread < 3

## Installation

1. Clone or download the repository to your local machine:

    ```bash
    git clone https://github.com/arianneroselina/IphonePhotosBackupTool.git
    ```

2. Install dependencies using pip:

    ```bash
    python -m pip install "exifread<3"
    ```

## Usage

```bash
python filter_files.py current_dir [other_dir]
```

- `current_dir`: Path to the directory containing the files to clean.
- `other_dir` (optional): Path to the directory for comparison.

If only current_dir is provided, the tool will clean up files in current_dir according to the specified criteria 1-3.
If both current_dir and other_dir are provided, the tool will also compare files between the two directories.

### Example

```bash
# Clean up files in current_dir only
python filter_files.py "iPhone\202312__"

# Clean up files in current_dir and compare with other_dir (recursively)
python filter_files.py "iPhone\202312__" "Pictures"
```
