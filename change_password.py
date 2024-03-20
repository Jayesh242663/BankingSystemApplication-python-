import tkinter
from tkinter import messagebox
import mysql.connector
import customtkinter
from customtkinter import *

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'

class Change_password(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("CHANGE PASSWORD")
        self.config(bg=colors[0])
        self.geometry("600x400")

        self.frame = CTkFrame(master=self, width=320, height=360, fg_color=colors[1], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label_1 = CTkLabel(master=self.frame, text="Change Your Password", font=(fonts, 20, "bold"),
                                 text_color="#9290C3")
        self.label_1.place(x=50, y=45)

        self.Account_number = CTkEntry(master=self.frame, width=220, placeholder_text="Account number",
                                       fg_color="#424769")
        self.Account_number.place(x=50, y=90)

        self.password_entry = CTkEntry(master=self.frame, width=220, placeholder_text="New Password",
                                        fg_color="#424769")
        self.password_entry.place(x=50, y=130)

        self.cnfpassword_entry = CTkEntry(master=self.frame, width=220, placeholder_text="Confirm Password",
                                           fg_color="#424769")
        self.cnfpassword_entry.place(x=50, y=175)

        self.change_button = CTkButton(master=self.frame, width=220, text="CHANGE", corner_radius=6,
                                       bg_color=colors[1], fg_color=colors[2], command=self.change_password)
        self.change_button.place(x=50, y=250)

    def change_password(self):
        account_number = self.Account_number.get()
        new_password = self.password_entry.get()
        confirm_password = self.cnfpassword_entry.get()

        if not all((account_number, new_password, confirm_password)):
            messagebox.showerror("Error", "Please fill in all fields.")
        elif new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="9321985498",
                    database="Bankingsys"
                )
                cursor = conn.cursor()
                cursor.execute("UPDATE login SET password = %s WHERE accno = %s", (new_password, account_number))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password changed successfully.")
                self.destroy()  # Close the window after successful password change
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

if __name__ == '__main__':
    App = Change_password()
    App.mainloop()
