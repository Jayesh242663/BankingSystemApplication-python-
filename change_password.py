import tkinter
from tkinter import messagebox
import mysql.connector
import customtkinter
from customtkinter import *

import connection

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'


class Change_password(customtkinter.CTk):
    def __init__(self, account_number):
        super().__init__()
        self.title("CHANGE PASSWORD")
        self.config(bg=colors[0])
        self.geometry("600x400")
        self.account_number = account_number

        self.frame = CTkFrame(master=self, width=320, height=360, fg_color=colors[1], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label_1 = CTkLabel(master=self.frame, text="Change Your Password", font=(fonts, 20, "bold"),
                                text_color="#9290C3")
        self.label_1.place(x=50, y=45)

        self.password_entry = CTkEntry(master=self.frame, width=220, placeholder_text="New Password",
                                       fg_color="#424769")
        self.password_entry.place(x=50, y=100)

        self.cnfpassword_entry = CTkEntry(master=self.frame, width=220, placeholder_text="Confirm Password",
                                          fg_color="#424769")
        self.cnfpassword_entry.place(x=50, y=155)

        self.change_button = CTkButton(master=self.frame, width=220, text="CHANGE", corner_radius=6,
                                       bg_color=colors[1], fg_color=colors[2], command=self.change_password)
        self.change_button.place(x=50, y=210)

    def change_password(self):
        account_number = self.account_number
        new_password = self.password_entry.get()
        confirm_password = self.cnfpassword_entry.get()

        if not all((new_password, confirm_password)):
            messagebox.showerror("Error", "Please fill in all fields.")
        elif new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()
                cursor.execute("UPDATE login SET password = %s WHERE accno = %s", (new_password, account_number))
                db.commit()
                messagebox.showinfo("Success", "Password changed successfully.")
                self.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")


if __name__ == '__main__':
    App = Change_password()
    App.mainloop()
