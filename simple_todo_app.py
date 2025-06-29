from ttkbootstrap import Window, ttk
from tkinter import StringVar, END

# Create the main application window
app = Window(themename="superhero")
app.title("ToDo List Application")
app.geometry("800x600")

# task input field
task_input_var = StringVar()

task_input = ttk.Entry(app, textvariable=task_input_var, font=("Arial", 14))
task_input.pack(pady=20)

# task listbox
task_listbox = ttk.Treeview(
    app,
    columns=("Task"),
    show="headings",
    height=15,
    selectmode="browse"
)

task_listbox.heading("Task", text="Task")
task_listbox.pack(pady=10, padx=20, fill="both", expand=True)

# Function to add a task
def add_task():
    task = task_input_var.get().strip()
    if task:
        task_listbox.insert("", "end", values=(task,))
        task_input_var.set("")
        
# Function to delete a selected task
def delete_task():
    selected_item = task_listbox.selection()
    if selected_item:
        task_listbox.delete(selected_item)

# Buttons frame
buttons_frame = ttk.Frame(app)
buttons_frame.pack(pady=20)
# Add Task button
add_task_button = ttk.Button(buttons_frame, text="Add Task", command=add_task)
add_task_button.pack(side="left", padx=5)
# Delete Task button
delete_task_button = ttk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side="left", padx=5)


app.mainloop()