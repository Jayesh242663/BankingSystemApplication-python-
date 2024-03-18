import tkinter as tk
from tkinter import Button, scrolledtext
import mysql.connector

class Check_balance(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Check Balance")
        self.geometry("800x600")
        self.create_widgets()
    def create_widgets(self):
        self.image10 = tk.PhotoImage(file="./Images/Bankimg2.png")
        self.bank_label_10 = tk.Label(self, image=self.image10, )
        self.bank_label_10.place(x=0, y=0)

        self.sp1 = scrolledtext.ScrolledText(self, width=50, height=3, wrap=tk.WORD, font=("Tahoma", 14))
        self.sp1.place(x=150, y=200)



if __name__ == "__main__":
    app = Check_balance()
    app.mainloop()
