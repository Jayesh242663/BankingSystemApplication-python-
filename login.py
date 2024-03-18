import tkinter

import customtkinter
from customtkinter import *
from tkinter import messagebox
import mysql.connector
colors =["#070F2B","#1B1A55","#535C91"]
class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.title("Login")
        self.config(bg=colors[0])
        self.geometry("600x440")

        self.frame = CTkFrame(master=self, width=320, height=360, fg_color=colors[1], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label = CTkLabel(master=self.frame, text="Log into your Account", font=('Century Gothic', 20, "bold"),
                              text_color="#9290C3")
        self.label.place(x=50, y=45)

        self.account_no_label = CTkEntry(master=self.frame, width=220, placeholder_text="Account Number",
                                         fg_color="#424769")
        self.account_no_label.place(x=50, y=110)

        self.password_label = CTkEntry(master=self.frame, width=220, placeholder_text="Password", fg_color="#424769")
        self.password_label.place(x=50, y=165)

        self.login_button = CTkButton(master=self.frame, width=220, text='Login', corner_radius=6, bg_color=colors[1],
                                      fg_color=colors[2],command=self.check_password)
        self.login_button.place(x=50, y=240)

    def login(self):
        accno = self.account_no_label.get()
        password = self.password_label.get()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="9321985498",
                port="3306",
                database="Bankingsys"
            )
            cursor = db.cursor()

            sql = "INSERT INTO login (accno, password) VALUES (%s, %s)"
            val = (accno, password)
            cursor.execute(sql, val)
            db.commit()
            db.close()

            messagebox.showinfo("Success", "Account created successfully.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    def check_password(self):
        username = self.account_no_label.get()
        password = self.password_label.get()

        # try:
        #     conn = mysql.connector.connect(
        #         host="localhost",
        #         user="root",
        #         password="9321985498",
        #         port="3306",
        #         database="Bankingsys"
        #     )
        #     cursor = conn.cursor()
        #
        #     cursor.execute("SELECT password FROM login WHERE accno = %s", (username,))
        #     user_record = cursor.fetchone()
        #
        #     if user_record:
        #         db_password = user_record[0]
        if username == "admin":
            print("username correct")

        if password == "admin":
            print("Password correct")
            # accno = user_record
            messagebox.showinfo("Success", "Username and password match. Logging in...")
            self.destroy()
            import options
            # options.Options(accno)
        else:
            messagebox.showerror("Error", "Incorrect password. Please try again.")
            # else:
            # messagebox.showerror("Error", "User does not exist. Please check your username.")
            # conn.close()
            # except mysql.connector.Error as e:(
            #     messagebox.showerror("Error", f"Error: {e}"))

    def open_starter(self):
        self.destroy()
        import starter
        starter.Starter()


if __name__ == "__main__":
    app = Login()
    app.mainloop()
