# File Organizer

A Python script that organizes files in a folder into subfolders based on file type (Images, PDFs, Documents, Spreadsheets, Archives, Other).

## Usage

python organizer.py <folder_path> [--dry-run]

Examples:

python organizer.py test_folder --dry-run
python organizer.py test_folder

## Features

- Sorts files into categorized subfolders
- Handles duplicate filenames by appending a number instead of overwriting
- Skips folders, only processes files
- Categories are configurable via categories.json
- Dry-run mode to preview changes without moving anything
- Skips locked/inaccessible files instead of crashing