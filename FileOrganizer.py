import os
import shutil
import argparse
import sys
from pathlib import Path

# Define file categories and their extensions
FILE_CATEGORIES = {
    "Videos": ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'],
    "Music": ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt'],
    "Archives": ['.zip', '.rar', '.tar', '.gz', '.7z'],
    "Executables": ['.exe', '.bat', '.sh', '.bin', '.app'],
    "Scripts": ['.py', '.js', '.rb', '.php', '.pl']
}

# ANSI escape codes for colors
BLUE = '\033[94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

def organize_files(target_dir):
    target_path = Path(target_dir).resolve()
    
    if not target_path.exists():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return

    print(f"Organizing files in: {target_path}")
    
    stats = {category: 0 for category in FILE_CATEGORIES.keys()}
    stats["Others"] = 0
    total_files = 0

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        (target_path / category).mkdir(exist_ok=True)
    (target_path / "Others").mkdir(exist_ok=True)

    # Recursive walk through the directory
    # We collect files first to avoid moving things while iterating if they end up in the same dir
    files_to_move = []
    for root, dirs, files in os.walk(target_path):
        root_path = Path(root)
        
        # Skip the category folders themselves to avoid infinite loops or moving organized files
        rel_path = root_path.relative_to(target_path)
        if rel_path.parts and rel_path.parts[0] in list(FILE_CATEGORIES.keys()) + ["Others"]:
            continue

        for file in files:
            files_to_move.append(root_path / file)

    for file_path in files_to_move:
        extension = file_path.suffix.lower()
        moved = False
        
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                dest_dir = target_path / category
                try:
                    # Handle name collisions
                    dest_path = dest_dir / file_path.name
                    if dest_path.exists():
                        # Simple collision handling: append counter
                        count = 1
                        while (dest_dir / f"{file_path.stem}_{count}{file_path.suffix}").exists():
                            count += 1
                        dest_path = dest_dir / f"{file_path.stem}_{count}{file_path.suffix}"
                    
                    shutil.move(str(file_path), str(dest_path))
                    stats[category] += 1
                    moved = True
                except Exception as e:
                    print(f"Failed to move {file_path.name}: {e}")
                break
        
        if not moved:
            dest_dir = target_path / "Others"
            try:
                dest_path = dest_dir / file_path.name
                if dest_path.exists():
                    count = 1
                    while (dest_dir / f"{file_path.stem}_{count}{file_path.suffix}").exists():
                        count += 1
                    dest_path = dest_dir / f"{file_path.stem}_{count}{file_path.suffix}"

                shutil.move(str(file_path), str(dest_path))
                stats["Others"] += 1
            except Exception as e:
                print(f"Failed to move {file_path.name} to Others: {e}")
        
        total_files += 1

    print(f"\n{GREEN}Organization complete!{ENDC}")
    print(f"Total files organized: {total_files}")
    for category, count in stats.items():
        print(f" - {category}: {count}")

    print(f"\n{BLUE}If you like this project and want to support its development, you can donate here: https://www.paypal.com/paypalme/EnricoArama{ENDC}")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by type.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Group command
    group_parser = subparsers.add_parser("group", help="Group files in the specified folder")
    group_parser.add_argument("path", help="Path to the folder to organize")

    args = parser.parse_args()

    if args.command == "group":
        organize_files(args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
