#reversing of names and display


students_name = []
students = int(input("Enter the number of students: "))

for i in range(students):
    name = input(f"Enter the name of student {i + 1}: ")
    students_name.append(name[:15])

print("\nOriginal Names:")
for student in students_name:
    print(student)

print("\nReversed Names:")
for student in students_name:
    print(student[::-1])