# with open("students.csv", "r", encoding="utf-8") as file:
#   print(file.read())

# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     students = list(reader)
#     print(students)

# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#   reader = csv.DictReader(file)
#   students = list(reader)

# for s in students:
#   chinese = int(s["chinese"])
#   english = int(s["english"])
#   math = int(s["math"])
#   average = (chinese + english + math) / 3
#   print(s["name"], average)

import csv

students = []
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        chinese = int(row["chinese"])
        english = int(row["english"])
        math = int(row["math"])
        avg = (chinese + english + math) / 3

        students.append({
            "name": row["name"],
            "chinese": chinese,
            "english": english,
            "math": math,
            "avg": avg
        })

names = []
for s in students:
    names.append(s["name"])
print("1. 所有學生姓名:")
print(", ".join(names))

print("\n2. 每位學生三科平均:")
for s in students:
    print(f"{s['name']}: {s['avg']:.2f}")

top_student = students[0]
for s in students:
    if s["avg"] > top_student["avg"]:
        top_student = s

print(f"\n3. 最高平均：{top_student['name']} {top_student['avg']:.2f}")

def get_math_score(student):
    return student["math"]

print()

top_math = max(students, key=get_math_score)
print(f"4. 數學最高：{top_math['name']} {top_math['math']}")

print()

total_score = 0
for s in students:
    total_score += s["chinese"] + s["english"] + s["math"]

class_avg = total_score / (len(students) * 3)
print(f"5. 全班平均：{class_avg:.2f}")

print()

print("Challenge:")
print("數學比英文高 10 分以上的學生:")
for s in students:
    if s["math"] - s["english"] >= 10:
        print(f"{s['name']}")