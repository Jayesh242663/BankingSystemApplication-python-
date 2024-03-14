import tkinter as tk
from tkinter import font as tkfont

class Options(tk.Tk):
    def __init__(self, accno):
        super().__init__()
        self.accno = accno

        self.geometry("800x600")
        self.title("MAIN MENU")
        self.configure(bg="white")



        self.image6 = tk.PhotoImage(file="./Images/Bankimg2.png")
        self.banklabel_6 = tk.Label(self, image=self.image6)
        self.banklabel_6.place(x=0, y=0)

        self.font = tkfont.Font(family="Tahoma", size=25)
        self.title_label = tk.Label(self, text="MAIN MENU", font=tkfont.Font(family="Tahoma", size=30, weight="bold"), fg="dark gray", bg="white")
        self.title_label.place(x=280, y=20, width=250, height=50)

        self.deposit_button = tk.Button(self, text="DEPOSIT", font=self.font, fg="light gray", bg="white", bd=0, command=self.open_deposit)
        self.deposit_button.place(x=50, y=200, width=150, height=60)

        self.withdraw_button = tk.Button(self, text="WITHDRAW", font=self.font, fg="light gray", bg="white", bd=0, command=self.open_withdraw)
        self.withdraw_button.place(x=600, y=200, width=180, height=60)

        self.balance_button = tk.Button(self, text="DISPLAY BALANCE", font=self.font, fg="light gray", bg="white", bd=0, command=self.open_check_balance)
        self.balance_button.place(x=250, y=200, width=300, height=60)

        self.exit_button = tk.Button(self, text="LOGOUT", font=self.font, fg="#D2042D", bg="white", bd=0, command=self.logout)
        self.exit_button.place(x=320, y=370, width=160, height=60)


    def open_deposit(self):
        self.destroy()
        import deposit
        deposit.Deposit(self.accno)

    def open_withdraw(self):
        self.destroy()
        import withdraw
        withdraw.Withdraw(self.accno)

    def open_check_balance(self):
        self.destroy()

    def logout(self):
        self.destroy()


if __name__ == "__main__":
    options = Options(accno="accno")
    options.mainloop()
