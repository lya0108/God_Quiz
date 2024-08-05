from tkinter import ttk  # for combobox
import tkinter


class test:
    def __init__(self):
        self.frame = tkinter.Frame()
        self.frame.grid()

        self.current_diff = tkinter.StringVar()  # create variable for combobox
        self.dropbox = ttk.Combobox(self.frame, textvariable=self.current_diff, values=("Normal", "Hard"),
                                    state="readonly", font=("Arial", "18"), width=6)
        self.dropbox.grid()


# main routine
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("God Quiz")
    test()
    root.mainloop()
