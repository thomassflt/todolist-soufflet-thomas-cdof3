import os


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

    def check_save(self):
        if(os.path.isfile("save.txt")):
            print("A save has been found\n")
            with open('save.txt', 'r') as f:
                for ligne in f:
                    ligne=ligne.replace("\n","")
                    self.add_task(ligne)
        else:
            print("There is no save\n")

    def save_tasks(self):
        with open('save.txt', 'w') as f:
            for i, task in enumerate(self.tasks, 1):
                f.write(f"{task}\n")




if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.check_save()
    todo_list.view_tasks()
    while True:
        os.system('clear')
        print("Todo List:\n")
        todo_list.view_tasks()
        print("\n------------------------\n")
        print("Commands:\n")
        print("  a <task> - add a task")
        print("  d <task_number> - delete a task")
        print("  q - quit\n")

        user_input = input("Enter a command: ").split()
        command = user_input[0].lower()

        if command == "a":
            task = " ".join(user_input[1:])
            todo_list.add_task(task)
        elif command == "d":
            try:
                task_number = int(user_input[1])
                todo_list.delete_task(task_number)
            except ValueError:
                print("Task number must be an integer.")
        elif command == "q":
            todo_list.save_tasks()
            break
        else:
            print("Invalid command.")
