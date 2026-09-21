from pathlib import Path
import shutil
import sys

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Documents": [".txt", ".doc", ".docx", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"

def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1
    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent

    while True:
        new_destination = parent / f"{stem} ({counter}){suffix}"
        if not new_destination.exists():
            return new_destination
        counter += 1


def organize(folder):
    for item in folder.iterdir():
        if not item.is_file():
            continue

        category = get_category(item.suffix.lower())
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)

        destination = target_dir / item.name
        destination = get_unique_destination(destination)

        shutil.move(str(item), str(destination))
        print(f"Moved {item.name} -> {destination.relative_to(folder)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organizer.py <folder_path>")
        sys.exit(1)

    target_folder = Path(sys.argv[1])

    if not target_folder.is_dir():
        print(f"Error: {target_folder} is not a valid folder")
        sys.exit(1)

    organize(target_folder)

