import json
from ttkbootstrap import Window, ttk
from tkinter import StringVar, END
import os

# Constants
DATA_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks():
    tasks = []
    for child in task_listbox.get_children():
        values = task_listbox.item(child, "values")
        tasks.append({"task": values[0], "done": values[1]})
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

# Create main window
app = Window(themename="superhero")
app.geometry("800x650")
# Add a custom icon if available
if os.path.exists("icon.ico"):
    app.iconbitmap("icon.ico")
# Title label
head_frame = ttk.LabelFrame(app, bootstyle="info")
head_frame.pack(padx=10, fill="both", expand=True)
title_label = ttk.Label(head_frame, text="To-Do List", font=("Arial", 24))
title_label.pack(pady=5)


# Input field
task_var = StringVar()

entry = ttk.Entry(app, textvariable=task_var, font=("Arial", 14))
entry.pack(pady=10, padx=10)

# Task list display (with Done column)
task_listbox = ttk.Treeview(
    app,
    columns=("Task", "Done"),
    show="headings",
    height=15
)
task_listbox.heading("Task", text="Task")
task_listbox.heading("Done", text="Done")
task_listbox.pack(pady=10, padx=10, fill="both", expand=True)

# Add task
def add_task():
    task = task_var.get().strip()
    if task:
        task_listbox.insert("", END, values=(task, "No"))
        task_var.set("")
        save_tasks()

# Delete selected task
def delete_task():
    selected = task_listbox.selection()
    for item in selected:
        task_listbox.delete(item)
    save_tasks()

# Mark selected as done
def mark_done():
    selected = task_listbox.selection()
    for item in selected:
        values = list(task_listbox.item(item, "values"))
        values[1] = "Yes"
        task_listbox.item(item, values=values, tags=("done",))
    save_tasks()

# Apply coloring
task_listbox.tag_configure("done", background="#d4edda")

# Load saved tasks
for task in load_tasks():
    tags = ("done",) if task["done"] == "Yes" else ()
    task_listbox.insert("", END, values=(task["task"], task["done"]), tags=tags)

# Buttons frame
buttons_frame = ttk.Labelframe(app, bootstyle="warning", text="Actions")
buttons_frame.pack(pady=10, padx=5)

add_btn = ttk.Button(buttons_frame, text="Add Task", command=add_task, bootstyle="success-outline")
add_btn.pack(side="left", padx=5, pady=10)

delete_btn = ttk.Button(buttons_frame, text="Delete Selected", command=delete_task, bootstyle="danger-outline")
delete_btn.pack(side="left", padx=5, pady=10)

done_btn = ttk.Button(buttons_frame, text="Mark as Done", command=mark_done, bootstyle="info")
done_btn.pack(side="left", padx=5, pady=10)

app.mainloop()
