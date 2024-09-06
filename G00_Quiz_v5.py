import tkinter as tk
from tkinter import ttk  # for combobox
from tkinter import *
from functools import partial  # prevents unwanted windows
import csv
import random

# font for all buttons: Arial size 20 bold, with white text
button_font = ("Arial", "16", "bold")
button_fg = "#FFFFFF"


# game finished

class main:
    def __init__(self):

        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid()

        self.main_heading = Label(self.main_frame, text="Gods Of Myth", font=("Arial", "30", "bold"))
        self.main_heading.grid(row=0)

        self.main_instructions = Label(self.main_frame,
                                       text="Enter number of question in the \nbox below then press play",
                                       font=("Arial", "12"), justify="center")
        self.main_instructions.grid(row=1, pady=10)

        self.entry_frame = Frame(self.main_frame)
        self.entry_frame.grid(row=2, padx=10, pady=10)

        self.main_entry = Entry(self.entry_frame, font=("Arial", "12"), width=18)
        self.main_entry.grid(row=0, column=0, ipady=6, padx=10)

        self.current_diff = StringVar()  # create variable for combobox
        self.dropbox = ttk.Combobox(self.entry_frame, textvariable=self.current_diff, values=("Normal", "Hard"),
                                    state="readonly", font=("Arial", "18"), width=6)
        self.dropbox.current(0)  # sets default value on dropbox to first item in list
        self.dropbox.grid(row=0, column=1)

        self.error_label = Label(self.main_frame, text="")
        self.error_label.grid(row=3, padx=5, pady=1)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=5, padx=10, pady=10)

        self.help_button = Button(self.button_frame, text="Help", font=button_font, bg="#F23390", fg=button_fg,
                                  activebackground="#b40b5e", activeforeground="#ffffff", width=6,
                                  command=self.to_help)
        self.help_button.grid(row=0, column=0, padx=5)

        self.play_button = Button(self.button_frame, text="Play", font=button_font, fg=button_fg, bg="#c721fd",
                                  activebackground="#8b17b1", activeforeground="#ffffff", width=6,
                                  command=lambda: self.num_question())
        self.play_button.grid(row=0, column=1, padx=5)

        self.stats_button = Button(self.button_frame, text="Stats", font=button_font, bg="#14eceb", fg=button_fg,
                                   activebackground="#006464", activeforeground="#ffffff", width=6, state=DISABLED)
        self.stats_button.grid(row=0, column=2, padx=5)

    # checks user input is bigger than 0
    def num_question(self):
        difficulty = ""  # resets difficulty for new game

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
            self.error_label.config(text=error, fg="#9C0000")  # red text
            self.main_entry.config(bg="#F8CECC")  # pink entry box

        else:
            difficulty = self.current_diff.get()  # get new difficulty from combobox
            self.error_label.config(text="", fg="#000000")  # black text
            self.main_entry.config(bg="#FFFFFF")  # white entry box
            self.to_play(response, difficulty)

        self.main_entry.delete(0, END)  # clears entry widget

    @staticmethod
    def to_play(how_many, difficulty):
        Play(how_many, difficulty)
        root.withdraw()  # hide root window

    def to_help(self):
        DisplayHelp(self)


class Play:
    def __init__(self, how_many, difficulty):
        self.play_box = Toplevel()

        self.all_gods = self.get_all_gods()

        # variables for stats when game ends
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_correct = IntVar()
        self.rounds_correct.set(0)

        self.rounds_wrong = IntVar()
        self.rounds_wrong.set(0)

        # if users press cross at top, closes game
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))

        self.quiz_frame = Frame(self.play_box, padx=10, pady=10)
        self.quiz_frame.grid()

        rounds_heading = f"Question 1 of {how_many}"
        self.game_heading = Label(self.quiz_frame,
                                  text=rounds_heading, font=("Arial", "16", "bold"), wraplength=300)
        self.game_heading.grid(row=0)

        self.question_label = Label(self.quiz_frame, text="", height=3, wraplength=300)
        self.question_label.grid(row=1)

        self.choice_frame = Frame(self.quiz_frame)  # frame for choice buttons
        self.choice_frame.grid(row=2, pady=5)

        self.choice_button_ref = []  # list used to refer to the buttons when editing config
        self.button_gods_list = []

        # create buttons to choose
        for item in range(0, 4):
            self.choice_button = Button(self.choice_frame,
                                        width=18, disabledforeground="#000000", height=2, wraplength=125)

            self.choice_button.grid(row=item // 2, column=item % 2, padx=10, pady=5)

            self.choice_button_ref.append(self.choice_button)

        self.stats_next_frame = Frame(self.quiz_frame, bg="#ffe291")
        self.stats_next_frame.grid(row=3)

        self.stats_correct = Label(self.stats_next_frame, text="Correct: 0", bg="#ffe291")
        self.stats_correct.grid(row=0, column=0, padx=16)

        self.stats_wrong = Label(self.stats_next_frame, text="Wrong: 0", bg="#ffe291")
        self.stats_wrong.grid(row=0, column=1, padx=16)

        self.next_button = Button(self.stats_next_frame, text="Next", font=button_font, bg="#00bfff",
                                  fg=button_fg,
                                  activebackground="#0086b3", activeforeground="#ffffff",
                                  width=8, state=DISABLED, command=lambda: self.new_round(difficulty))
        self.next_button.grid(row=0, column=2)

        self.score_frame = Frame(self.quiz_frame, bg="#ffe291")
        self.score_frame.grid(row=4, pady=10)

        self.stats_score = Label(self.score_frame, text=f"Score: 0%", bg="#ffe291")
        self.stats_score.grid(row=0, column=0, padx=37, pady=10)

        self.high_score = Label(self.score_frame, text=f"High Score: 0%", bg="#ffe291")
        self.high_score.grid(row=0, column=1, padx=37, pady=10)

        self.new_round(difficulty)

    # gets gods from csv file
    def get_all_gods(self):
        file = open("gods.csv", "r")
        var_all_gods = list(csv.reader(file, delimiter=","))
        file.close()

        var_all_gods.pop(0)  # remove the first row (header values)
        return var_all_gods

    # get 4 gods for each round
    def get_round_gods(self):

        round_gods_list = []
        god_name_list = []

        # get 4 unique gods
        while len(round_gods_list) < 4:
            # choose item
            random_god = random.choice(self.all_gods)

            # check god is not already in list
            if random_god[1] not in god_name_list:
                # add item to rounds list
                round_gods_list.append(random_god)
                god_name_list.append(random_god[1])

        return round_gods_list

    def new_round(self, difficulty):
        self.next_button.config(state=DISABLED)

        current_round = self.rounds_played.get()
        current_round += 1
        self.rounds_played.set(current_round)

        new_heading = f"Question {current_round} of {self.rounds_wanted.get()}"
        self.game_heading.config(text=new_heading)

        self.button_gods_list.clear()
        self.button_gods_list = self.get_round_gods()

        # Randomly choose the index of the correct answer button
        correct_index = random.randint(0, len(self.choice_button_ref) - 1)

        # Set button text and command
        for i in range(len(self.choice_button_ref)):
            # Set the text of the button to god's name and reset bg colour
            self.choice_button_ref[i]["bg"] = "#FFFFFF"
            self.choice_button_ref[i]["text"] = self.button_gods_list[i][1]
            self.choice_button_ref[i]["state"] = NORMAL

            # checks if answer is correct and enable next button
            self.choice_button_ref[i].config(command=lambda i=i: self.check_answer(i, correct_index, current_round))

            # Determine if this button is the correct answer
            if i == correct_index:
                if difficulty == "Normal":
                    self.question_label.config(
                        text=f"Who is the {self.button_gods_list[i][0]} {self.button_gods_list[i][2]}")
                else:
                    self.question_label.config(text=f"Who is the {self.button_gods_list[i][2]}")

    def check_answer(self, clicked_index, correct_index, current_round):

        if clicked_index == correct_index:
            # Handle correct answer logic here
            self.choice_button_ref[clicked_index]["bg"] = "#2ebb01"
            num_correct = self.rounds_correct.get()
            num_correct += 1
            self.rounds_correct.set(num_correct)
            self.stats_correct.config(text=f"Correct: {self.rounds_correct.get()}")

            score = num_correct / self.rounds_wanted.get() * 100
            self.stats_score.config(text=f"Score: {score:.1f}%")
        else:
            # Handle wrong answer logic here
            self.choice_button_ref[clicked_index]["bg"] = "#CF3C49"
            num_wrong = self.rounds_wrong.get()
            num_wrong += 1
            self.rounds_wrong.set(num_wrong)
            self.stats_wrong.config(text=f"Wrong: {self.rounds_wrong.get()}")

        for i in range(len(self.choice_button_ref)):
            self.choice_button_ref[i]["state"] = DISABLED

        if current_round == self.rounds_wanted.get():
            self.next_button.config(state=NORMAL, text="Return")
            self.next_button.config(command=lambda: self.close_play())
        else:
            self.next_button.config(state=NORMAL)

    def close_play(self):
        # reshow root and end current game
        root.deiconify()
        self.play_box.destroy()


class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"

        # setup dialogue box
        self.help_box = Toplevel()
        self.help_box.title("Help")
        self.help_box.geometry("314x300")

        # disable help button
        partner.help_button.config(state=DISABLED)

        # if user closes the help frame 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text="Help / Info", font=("Arial", "30", "bold"), bg=background)
        self.help_heading.grid(row=0, column=0)

        helpinfo = "Enter Number of Questions Then Press Enter. A question will appear. When you select a god the " \
                   "game will tell you whether you're correct or not. Then press 'Next' to move on\n\nNormal " \
                   "Difficulty: Default\nHard Difficulty: removes pantheon hint in question"

        self.help_info = Label(self.help_frame, text=helpinfo, font=("Arial", "12"), bg=background, justify=LEFT,
                               wraplength=300)
        self.help_info.grid(row=1, padx=10, pady=10, column=0)

        self.return_button = Button(self.help_frame, text="Return", font=("Arial", "15", "bold"), bg="#a30000",
                                    fg="white", width=10, command=partial(self.close_help, partner))
        self.return_button.grid(row=2, pady=10, column=0)
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
