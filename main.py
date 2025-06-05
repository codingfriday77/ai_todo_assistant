from database import connect_db, add_task, get_tasks, complete_task

def show_tasks():
    tasks = get_tasks()
    if not tasks:
        print("✅ No pending tasks.")
    for task in tasks:
        print(f"[{task[0]}] {task[1]} | {task[2] or 'No date'} {task[3] or 'No time'}")

def main():
    connect_db()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("You can type something like: 'Remind me to call dad tomorrow at 5pm'")
            use_ai = input("Use AI to extract task details? (y/n): ").lower()
        
            if use_ai == 'y':
                from nlp_parser import parse_task_from_text
                sentence = input("Enter your task sentence: ")
                task, date, time = parse_task_from_text(sentence)
                print(f"\nParsed Task: {task}\nDate: {date or 'N/A'}\nTime: {time or 'N/A'}")
            else:
                task = input("Enter task description: ")
                date = input("Enter date (optional): ")
                time = input("Enter time (optional): ")

            add_task(task, date, time)
            print("✅ Task added!")

            
        elif choice == '2':
            show_tasks()

        elif choice == '3':
            task_id = input("Enter task ID to mark as done: ")
            complete_task(task_id)
            print("✅ Task marked as done!")

        elif choice == '4':
            print("👋 Exiting...")
            break
        
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
