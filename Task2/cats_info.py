from pathlib import Path

# Task 2: Read cat information from a file and return a list of dictionaries

def get_cats_info(path):
  
    try: 
        cats = []
        with open(Path(path), "r", encoding="utf-8") as file:
            file_content = file.readlines()
            for cat in file_content:
                try:      
                    cat_id, name, age = cat.strip().split(",")
                    cat_object = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat_object)
                except ValueError:
                    print(f"Error parsing line: {cat.strip()}. Expected format: id,name,age")

        return cats
    except FileNotFoundError:
        print(f"File by path '{Path(path)}' not found.")
        return []









cats_info = "Task2/cats_file.txt"

print(get_cats_info(cats_info))
