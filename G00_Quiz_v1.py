# imports
import tkinter as tk
from tkinter import *
from functools import partial  # prevents unwanted windows
import csv
import random

# font for all buttons: Arial size 20 bold, with white text
button_font = ("Arial", "16", "bold")
button_fg = "#FFFFFF"


# main class only


class main:
    def __init__(self):

        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        self.main_heading = Label(self.main_frame, text="Gods Of Myth", font=("Arial", "30", "bold"))
        self.main_heading.grid(row=0)

        self.main_instructions = Label(self.main_frame,
                                       text="Enter number of question in the \nbox below then press play",
                                       font=("Arial", "12"), wrap=300, justify="center")
        self.main_instructions.grid(row=1, pady=10)

        self.entry_frame = Frame(self.main_frame)
        self.entry_frame.grid(row=2, padx=10, pady=10)

        self.main_entry = Entry(self.entry_frame, font=("Arial", "16"), width=15)
        self.main_entry.grid(row=0, column=0, ipady=6)

        self.play_button = Button(self.entry_frame, text="Play", font=button_font, fg=button_fg, bg="#c721fd",
                                  activebackground="#8b17b1", activeforeground="#ffffff", width=5,
                                  command=lambda: self.num_question())
        self.play_button.grid(row=0, column=1)

        self.error_label = Label(self.main_frame, text="")
        self.error_label.grid(row=3, padx=5, pady=5)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=5, padx=10, pady=10)

        self.stats_button = Button(self.button_frame, text="Stats", font=button_font, bg="#14eceb", fg=button_fg,
                                   activebackground="#006464", activeforeground="#ffffff", width=10, state=DISABLED)
        self.stats_button.grid(row=0, column=0, padx=10)

        self.help_button = Button(self.button_frame, text="Help", font=button_font, bg="#F23390", fg=button_fg,
                                  activebackground="#b40b5e", activeforeground="#ffffff", width=10)
        self.help_button.grid(row=0, column=1, padx=10)

    # checks user input is bigger than 0
    def num_question(self):

        has_error = "no"
        error = "Please Enter a Number That is More Than 0"

        response = self.main_entry.get()

        try:
            response = int(response)

            if response <= 0:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            # red text, pink entry box
            self.error_label.config(text=error, fg="#9C0000")
            self.main_entry.config(bg="#F8CECC")

        else:
            # black text, white entry box
            self.error_label.config(text="", fg="#000000")
            self.main_entry.config(bg="#FFFFFF")

        # clears entry widget
        self.main_entry.delete(0, END)

# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("God Quiz")
    main()
    root.mainloop()
