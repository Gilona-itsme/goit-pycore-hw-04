from pathlib import Path

# Task 1: Calculate total and average salary from a file
def total_salary(path):
    try:
        with open(Path(path), "r", encoding="utf-8") as file:
            file_content = file.readlines()
            all_salaries = [int(emploee.split(',')[-1]) for emploee in file_content]
            total = sum(all_salaries)
            average = int(total / len(all_salaries))

        return total, average
   
    except FileNotFoundError:
       print(f"File by path '{path}' not found.")
       return (0, 0)





file_path = "Task1/employees.txt"
total, average = total_salary(file_path)
print(total_salary(file_path))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")         
