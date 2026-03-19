students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!\n")


# View all students
def view_students():
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    print()

def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s["id"] == sid:
            print("Student Found:")
            print(s)
            return
    print("Student not found.\n")

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["age"] = input("Enter new age: ")
            s["course"] = input("Enter new course: ")
            print("Student updated successfully!\n")
            return
    print("Student not found.\n")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")


# Main menu
def menu():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()