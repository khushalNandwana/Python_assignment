student_data = {}  # Dictionary to manage student names and marks

def add_student():
    
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student_data[name] = marks
    print("data added")

def search_student():
    
    name = input("Enter student name: ")
    if name in student_data:
        print(f"Marks for {name}: {student_data[name]}")
    else:
        print("Student not found!")

def update_student():
    
    name = input("Enter student name to update: ")
    if name in student_data:
        new_marks = int(input("Enter new marks: "))
        student_data[name] = new_marks
        print("Student data updated!")
    else:
        print("Student not found!")

def display_menu():
    
    print("\nStudent Record System")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice!")