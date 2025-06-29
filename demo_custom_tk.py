import customtkinter as ctk

app = ctk.CTk()
app.title("My App")
app.geometry("700x400")

btn = ctk.CTkButton(app, text="Click Me")
btn.pack()


app.mainloop()