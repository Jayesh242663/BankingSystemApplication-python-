import tkinter as tk
from tkinter import messagebox
import mysql.connector
from Buttons import HoverButton


class Password(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("SET YOUR PASSWORD")
        self.configure(bg='#F0F0F0')

        self.image7 = tk.PhotoImage(file="./Images/Passwordimg.png")
        self.password_image = tk.Label(self, image=self.image7)
        self.password_image.place(x=0, y=0)

        self.font = ("Tahoma", 22)

        self.title_label = tk.Label(self, text="SET YOUR PASSWORD", font=("tahoma", 20, "bold"), fg="white", bg="black")
        self.title_label.place(x=230, y=15, width=400, height=30)

        self.pass1_label = tk.Label(self, text="PASSWORD:", font=self.font, fg="light gray", bg="black")
        self.pass1_label.place(x=130, y=140, width=180, height=40)

        self.pass2_label = tk.Label(self, text="CONFIRM PASSWORD:", font=self.font, fg="light gray", bg="black")
        self.pass2_label.place(x=75, y=205, width=300, height=40)

        self.pass1_entry = tk.Entry(self, font=("tahoma", 28), fg="black", bg="white")
        self.pass1_entry.place(x=380, y=140, width=200, height=50)

        self.pass2_entry = tk.Entry(self, font=("tahoma", 28), fg="black", bg="white")
        self.pass2_entry.place(x=380, y=200, width=200, height=50)

        self.login_button = HoverButton(self, text="LOGIN", font=("tahoma", 25, "bold"), fg="light gray", bg='black',  command=self.open_login)
        self.login_button.place(x=310, y=400, width=150, height=50)

        self.create_button = HoverButton(self, text="CREATE", font=("tahoma", 25, "bold"), fg="light gray", bg='black', command=self.create_password)
        self.create_button.place(x=400, y=290, width=150, height=50)

        self.back_button = HoverButton(self, text="BACK", font=("tahoma", 25, "bold"), fg="light gray", bg='black',  command=self.open_add_details)
        self.back_button.place(x=200, y=290, width=150, height=50)

    def create_password(self):
        password1 = self.pass1_entry.get()
        password2 = self.pass2_entry.get()

        if password1 != password2:
            messagebox.showerror("Error", "Passwords do not match.")
        elif not password1:
            messagebox.showerror("Error", "Please enter a password.")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="9321985498",
                    database="Bankingsys"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO login (password) VALUES (%s)", (password1,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been set.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    def display_passwords(self):
        password1 = self.pass1_entry.get()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="9321985498",
                database="Bankingsys"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT accno, password FROM login WHERE password = %s", (password1,))
            rows = cursor.fetchall()
            conn.close()

            if rows:
                messagebox.showinfo("Account Numbers and Passwords", "\n".join([f"Account No: {row[0]}, Password: {row[1]}" for row in rows]))
            else:
                messagebox.showinfo("No Matches", "No accounts found with this password.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def open_add_details(self):
        self.destroy()
        import adddetails
        adddetails.AddDetails()

    def open_login(self):
        self.destroy()
        import login
        login.Login()

if __name__ == "__main__":
    Password().mainloop()
