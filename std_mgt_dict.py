student_data={}

while True:
    print("\nStudent data Management:")
    print("1. Add student")
    print("2. Search Student")
    print("3. Update Marks")
    

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student_data[name] = marks
        print("data added")

    elif choice == '2':
        search_student = input("Enter student name: ")
        if search_student in student_data:
            print(f"{search_student}: {student_data[search_student]}")
        else:
            print("student data not found")

    elif choice == '3':
        update= input("Enter student name: ")
        if update in student_data:
            new_marks = int(input("Enter new marks: "))
            student_data[update] = new_marks
            print("marks updated")
        else:
            print("Student data not found")
    else:
        print("Invalid input please try again")
