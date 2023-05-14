import json
import csv

def read_students_data(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

def merge_student_data(file_paths):
    merged_data = []
    for file_path in file_paths:
        data = read_students_data(file_path)
        merged_data.extend(data)
    return merged_data

def get_average_grade_by_faculty(students_data, faculty):
    grades = []
    for student in students_data:
        if student["Факультет"].strip().lower() == faculty.strip().lower():
            grades.extend(student["Оценки"])
    if grades:
        return sum(grades) / len(grades)
    else:
        return None

def save_student_data_to_csv(students_data, output_file):
    fieldnames = ["Имя", "Фамилия", "Возраст", "Факультет", "Оценки"]
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_data)

file_paths = ["Матфак.json", "Экономисты.json"]
merged_data = merge_student_data(file_paths)

faculty = input("Введите название факультета: ")
average_grade = get_average_grade_by_faculty(merged_data, faculty)
if average_grade is not None:
    print(f"Средний балл студентов факультета {faculty}: {average_grade:.2f}")
else:
    print(f"Студентов на факультете {faculty} не найдено.")

output_file = "student_data.csv"
save_student_data_to_csv(merged_data, output_file)
print("Информация о студентах сохранена в файл student_data.csv")

