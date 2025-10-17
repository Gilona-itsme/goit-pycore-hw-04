from pathlib import Path
import sys
from iterate_folders import iterate_folder
from color_rules import  ERROR_COLOR

#Task 3: Main script to run the folder iteration

def main():
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
    else:
        directory_path = input("Enter directory path: ")

    core_path = Path(directory_path)

    if core_path.exists() and core_path.is_dir():
        iterate_folder(core_path)
    else:
        print(f"{ERROR_COLOR}The path '{core_path}' does not exist or is not a directory.")
        sys.exit(1)


if __name__ == '__main__':
    main()


