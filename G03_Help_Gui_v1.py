# imports
import tkinter as tk
from tkinter import *
from functools import partial # prevents unwanted windows


class main:
    def __init__(self):
        
        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        self.help_button = Button(self.main_frame, text="Help", width=10, command=self.to_help)
        self.help_button.grid(row=0, column=1, padx=10)

    def to_help(self):
        DisplayHelp(self)

class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"

        # setup dialogue box
        self.help_box = Toplevel()
        self.help_box.title("Don't Extend Window")
        self.help_box.geometry("310x240")

        # diasble help button
        partner.help_button.config(state=DISABLED)

        # if user closes the help frame 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text="Help / Info", font=("Arial", "30", "bold"), bg=background)
        self.help_heading.grid(row=0, column=0)

        helpinfo = "Enter Number of Questions Then Press Enter. A question will appear. When you select a god the game will tell you whether you've won or not. Then press 'Next' to move on"

        self.help_info = Label(self.help_frame, text=helpinfo, font=("Arial", "12"), bg=background, wrap=300, justify=CENTER)
        self.help_info.grid(row=1, padx=10, pady=10, column=0)

        self.return_button = Button(self.help_frame, text="Return", font=("Arial", "15", "bold"), bg="#a30000", fg="white", width=10, command=partial(self.close_help, partner))
        self.return_button.grid(row=2, pady=10, column=0)

        self.idk = Label(self.help_frame, text="""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⣠⣶⣶⣄⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⣀⣶⣿⣿⣿⣿⣿⣆⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⢀⣤⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⢀⣠⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠉⠉⠙⠛⠛⠻⢿⣿⡿⠟⠁⠀⣀⣴⣿⣿⣿⣿⣿⠟
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⣉⣡⠀⣠⣴⣶⣶⣦⠄⣀⡀⠀⠀ ⠀⣠⣾⣿⣿⣿⣿⣿⡿⢃⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣾⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣠⣾⡟⢡⣾⣿⣿⣿⡿⢋⣴⣿⡿⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⢡⣾⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿⡟⣰⣿⣿⣿⣿⠏⣰⣿⣿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢚⣛⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠸⣿⠟⢰⣿⣿⣿⣿⠃⣾⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠻⠻⠃⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢉⣴⣿⣿⣿⣿⡇⠘⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⠁⢀⣀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠟⠉⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌
⣿⣿⣿⣿⣿⣿⡿⠁⣀⣤⡀⠀⠈⠻⢿⠀⣼⣿⣷⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀ ⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⠛⠙⠃⠀⣿⣿⣿⠀⠀ ⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠁⢀⣴⣶⣶⣾⣿⣿⣿⣿⣶⡐⢦⣄⠀⠀⠈⠛⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢀⣼⡿⢛⣩⣴⣶⣶⣶⣶⣶⣶⣭⣙⠻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿
⠁⠀⣴⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣦⡙⠻⣶⣄⡀⠀⠈⠙⢿⣿⣷⣦⣤⣤⣴⣿⡏⣠⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⣿⠋⣠⠔⠀⠀⠻⣿⣿⣿⣿⢉⡳⢦⣉⠛⢷⣤⣀⠀⠈⠙⠿⣿⣿⣿⣿⢸⣿⡄⠻⣿⣿⠟⡈⣿⣿⣿⣿⣿⢉⣿⣧⢹⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⡇⠠⡇⠀⠀⠀⠀⣿⣿⣿⣿⢸⣿⣷⣤⣙⠢⢌⡛⠷⣤⣄⠀⠈⠙⠿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣤⣙⣛⣛⣥⣾⣿⣿⡌⣿⣿⣿⣷⣤⣀⣀⣀⣠⣴⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⣷⡀⠡⠀⠀⠀⣰⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣦⣌⡓⠤⣙⣿⣦⡄⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⣿⣿⣶⣤⣴⣾⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣷⠀⣶⡄⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⣿⣿⣿⠟⠻⣿⣿⡏⣉⣭⣭⡘⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡇⢸⡇⢠⡀⠈⠙⠋⠉⠉⠉⠉⠛⠫⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⠛⣿⣿⣀⣀⣾⡿⢀⣿⣿⣿⢻⣷⣦⢈⡙⠻⢿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡇⢸⡇⢸⣿⠀⣦⠀⠀⠶⣶⣦⣀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢸⣿⣿⣦⣈⡛⠿⠟⣋⣤⣾⣿⣿⣿⣸⣿⣿⢸⡇⢰⡆⢈⡙⠻⢿⣿⣿⣿⠀⢿⡇⢸⡇⢸⣿⢠⣿⡇⣿⡆⢈⡙⠻⠧⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣝⠛⢿⣿⣿⣿⣿⣿⣿⠟⣁⠀⠀⢈⠛⠿⢸⣇⢸⡇⢸⡇⣶⣦⣌⡙⠻⢄⡀⠁⠘⠇⠘⣿⢸⣿⡇⣿⡇⢸⡛⠷⣦⣄⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡆⠀⠈⠳⢶⣤⣍⡉⠉⣩⣤⣤⡉⠻⢶⣤⣀⠂⠀⠉⠘⠇⢸⡇⣿⣿⣿⣿⣷⣦⣍⡑⠢⣄⠀⠈⠈⠻⠇⣿⡇⢸⣿⣷⣾⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣦⣄⡀⠈⠉⠛⠶⢄⡉⠻⠿⣷⣦⣌⡙⠷⢶⣄⡀⠀⠈⠁⠙⢿⣿⣿⣿⣿⣿⣿⣷⣦⣍⡒⠤⣀⠀⠈⠃⢸⣿⣿⣿⣿⣷⠀⢸⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠈⠉⠂⠄⢙⣿⣿⣷⣦⣈⠙⠳⢦⣄⡀⠠⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣌⡐⠄⢸⣿⣿⣿⣿⣿⡇⠀⣿⠿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⡿⢰⣦⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣄⡀⠀⠀⠀⠉⠛⠛⠛⠿⠷⣤⣈⠛⠷⢤⣈⡂⢄⡉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣌⡛⠿⣿⣿⡇⠀⢿⣷⣌⡛⠿⠿⠏⣼⣷⣤⣉⣉⣀⣼⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⢀⣤⣶⣦⣤⣤⣄⡈⠙⠻⠖⠀⣉⣩⣤⣤⣤⣤⣤⣤⣀⡈⠉⠙⠻⣿⣿⣿⣿⣶⡄⠉⠀⠀⣸⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⣴⣿⣿⣿⣿⣿⠟⣩⣽⣿⣿⣿⣷⣦⣀⠀⠙⢻⣿⣿⠇⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠏⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠉⠻⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⣿⣿⡿⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣦⡀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢀⣙⣟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣘⣛⣻⣦⢀⣀⣙⣛⣛⣛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""", font=("Arial", "3"), bg=background)
        self.idk.grid(row=3, padx=10, pady=10)

        # closes help dialogue
    def close_help(self, partner):
            # set help button back to normal
            partner.help_button.config(state=NORMAL)
            self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("God Quiz")
    main()
    root.mainloop()