# imports
import tkinter as tk
from tkinter import *

class main:
    def __init__(self):
        
        # font for all buttons: Arial size 20 bold, with white text
        button_font = ("Arial", "16", "bold")
        button_fg = "#FFFFFF"

        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        self.main_heading = Label(self.main_frame, text="Gods Of Myth", font=("Arial", "30", "bold"))
        self.main_heading.grid(row=0)

        self.main_instructions = Label(self.main_frame, text="Enter number of question in the \nbox below then press play", font=("Arial", "12"), wrap=300, justify="center")
        self.main_instructions.grid(row=1, pady=10)

#        self.output_label = Label(self.main_frame, text="")
#        self.output_label.grid(row=2, padx=5, pady=5)
        
        self.entry_frame = Frame(self.main_frame)
        self.entry_frame.grid(row=3, padx=10, pady=10)

        self.main_entry = Entry(self.entry_frame, font=("Arial", "16"), width=15)
        self.main_entry.grid(row=0, column=0, ipady=6)

        self.play_button = Button(self.entry_frame, text="Play", font=button_font, fg=button_fg, bg="#13ab45", activebackground="#0b6629", activeforeground="#ffffff", width=5)
        self.play_button.grid(row=0, column=1)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=5, padx=10, pady=10)

        self.stats_button = Button(self.button_frame, text="Stats", font=button_font, bg="#00b0b0", fg=button_fg, activebackground="#006464", activeforeground="#ffffff", width=10,state=DISABLED)
        self.stats_button.grid(row=0, column=0, padx=10)

        self.instructions_button = Button(self.button_frame, text="Instructions", font=button_font, bg="#d98a00", fg=button_fg, activebackground="#8d5900", activeforeground="#ffffff", width=10)
        self.instructions_button.grid(row=0, column=1, padx=10)

# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Womp Womp")
    main()
    root.mainloop()