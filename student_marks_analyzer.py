
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

topper = max(students, key=students.get)

total = 0
failures = []

for name, marks in students.items():
    total = total + marks

    if marks < 33:
        failures.append(name)

average = total / n

print("\nStudent Marks:", students)
print("Topper:", topper)
print("Highest Marks:", students[topper])
print("Average Marks:", average)
print("Failed Students:", failures)
print("Total Failures:", len(failures))
