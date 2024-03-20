import tkinter
import customtkinter
from customtkinter import *
from adddetails import AddDetails
from login import Login

colors = ["#070F2B", "#1B1A55", "#535C91"]

class Starter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Banking System Application")
        self.geometry("600x440")
        self.config(bg=colors[0])

        self.frame = CTkFrame(master=self, width=320, height=300, fg_color=colors[1], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.login_button = CTkButton(master=self.frame, width=220, text='Login', corner_radius=6, bg_color=colors[1],
                                      fg_color=colors[2], command=self.open_login_page)
        self.login_button.place(x=50, y=200)

        self.signup_button = CTkButton(master=self.frame, width=220, text='Signup', corner_radius=6, bg_color=colors[1],
                                       fg_color=colors[2], command=self.open_signup_page)
        self.signup_button.place(x=50, y=70)

        self.label_1 = CTkLabel(master=self, text="DON'T HAVE AN ACCOUNT? CREATE ONE NOW", font=('Century Gothic', 13, "bold"), text_color="#9290C3",bg_color=colors[1])
        self.label_1.place(x=160 ,y=90)

        self.label_2 = CTkLabel(master=self, text="HAVE ONE,JUST CLICK ON LOGIN",
                                font=('Century Gothic', 13, "bold"), text_color="#9290C3", bg_color=colors[1])
        self.label_2.place(x=200, y=200)

    def open_login_page(self):
        self.destroy()
        login_page = Login()
        login_page.mainloop()

    def open_signup_page(self):
        self.destroy()
        signup_page = AddDetails()
        signup_page.mainloop()

if __name__ == "__main__":
    app = Starter()
    app.mainloop()
