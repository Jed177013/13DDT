# Imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# When the submit button is clicked, this function will run to open a new window
# All the codes for tracker2.py will be written in this function
def open_tracker2(name_value):
    # GUI Code
    root = Tk()
    root.title("Task Management")
    root.configure(bg="#5D737E")  # Set the background color

    # Configure rows and columns to be expandable
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create the frame displaying basic information
    intro_frame = LabelFrame(root, text = "Assignments and Tasks")
    intro_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    # Create label to display the welcome message
    # capitalize() syntax to capitalise the first letter of name the for user input
    welcome_label = Label(root, text=f"Welcome, {name_value.capitalize()}!" ,font=("Arial", 20, "bold"))
    welcome_label.grid(row = 0, padx = 5, pady = 5)


    test_label = Label(intro_frame, text = "Test")
    test_label.grid()

    # Create an add button
    add_button = Button(intro_frame, text="Add", relief="ridge")
    add_button.grid(row=3, sticky="E")





    # Run the mainloop
    root.mainloop()