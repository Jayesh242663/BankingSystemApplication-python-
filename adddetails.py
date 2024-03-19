# import tkinter as tk
# from tkinter import messagebox
# from tkinter.ttk import Button, Combobox
# from Buttons import HoverButton
#
#
# import mysql.connector
# from tkcalendar import DateEntry
# class AddDetails(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Signup")
#         self.geometry("800x600")
#         self.create_widgets()
#
#
#     def create_widgets(self):
#         self.image3 = tk.PhotoImage(file="./Images/Banking_1.png")
#         self.bank_label_3 = tk.Label(self, image=self.image3,)
#         self.bank_label_3.place(x=0, y=0)
#         labels = ["Name:", "D.O.B:", "Gender:", "Address:", "Account Type:", "Balance:"]
#         for i, label_text in enumerate(labels):
#             label = tk.Label(self, text=label_text, font=("Tahoma", 14, "bold"), fg="white",bg="black")
#             label.place(x=100, y=30 + i * 70)
#
#         # Entry FieldsD
#         self.name_entry = tk.Entry(self, font=("Tahoma", 14))
#         self.name_entry.place(x=250, y=30, width=300)
#
#         self.dob_entry = DateEntry(self, font=("Tahoma", 14))
#         self.dob_entry.place(x=250, y=100, width=300)
#
#         self.gender_var = tk.StringVar()
#         self.male_radio = tk.Radiobutton(self, text="Male", font=("Tahoma", 14), variable=self.gender_var, value="Male")
#         self.male_radio.place(x=250, y=170)
#
#         self.female_radio = tk.Radiobutton(self, text="Female", font=("Tahoma", 14), variable=self.gender_var, value="Female")
#         self.female_radio.place(x=400, y=170)
#
#         self.address_entry = tk.Entry(self, font=("Tahoma", 14))
#         self.address_entry.place(x=250, y=240, width=300)
#
#         account_types = ["Savings", "Current", "Personal"]
#         self.acctype_combobox = Combobox(self, values=account_types, font=("Tahoma", 14))
#         self.acctype_combobox.place(x=250, y=310, width=300)
#
#         self.balance_entry = tk.Entry(self, font=("Tahoma", 14))
#         self.balance_entry.place(x=250, y=380, width=300)
#
#         # Buttons
#         self.next_button = HoverButton(self, text="NEXT",bg='#FFFFFF', command=self.store_data)
#         self.next_button.place(x=300, y=470)
#
#         self.back_button = HoverButton(self, text="Back",bg='#FFFFFF', command=self.open_starter)
#         self.back_button.place(x=100, y=470)
#
#     def store_data(self):
#         try:
#             name = self.name_entry.get()
#             dob = self.dob_entry.get()
#             gender = self.gender_var.get()
#             address = self.address_entry.get()
#             acctype = self.acctype_combobox.get()
#             balance = self.balance_entry.get()
#
#             db = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="9321985498",
#                 port="3306",
#                 database="Bankingsys"
#             )
#             cursor = db.cursor()
#             sql = "INSERT INTO acc_details (name, dob, gender, address, acctype, balance) VALUES (%s, %s, %s, %s, %s, %s)"
#
#             # Specify the columns into which you want to insert the data
#             data = (name, dob, gender, address, acctype, balance)
#
#             cursor.execute(sql, data)
#             db.commit()
#             db.close()
#             messagebox.showinfo("Success", "Account created successfully.")
#             self.destroy()
#             import password
#             password.Password()
#         except mysql.connector.Error as err:
#             messagebox.showerror("Error", f"Error: {err}")
#
#     def open_starter(self):
#         self.destroy()
#         import starter
#         starter.Starter()
#
#
#
# if __name__ == "__main__":
#     app = AddDetails()
#     app.mainloop()


import tkinter
import customtkinter
from customtkinter import *
from tkinter import messagebox
colors =["#070F2B","#1B1A55","#535C91"]
fonts = 'Century Gothic'

class AddDetails(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add Details")
        self.config(bg=colors[0])
        self.geometry("1050x750")

        self.frame = CTkFrame(master=self, width=800, height=600 , fg_color=colors[2],corner_radius=16,border_color="#3E065F",bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label = CTkLabel(master=self.frame, text="Please fill the form to create an Account", font=(fonts, 22, "bold"), text_color=colors[1])
        self.label.place(x=10, y=10)

        self.name_label = CTkLabel(master=self.frame, text="Name:", font=(fonts,20))
        self.name_label.place(x=10, y=50)

        self.date_of_birth = CTkLabel(master=self.frame, text="Date Of Birth:", font=(fonts,20))
        self.date_of_birth.place(x=10, y=90)

        self.gender_label = CTkLabel(master=self.frame, text="Gender:", font=(fonts, 20))
        self.gender_label.place(x=10, y=130)

        self.phone_number_label = CTkLabel(master=self.frame, text="Phone Number:", font=(fonts, 20))
        self.phone_number_label.place(x=10, y=170)


if __name__ == '__main__':
    details = AddDetails()
    details.mainloop()
