import tkinter as tk
from tkinter import *


# Creating object of tk class
root = tk.Tk()

# Setting up the Box 
root.geometry("480x480")
root.resizable(False, False)
root.iconbitmap('university_icon.ico')
root.title("University Finder")
root.config(background="green")

photo = PhotoImage(file=r'Green_button.png')  # Setting up Image for Button


def widgets():
    """
    This function displays find me a university text and find button.
    """
    head_label = Label(root,
                       text="FIND ME A UNIVERSITY!",
                       padx=15,
                       pady=15,
                       font="Rockwell 20",
                       bg="green",
                       fg="white")
    head_label.config(anchor=CENTER)
    head_label.pack()

    button = Button(root,
                    text="Click Me!",
                    image=photo,
                    command=navigate)
    button.config(anchor=CENTER)
    button.pack()


def navigate():
    """
    This function import from main.py.
    """
    import main


widgets()  # Calling Widgets into Action
root.mainloop()  # Infinite Loop for the interface
