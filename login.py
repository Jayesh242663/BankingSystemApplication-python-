import tkinter as tk
from tkinter.ttk import Button
from tkinter import messagebox
import mysql.connector
from Buttons import HoverButton

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("800x600")
        self.configure(bg='#F0F0F0')

        self.image2 = tk.PhotoImage(file="./Images/Bankimg1.png")
        self.bank_image_label = tk.Label(self, image=self.image2)
        self.bank_image_label.place(x=0, y=0)

        self.username_label = tk.Label(self, text="ACCOUNT NO:", font=("Tahoma", 28, "bold"), fg="white")
        self.username_label.place(x=140, y=120)

        self.username_entry = tk.Entry(self, font=("Tahoma", 28))
        self.username_entry.place(x=425, y=120, width=200, height=50)

        self.password_label = tk.Label(self, text="PASSWORD:", font=("Tahoma", 28, "bold"), fg="white")
        self.password_label.place(x=140, y=190)

        self.password_entry = tk.Entry(self, font=("Tahoma", 28), show="*")
        self.password_entry.place(x=425, y=190, width=200, height=50)

        self.login_button = HoverButton(self, text="LOGIN",bg='#FFFFFF', command=self.check_password)
        self.login_button.place(x=425, y=350, width=150, height=50)

        self.cancel_button = HoverButton(self, text="Cancel",bg='#FFFFFF', command=self.open_starter)
        self.cancel_button.place(x=250, y=350, width=150, height=50)

    def login(self):
        accno = self.username_entry.get()
        password = self.password_entry.get()

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
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="9321985498",
                port="3306",
                database="Bankingsys"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT password FROM login WHERE accno = %s", (username,))
            user_record = cursor.fetchone()

            if user_record:
                db_password = user_record[0]

                if password == db_password:
                    accno = user_record
                    messagebox.showinfo("Success", "Username and password match. Logging in...")
                    self.destroy()
                    import options
                    options.Options(accno)
                else:
                    messagebox.showerror("Error", "Incorrect password. Please try again.")
            else:
                messagebox.showerror("Error", "User does not exist. Please check your username.")

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    def open_starter(self):
        self.destroy()
        import starter
        starter.Starter()


if __name__ == "__main__":
    app = Login()
    app.mainloop()
