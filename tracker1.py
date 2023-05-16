# Imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tracker2

# Submit function that closes page 1
def submit():
    name_value = name.get()
    root.withdraw()  # Hide the first window
    tracker2.open_tracker2(name_value)  # Run function imported from tracker2.py


# GUI Code
root = Tk()
root.title("Homework Tracker App")
root.configure(bg="#5D737E")  # Set the background color

# Configure rows and columns to be expandable
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create the frame displaying basic information
intro_frame = LabelFrame(root)
intro_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create the frame displaying informations
instruction_frame = LabelFrame(root)
instruction_frame.grid(row=1, padx=10, pady=10, sticky="NSEW")

# Create bottom frame for logging in
login_frame = LabelFrame(root, text="Login Details")
login_frame.grid(row=2, padx=10, pady=10, sticky="NSEW")

# Configure column and row resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
intro_frame.columnconfigure(1, weight=1)
instruction_frame.columnconfigure(1, weight=1)
login_frame.columnconfigure(1, weight=1)

# Create PhotoImage and subsample method to reduce size
logo_image = PhotoImage(file="logo.png")
smaller_image = logo_image.subsample(5, 5)

# Hold image label
logo_label = Label(intro_frame, image=smaller_image)
logo_label.grid(row=0, column=0, padx=8, pady=8)

# Create and set the Title message text variable
title_label = Label(intro_frame, text="Homework Tracker", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=1, padx=5)

# Create and set the short description text variable
description_label = Label(
    intro_frame,
    # List of the instructions
    text="This homework tracker appc created using Tkinter"
    " will allow you to easily record and keep track of your"
    " assignments or homework online",
    wraplength=350,
    justify="left",
)
description_label.grid(row=1, columnspan=2, padx=8, pady=8, sticky="W")

# Create the PhotoImage and label to hold it
todo_image = PhotoImage(file="todo.png")
todos_image = todo_image.subsample(7, 6)
image_label = Label(instruction_frame, image=todos_image)
image_label.grid(row=0, column=0, padx=8, pady=5)

# Create variable and initialise with starting text
# Create instruction list
instructions_text = "\nHow to use:\n\n"
instructions = [
    "Enter your name, email address and password to login ",
    "You will be able to view the work you have added before ",
    "You can add a new task and select a due date for it, and it will be added to the list ",
    "You could also delete the work you finished ",
]

# Enumerate to provide index starting from 1
for index, instruction in enumerate(instructions, start=1):
    instructions_text += f"{index}. {instruction}\n"

# Create label and allign it to left
instructions_label = Label(
    instruction_frame, text=instructions_text, justify=LEFT, wraplength=200
)
instructions_label.grid(row=0, column=1, padx=5)

# Create a label for the amount field and pack it into the GUI
name_label = Label(login_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=15)

# Create a variable to store the name and display later
name = StringVar()
name.set("")

# Create an entry to type in name
name_entry = Entry(login_frame, textvariable=name)
name_entry.grid(row=0, column=1, padx=30)

# Create a label for the amount field and pack it into the GUI
mail_label = Label(login_frame, text="Email:")
mail_label.grid(row=1, column=0, padx=10, pady=15)

# Create a variable to store the mail
mail = StringVar()
mail.set("")

# Create an entry to type in mail
mail_entry = Entry(login_frame, textvariable=mail)
mail_entry.grid(row=1, column=1, padx=30)

# Create a label for the password and pack it into the GUI
password_label = Label(login_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=15)

# Create a variable to store the password
password = StringVar()
password.set("")

# Create an entry to type in password
password_entry = Entry(login_frame, textvariable=password)
password_entry.grid(row=2, column=1, padx=30)

# Create a submit button
submit_button = Button(login_frame, text="Submit", relief="raise", command=submit)
submit_button.grid(row=3, column=1, padx=39, pady=10, sticky="E")

# Run the mainloop
root.mainloop()
