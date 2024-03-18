import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from tkinter import scrolledtext
import mysql.connector
from options import Options
from Buttons import HoverButton


class Withdraw(tk.Tk):
    def __init__(self, accno):
        super().__init__()
        self.accno = accno
        self.title("Withdraw")
        self.geometry("800x600")
        self.configure(bg='#F0F0F0')


        self.create_widgets()

    def create_widgets(self):
        self.image4 = tk.PhotoImage(file="./Images/Bankimg2.png")
        self.banklabel_4 = tk.Label(self, image=self.image4)
        self.banklabel_4.place(x=0, y=0)

        self.sp1 = scrolledtext.ScrolledText(self, width=50, height=3, wrap=tk.WORD, font=("Tahoma", 14))
        self.sp1.place(x=150, y=200)

        self.l2 = tk.Label(self, text="ENTER AMOUNT TO WITHDRAW", font=("Tahoma", 14), fg="white", bg="gray")
        self.l2.place(x=280, y=320)

        self.amount_entry = tk.Entry(self, font=("Tahoma", 14))
        self.amount_entry.place(x=350, y=400, width=120)

        self.withdraw_button = HoverButton(self, text="WITHDRAW",bg='#FFFFFF', command=self.withdraw)
        self.withdraw_button.place(x=420, y=450, width=220)

        self.back_button = HoverButton(self, text="BACK",bg='#FFFFFF', command=self.back)
        self.back_button.place(x=150, y=450, width=170)

        self.fetch_and_display_details()

    def fetch_and_display_details(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="9321985498",
                port="3306",
                database="Bankingsys"
            )
            cursor = conn.cursor()


            cursor.execute("SELECT name, balance FROM accounts WHERE accno = %s", (self.accno,))

            account_details = cursor.fetchone()

            if account_details:
                name, balance = account_details
                self.sp1.insert(tk.END, f"Name: {name}\n")
                self.sp1.insert(tk.END, f"Balance: {balance}\n")
            else:
                messagebox.showinfo("Error", "Account details not found.")

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    def withdraw(self):
        if not self.amount_entry.get():
            messagebox.showinfo("Error", "Enter the amount you want to withdraw.")
        else:
            try:
                amount = int(self.amount_entry.get())
                tempbalance_text = self.sp1.get(1.0, tk.END).strip()
                if not tempbalance_text:  # Check if text is empty
                    messagebox.showinfo("Error", "No balance information available.")
                else:
                    tempbalance = int(tempbalance_text.split()[-1])
                    if tempbalance < amount:
                        messagebox.showinfo("Error", "Balance is less than amount.")
                    else:
                        tempbalance -= amount
                        self.sp1.delete(1.0, tk.END)
                        self.sp1.insert(tk.INSERT, f"Balance: {tempbalance}")
                        messagebox.showinfo("Success", "Amount withdrawn successfully.")
            except ValueError:
                messagebox.showinfo("Error", "Invalid amount entered.")

    def back(self):
        self.destroy()
        Options(accno=self.accno)


if __name__ == "__main__":
    app = Withdraw(accno="accno")
    app.mainloop()
