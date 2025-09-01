import os
import time
tasks = []
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
def show_tasks():
        if tasks == []:
            print("you haven`t added any tasks yet")
        for y in tasks:
            print(y)
def delete_task():
    task = input("Enter the task you want to delete: ")
    for i in tasks:
        if i == task:
            tasks.remove(i)

while True:
    os.system("cls")
    print("""
Welcome to the today`s to-do list app

choose an option:
1.add a task
2.show the tasks
3.delete a task
4.exit
""")
    action = int(input("Enter your choice: "))
    if action == 1:
        add_task()
        print(" The task added successfully..\n")
        input("Enter any key to return to the main menu...")
    elif action == 2:
        show_tasks()
        input("\nEnter any key to return to the main menu...")
    elif action == 3:
        delete_task()
        print("The task deleted successfully..\n")
        input("Enter any key to return to the main menu...")
    elif action == 4:
        break
    else :
        print("invalid chlice...")
        time.sleep(2) 