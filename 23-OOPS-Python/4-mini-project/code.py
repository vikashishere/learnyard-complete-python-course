class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no}) - Marks: {self.marks}"

    def __lt__(self, other):
        return self.marks < other.marks

    def __eq__(self, other):
        return self.marks == other.marks


# List to store student objects
students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number!")
        return
    student = Student(name, roll, marks)
    students.append(student)
    print("Student added!\n")

def display_all_students():
    if not students:
        print("No students in the system.\n")
        return
    for s in students:
        print(s)
    print()

def compare_students():
    if len(students) < 2:
        print("Need at least 2 students to compare.\n")
        return
    print("Comparing first two students in the list:\n")
    s1, s2 = students[0], students[1]
    print(s1)
    print(s2)

    if s1 > s2:
        print(f"\n{s1.name} has more marks than {s2.name}")
    elif s1 < s2:
        print(f"\n{s2.name} has more marks than {s1.name}")
    else:
        print("\nBoth students have equal marks")


def menu():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Compare First Two Students")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            compare_students()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the menu
if __name__ == "__main__":
    menu()




# 🧪 Sample Run
# ----- Student Management System -----
# 1. Add Student
# 2. Display All Students
# 3. Compare First Two Students
# 4. Exit
# Enter your choice: 1
# Enter student name: Rahul
# Enter roll number: 23
# Enter marks: 89
# Student added!

# ...

# Rahul (Roll No: 23) - Marks: 89
# Neha (Roll No: 12) - Marks: 93

# Neha has more marks than Rahul



# 💡 Extension Ideas
# Add option to remove a student
# Store students in a file (next module)
# Sort students by marks
# Add subject-wise marks