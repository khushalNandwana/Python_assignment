#to-do list application
def create_to_do_list():
    
    return {}

def add_task(todo_list, task):
   
    todo_list[task] = False  

def mark_complete(todo_list, task):
    
    if task in todo_list:
        todo_list[task] = True 
        print("Task completed successfully")
    else:
        print(f"Task '{task}' not listed.")

def view_pending(todo_list):
    
    for task, done in todo_list.items():
        if not done:
            print(f"Pending Task-{task}")
    if done:
        print("No task pending")
    
def view_completed(todo_list):
    
    for task, done in todo_list.items():
        if done:
            print(f"- {task}")
            print("Completed Tasks:")
        else:
            print("No task completed")

def main():
    my_list = create_to_do_list()

    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. Mark as Completed")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
     
        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter new task: ")
            add_task(my_list, new_task)
            print("new task successfully added")
        elif choice == '2':
            complete_task = input("Enter the completed task: ")
            mark_complete(my_list, complete_task)
            
        elif choice == '3':
            view_pending(my_list)
        elif choice == '4':
            view_completed(my_list)
       
        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    main()
