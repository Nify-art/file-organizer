from pathlib import Path
import shutil
import sys
import json


def load_categories(config_path):
    with open(config_path, "r") as f:
        return json.load(f)


def get_category(extension, categories):
    for category, extensions in categories.items():
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


def organize(folder, categories, dry_run=False):
    for item in folder.iterdir():
        if not item.is_file():
            continue

        category = get_category(item.suffix.lower(), categories)
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)

        destination = target_dir / item.name
        destination = get_unique_destination(destination)

        if dry_run:
            print(f"Would move {item.name} -> {category}/{destination.name}")
        else:
            try:
                shutil.move(str(item), str(destination))
                print(f"Moved {item.name} -> {destination.relative_to(folder)}")
            except (PermissionError, OSError) as e:
                print(f"Skipped {item.name}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path> [--dry-run]")
        sys.exit(1)

    target_folder = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv

    if not target_folder.is_dir():
        print(f"Error: {target_folder} is not a valid folder")
        sys.exit(1)

    categories = load_categories(Path(__file__).parent / "categories.json")
    organize(target_folder, categories, dry_run=dry_run)