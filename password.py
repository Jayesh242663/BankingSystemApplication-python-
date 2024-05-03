import tkinter
from tkinter import messagebox
import mysql.connector
import customtkinter
from customtkinter import *

import connection
from adddetails import AddDetails
from login import Login

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'


class Password(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Set Password")
        self.config(bg=colors[0])
        self.geometry("600x440")

        self.frame = CTkFrame(master=self, width=320, height=360, fg_color=colors[1], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label_1 = CTkLabel(master=self.frame, text="Set Your Password", font=(fonts, 20, "bold"),
                                text_color="#9290C3")
        self.label_1.place(x=50, y=45)

        self.password_entry = CTkEntry(master=self.frame, width=220, placeholder_text="PASSWORD",
                                       fg_color="#424769")
        self.password_entry.place(x=50, y=110)

        self.cnfpassword_entry = CTkEntry(master=self.frame, width=220, placeholder_text="CONFIRM PASSWORD",
                                          fg_color="#424769")
        self.cnfpassword_entry.place(x=50, y=175)

        self.next = CTkButton(master=self.frame, width=120, text='Next', corner_radius=6, bg_color=colors[1],
                              fg_color=colors[2], command=self.open_login)
        self.next.place(x=165, y=300)

        self.back = CTkButton(master=self.frame, width=120, text='Back', corner_radius=6, bg_color=colors[1],
                              fg_color=colors[2], command=self.open_add_details)
        self.back.place(x=30, y=300)

        self.create_button = CTkButton(master=self.frame, width=220, text="CREATE", corner_radius=6, bg_color=colors[1],
                                       fg_color=colors[2], command=self.create_password)
        self.create_button.place(x=50, y=250)

    def create_password(self):
        password1 = self.password_entry.get()
        password2 = self.cnfpassword_entry.get()

        if not password1 or not password2:
            messagebox.showerror("Error", "Please enter both password and confirm password.")
        elif len(password1) < 4:
            messagebox.showerror("Error", "Password should be more or equal than 4 digits")
        elif password1 != password2:
            messagebox.showerror("Error", "Passwords do not match.")
        elif not password1.isdigit() or not password2.isdigit():
            messagebox.showerror("Error", "Password should not consist of any Alphabet or symbols")
        else:
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()
                cursor.execute("INSERT INTO login (password) VALUES (%s)", (password1,))
                db.commit()
                messagebox.showinfo("Success", "Your password has been set.")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def open_add_details(self):
        self.destroy()
        adddetails_page = AddDetails()
        adddetails_page.mainloop()

    def open_login(self):
        self.destroy()
        login_page = Login()
        login_page.mainloop()


if __name__ == "__main__":
    app = Password()
    app.mainloop()
