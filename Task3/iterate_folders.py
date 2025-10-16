from pathlib import Path
import sys, re
from color_rules import DIR_COLOR, FILE_COLOR, ERROR_COLOR

def iterate_folder(path, level=0, indent: str = ""):
    
    try:
        files = sorted([f for f in path.iterdir() if not f.name.startswith('.')])
        for file in files:
            if file.name.startswith('.'):
                continue
            if file.is_dir():
                result =  f"{indent}{DIR_COLOR}{file.name}/"
                print(result)
                iterate_folder(file,level +1, indent + "    ")
            else:
                current_indent = "" if level == 0 else indent 
                print(f"{current_indent}{FILE_COLOR}{file.name}")

        
    except PermissionError:
        print (f"{indent}{ERROR_COLOR}Permission denied: {file}")
    except Exception as e:
        print (f" {indent} {ERROR_COLOR}Error accessing {file}: {e}")



#iterate_folder(Path("/Volumes/Ilona_G/Python_Woolfs/goit-pycore-hw-04"))


