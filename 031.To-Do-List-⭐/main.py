# To-Do List

tasks = []
running = True

while running:
    user_tasks = input("Enter the tasks that you have to do (enter e to exit): ")
    if user_tasks.isdigit():
        print("Error! Numbers are not allowed.")
    else:
        tasks.append(user_tasks)
        print("Task added successfully!")

    if user_tasks == "e" or user_tasks == "E":
        running = False

tasks.pop()
print(tasks)

while True:
    delete = input("Do you wanna delete any task? (y/n): ")

    if delete.lower() == "y":
        index = int(input("Enter the number of the task that you wanna delete: "))
        index -= 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted successfully!")
            print(tasks)

            if len(tasks) == 0:
                print("There are no more tasks!")
                break
        else:
            print("Invalid task number!")

    elif delete.lower() == "n":
        print("Good job doing your tasks :)")
        break

    else:
        print("Invalid input!")