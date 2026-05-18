class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


students = []


def add_student():
    roll = int(input("Enter Roll: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    s = Student(roll, name, marks)
    students.append(s)


def display_students():
    if len(students) == 0:
        print("No student records found")
    else:
        for s in students:
            print(s.roll, s.name, s.marks)


while True:
    print("\n1. Add")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")                                                                                                                                           
