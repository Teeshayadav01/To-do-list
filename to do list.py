import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        #Initialize tasks list
        self.tasks = []

        #task input field
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        #add task button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        #listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        #complete task button
        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        #delete task button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Initialize listbox with existing tasks
        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.itemconfig(selected_task_index, {'bg': 'light green'})
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete!")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.refresh_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
    
