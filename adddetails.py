import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button, Combobox

import mysql.connector
from tkcalendar import DateEntry
class AddDetails(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Signup")
        self.geometry("800x600")
        self.create_widgets()


    def create_widgets(self):
        self.image3 = tk.PhotoImage(file="./Images/Bankimg1.png")
        self.bank_label_3 = tk.Label(self, image=self.image3)
        self.bank_label_3.place(x=0, y=0)
        # Labels
        labels = ["Name", "D.O.B", "Gender", "Address", "Account Type", "Balance"]
        for i, label_text in enumerate(labels):
            label = tk.Label(self, text=label_text, font=("Tahoma", 14, "bold"), fg="white", bg="gray")
            label.place(x=50, y=30 + i * 70)

        # Entry Fields
        self.name_entry = tk.Entry(self, font=("Tahoma", 14))
        self.name_entry.place(x=250, y=30, width=300)

        self.dob_entry = DateEntry(self, font=("Tahoma", 14))
        self.dob_entry.place(x=250, y=100, width=300)

        self.gender_var = tk.StringVar()
        self.male_radio = tk.Radiobutton(self, text="Male", font=("Tahoma", 14), variable=self.gender_var, value="Male")
        self.male_radio.place(x=250, y=170)

        self.female_radio = tk.Radiobutton(self, text="Female", font=("Tahoma", 14), variable=self.gender_var, value="Female")
        self.female_radio.place(x=400, y=170)

        self.address_entry = tk.Entry(self, font=("Tahoma", 14))
        self.address_entry.place(x=250, y=240, width=300)

        account_types = ["Savings", "Current", "Personal"]
        self.acctype_combobox = Combobox(self, values=account_types, font=("Tahoma", 14))
        self.acctype_combobox.place(x=250, y=310, width=300)

        self.balance_entry = tk.Entry(self, font=("Tahoma", 14))
        self.balance_entry.place(x=250, y=380, width=300)

        # Buttons
        self.next_button = Button(self, text="NEXT", command=self.store_data)
        self.next_button.place(x=300, y=470)

        self.back_button = Button(self, text="Back", command=self.open_starter)
        self.back_button.place(x=100, y=470)

    def store_data(self):
        try:
            name = self.name_entry.get()
            dob = self.dob_entry.get()
            gender = self.gender_var.get()
            address = self.address_entry.get()
            acctype = self.acctype_combobox.get()
            balance = self.balance_entry.get()

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="9321985498",
                port="3306",
                database="Bankingsys"
            )
            cursor = db.cursor()
            sql = "INSERT INTO acc_details (name, dob, gender, address, acctype, balance) VALUES (%s, %s, %s, %s, %s, %s)"

            # Specify the columns into which you want to insert the data
            data = (name, dob, gender, address, acctype, balance)

            cursor.execute(sql, data)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Account created successfully.")
            self.destroy()
            import password
            password.Password()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def open_starter(self):
        self.destroy()
        import starter
        starter.Starter()



if __name__ == "__main__":
    app = AddDetails()
    app.mainloop()
