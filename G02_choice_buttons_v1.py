import tkinter as tk
from tkinter import *

class main:
    def __init__(self):
        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        for item in range(0, 4):
            self.choice_button = Button(self.main_frame, 
                                        width=15)

            self.choice_button.grid(row=item//2, column=item%2, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("God Quiz")
    main()
    root.mainloop()