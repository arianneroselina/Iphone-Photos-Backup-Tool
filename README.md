# Iphone Photos Backup Tool

Iphone Photos Backup Tool is a Python script designed to clean up files in a specified directory based on certain criteria.
It removes files
- with unallowed file extensions,
- files containing "_E" in their names,
- and deletes files that already exist in another directory while comparing their file name and "Date taken" metadata.

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
python filter_files.py current_dir other_dir
```

Replace `current_dir` with the path to the directory containing the files to clean,
and `other_dir` with the path to the directory for comparison.

### Example

```bash
python filter_files.py "iPhone\202312__" "Pictures"
```
