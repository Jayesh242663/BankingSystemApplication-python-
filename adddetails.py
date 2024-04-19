import time
import tkinter
from datetime import datetime, date
import re

import customtkinter
from mysql import connector
from customtkinter import *
from tkinter import messagebox

import connection
from add_seq_questions import Security_questions_2

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'


def has_special_char(s):
    if re.search(r'\W', s) or re.search(r'\d', s):
        return True
    else:
        return False


def email_check(s):
    if re.search(r'@', s) and re.search(r'.com', s):
        return False
    else:
        return True


def open_add_seq_questions():
    add_seq_questions_page = Security_questions_2()
    add_seq_questions_page.mainloop()


class AddDetails(customtkinter.CTk):
    def __init__(self):
        global date_list
        super().__init__()
        self.title("Add Details")
        self.config(bg=colors[0], )
        self.geometry("1000x550")

        # name,number, email, dateofbirth, gender ,accountype ,address
        self.frame = CTkFrame(master=self, width=800, height=380, fg_color=colors[2], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label = CTkLabel(master=self.frame, text="Please fill the form to create an Account",
                              font=(fonts, 22, "bold"), text_color=colors[1])
        self.label.place(x=180, y=10)

        self.name_label = CTkLabel(master=self.frame, text="Name:", font=(fonts, 20))
        self.name_label.place(x=10, y=70)

        self.date_of_birth = CTkLabel(master=self.frame, text="Date Of Birth:", font=(fonts, 20))
        self.date_of_birth.place(x=10, y=130)

        self.gender_label = CTkLabel(master=self.frame, text="Gender:", font=(fonts, 20))
        self.gender_label.place(x=400, y=130)

        self.phone_number_label = CTkLabel(master=self.frame, text="Phone Number:", font=(fonts, 20))
        self.phone_number_label.place(x=10, y=200)

        self.email_label = CTkLabel(master=self.frame, text="Email:", font=(fonts, 20))
        self.email_label.place(x=400, y=70)

        self.account_type_label = CTkLabel(master=self.frame, text="Account Type:", font=(fonts, 20))
        self.account_type_label.place(x=10, y=250)

        self.address_label = CTkLabel(master=self.frame, text="Address:", font=(fonts, 20))
        self.address_label.place(x=400, y=200)

        self.name_entry = CTkEntry(master=self.frame, width=250)
        self.name_entry.place(x=85, y=70)

        self.email_entry = CTkEntry(master=self.frame, width=250)
        self.email_entry.place(x=470, y=70)

        self.address_entry = CTkEntry(master=self.frame, width=250)
        self.address_entry.place(x=490, y=200)

        date_list = [str(i) for i in range(1, 32)]
        self.date = CTkComboBox(master=self.frame, values=date_list, width=70)
        self.date.set("Day")
        self.date.place(x=150, y=130)

        month_list = [str(i) for i in range(1, 13)]
        self.month = CTkComboBox(master=self.frame, values=month_list, width=80)
        self.month.set("Month")
        self.month.place(x=220, y=130)

        current_year = datetime.today().year
        year_list = [str(i) for i in range(1950, current_year)]
        self.year = CTkComboBox(master=self.frame, values=year_list, width=70)
        self.year.set("Year")
        self.year.place(x=300, y=130)

        self.radio_var = tkinter.IntVar(value=0)
        self.male = CTkRadioButton(master=self.frame, text="Male", value=1, variable=self.radio_var, font=(fonts, 17))
        self.male.place(x=500, y=135)

        self.female = CTkRadioButton(master=self.frame, text="Female", value=2, variable=self.radio_var,
                                     font=(fonts, 17))
        self.female.place(x=580, y=135)

        self.account_type = CTkComboBox(master=self.frame,
                                        values=["Current Account", "Personal Account", "Saving Account"])
        self.account_type.place(x=160, y=250)

        self.number_entry = CTkEntry(master=self.frame)
        self.number_entry.place(x=170, y=200)

        self.submit_button = CTkButton(master=self.frame, text="Submit", command=self.create_account)
        self.submit_button.place(x=300, y=320)

        self.sq_label = CTkLabel(master=self.frame, text="Security Questions:", font=(fonts, 20))
        self.sq_label.place(x=400, y=250)

        self.sq_button = CTkButton(master=self.frame, text="SECURITY QUESTIONS", command=open_add_seq_questions)
        self.sq_button.place(x=600, y=255)

    # def phone_number_check(self, s):
    #     if re.search(r'\W', s) and re.search(r'[^A-Za-z]',s):
    #         if len(s) == 10:
    #            return False
    #     else:
    #         return True

    def create_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        day = self.date.get()
        month = self.month.get()
        year = self.year.get()
        dob = f"{year}-{month}-{day}"
        phoneno = self.number_entry.get()
        address = self.address_entry.get()
        gender = self.radio_var.get()
        account_type = self.account_type.get()

        if name == "" or email == "" or phoneno == "" or address == "":
            messagebox.showerror("ERROR", "Please fill all the information listed")
        else:
            if has_special_char(name):
                messagebox.showerror("Incorrect NAME", "Name should not have any NUMBERS/SYMBOLS/SPACES")
            else:
                if email_check(email):
                    messagebox.showerror("Incorrect EMAIL", "Please check your EMAIL ADDRESS")
                else:
                    if day.isdigit() and month.isdigit() and year.isdigit() is not True:
                        messagebox.showerror("Date Of Birth", "Please fill your Birthdate")
                    else:
                        today = date.today()
                        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
                        if age <= 18:
                            messagebox.showerror("Age Error", "Minors can't open an Account")
                        else:
                            if phoneno.isdigit() is not True:
                                messagebox.showerror("Incorrect Phone Number", "Please recheck your PHONE NUMBER")
                            elif len(phoneno) != 10:
                                messagebox.showerror("Incorrect Phone Number",
                                                     "Your phone number should be of 10 digits")
                            else:
                                balance = 500
                                if gender == 1:
                                    gender = "male"
                                elif gender == 2:
                                    gender = "female"
                                if gender == 0:
                                    messagebox.showerror("Gender", "Please select your gender")
                                else:
                                    try:
                                        db = connection.Connection().get_connection()
                                        cursor = db.cursor()
                                        sql = ("INSERT INTO acc_details (name, dob, gender, address, phoneno, acctype, "
                                               "email, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

                                        data = (name, dob, gender, address, phoneno, account_type, email, balance)

                                        cursor.execute(sql, data)
                                        db.commit()
                                        account_no = cursor.lastrowid
                                        messagebox.showinfo("Success", "Account created successfully.")
                                        time.sleep(2)
                                        messagebox.showinfo("Success", f"Your Account number:{account_no}")
                                        self.destroy()
                                        from password import Password
                                        password_page = Password()
                                        password_page.mainloop()

                                    except connector.Error as err:
                                        messagebox.showerror("Error", f"Error: {err}")


if __name__ == '__main__':
    details = AddDetails()
    details.mainloop()
