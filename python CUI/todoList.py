class Task():
  def __init__(self,description,status):
    self.description = description
    self.status = status

class ToDoList():
  def __init__(self):
    self.tasks = []

  def add_task(self,description):
    task = Task(description,"Incomplete")
    self.tasks.append(task)
    print("task added")

  def view_tasks(self):
    if not self.tasks:
      print("No tasks found")
    else:
      for index, task in enumerate(self.tasks, start=1):
        print(f"{index}, {task.description}, [{task.status}]")

todo = ToDoList()

while True:
  print("\nMenu: add, view, exit")
  choice = input("enter your choice:")

  if choice == "add":
      desc = input("enter task description:")
      todo.add_task(desc)
  elif choice == "view":
      todo.view_tasks()
  elif choice == "exit":
    print("Goodbye!!")
    break
  else:
    print("Invalid choice. Please try again.")
  