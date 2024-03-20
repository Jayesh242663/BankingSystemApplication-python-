# import tkinter as tk
# from tkinter import font as tkfont
# from Buttons import HoverButton
import tkinter

import customtkinter
from customtkinter import *
colors =["#070F2B","#1B1A55","#535C91"]

class Options(customtkinter.CTk):
    def __init__(self, accno):
        super().__init__()
        self.accno = accno

        self.geometry("600x600")
        self.title("MAIN MENU")
        self.config(bg=colors[0])

        self.frame = CTkFrame(master=self, width=550, height=550, fg_color=colors[1], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.title_label = CTkLabel(master=self.frame, width=220, text="MAIN MENU",font=('Century Gothic', 20, "bold"), text_color="#9290C3")
        self.title_label.place(x=170, y=50)
    #
    #     self.deposit_button = HoverButton(self, text="DEPOSIT", font=self.font, fg="light gray", bg='#FFFFFF', bd=0, command=self.open_deposit)
    #     self.deposit_button.place(x=50, y=200, width=150, height=60)
        self.deposit_button = CTkButton(master=self.frame, width=150, text='Deposit', corner_radius=6, bg_color=colors[1],fg_color=colors[2],command=self.open_deposit)
        self.deposit_button.place(x=30, y=240)

        self.withdraw_button = CTkButton(master=self.frame, width=150, text='Withdraw', corner_radius=6,
                                        bg_color=colors[1], fg_color=colors[2],command=self.open_withdraw)
        self.withdraw_button.place(x=200, y=240)

        self.balance_button = CTkButton(master=self.frame, width=150, text='Balance', corner_radius=6,
                                        bg_color=colors[1], fg_color=colors[2],command=self.open_check_balance)
        self.balance_button.place(x=370, y=240)

        self.exit_button = CTkButton(master=self.frame, width=200, text='Exit', corner_radius=6,
                                        bg_color=colors[1], fg_color=colors[2],command=self.logout)
        self.exit_button.place(x=180, y=500)


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
