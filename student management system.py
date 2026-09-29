students = []


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("\nStudent added successfully!")


def display_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n----- STUDENT DETAILS -----")

    for student in students:
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("---------------------------")


def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("\nStudent not found.")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


def update_student():
    roll = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found.")


while True:

    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")
