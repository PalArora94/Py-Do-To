# Goal: Build Command-Line Task Manager
# We will build a command-line application to manage tasks, including following features:
#   - add tasks
#   - view all the tasks in the list
#   - mark tasks as complete
#   - delete tasks
#   - download the list as a CSV file
#
# Workflow:
#   1. A text file will store the tasks. For each task, there will be a unique ID, a title,
#      and a status, which will either be incomplete or complete.
#   2. To manage all the features of our app, we will use a dictionary.
#
# Run the script: python <name of the script>
# Install package: python -m pip install <package_name>

import os
import pandas as pd

# File to store tasks
FILE_NAME = "tasks.txt"


# Load tasks from file
def load_task():
    tasks = {}
    if os.path.exists(FILE_NAME):  # checking if the file exists in our directory; if it does:
        with open(FILE_NAME, 'r') as file:
            for line in file:    # each line in this file is a task
                task_id, title, status, deadline, priority = line.strip().split(" | ")  # using special character | to divide the three things
                tasks[int(task_id)] = {"title": title, "status": status, "deadline": deadline, "priority": priority}
                # this loads all existing tasks into dict. tasks

    return tasks

# For the first time when we run this function, there is no file `tasks.txt`,
# hence no tasks — it will return an empty dictionary.


# Save tasks to file
def save_tasks(tasks):  # passing our dictionary list here
    with open(FILE_NAME, 'w') as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} | {task['deadline']} | {task['priority']}\n")


# Add a new task
def add_task(tasks):  # passing our dictionary list here
    title = input("\nEnter the task title: ")
    deadline = input("\nEnter a Deadline for your task: ")
    priority = input("\nWhat is the priority of this task in your list 'High'/'Med'/'Low': ")
    task_id = max(tasks.keys(), default=0) + 1
    # keys=task_ids which are integers so whatever the last task id is (max) add 1 to get the next item in your list
    # default = 0 gets us the first item in the list

    # add this task to the dictionary tasks
    tasks[task_id] = {"title": title, "status": "Incomplete", "deadline": deadline, "priority": priority}
    print(f"\n\nTask: '{title}' with id: '{task_id}' added.")  # message for the user


# View all tasks
def view_tasks(tasks):
    if not tasks:  # if dict is empty
        print("\nNo tasks available.")
    else:
        print("\n To Do List: \nId -  Title - Status - Deadline - Priority ")
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']} - {task['deadline']} - {task['priority']}")


# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("\nEnter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "Complete"
        print(f"Task '{tasks[task_id]['title']}' completed! ")
    else:
        print("\nTask ID not found.")

# Note: user might not want to keep the task around in the list when the user has marked it as complete.
# The delete_task function below handles removal from the list.


# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"\nTask: '{deleted_task['title']}' deleted! ")
    else:
        print("\nTask ID not found.")

# Download the list as CSV
def download_csv(): 
    # read the file using pandas (with delimiter)
    if os.path.exists(FILE_NAME):   # checking if text file is there in our folder
        cols = ['ID', 'Task', 'Status', 'Deadline', 'Priority']  # this will give structure to our list as a CSV file
        df = pd.read_csv(FILE_NAME, sep = '|', names=cols, index_col="ID", header=None) 
        # if we don't assign a col. to use for index, and no header (names), pd assigns first row as header and
        # index the rest of the rows which messes up the structure of dataframe
        
        print(df)
    else:
        print("\nNo To-Do List found!")
        
    # convert it to csv
    df.to_csv("mycsv.csv", index=False)
    


# Main Menu to display all options to user
def main():
    tasks = load_task()  # want to get all tasks as soon as program runs
    while True:  # keeps on running until user specifically exits
        print("\nTask Manager Menu\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete a Task")
        print("5. Download your list as a CSV file")
        print("6. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            download_csv()
        elif choice == "6":
            save_tasks(tasks)
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again!")


# In Python, if we want to run the main function as soon as the application starts, we do this:
if __name__ == "__main__":
    main()
