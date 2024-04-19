import tkinter
import mysql.connector
import customtkinter
from customtkinter import *
from tkinter import messagebox
import connection
from adddetails import AddDetails
from check_seq_question import Security_questions

# colors =["#070F2B","#1B1A55","#535C91"]
main_theme = ["#070F2B", "#1B1A55", "#535C91"]

# main_theme = ["#FF204E", "#A0153E", "#5D0E41"]
# main_theme = ["#9290C3","#535C91","#1B1A55"]
# main_theme = ["#FAF0E6", "#B9B4C7", "#5C5470"]
fonts = 'Century Gothic'


class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.config(bg=main_theme[0])
        self.geometry("995x540+300+150")

        self.frame1 = CTkFrame(master=self, width=320, height=360, fg_color=main_theme[2], corner_radius=16,
                               border_color="#3E065F", bg_color=main_theme[0])
        self.frame1.place(relx=0.38, rely=0.5, anchor=tkinter.CENTER)

        self.create_label = CTkLabel(master=self.frame1, text="Create your Account", font=(fonts, 20, "bold"),
                                     text_color=main_theme[1])
        self.create_label.place(x=50, y=45)

        self.description_label = CTkLabel(master=self.frame1,
                                          text="If you don't have an account\n with us.\n\nTHEN CREATE ONE "
                                               "NOW.\n\nJOIN OUR COMMUNITY",
                                          font=(fonts, 16),
                                          text_color="white")
        self.description_label.place(x=40, y=110)

        self.signup_button = CTkButton(master=self.frame1, width=220, text="Signup", corner_radius=6,
                                       bg_color=main_theme[2], fg_color=main_theme[1], command=self.open_signup_page)
        self.signup_button.place(x=50, y=250)

        self.frame = CTkFrame(master=self, width=320, height=360, fg_color=main_theme[1], corner_radius=16,
                              border_color="#3E065F", bg_color=main_theme[0])
        self.frame.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

        self.label = CTkLabel(master=self.frame, text="Log into your Account", font=(fonts, 20, "bold"),
                              text_color=main_theme[2])
        self.label.place(x=50, y=45)

        self.account_no_label = CTkEntry(master=self.frame, width=220, placeholder_text="Account Number",
                                         fg_color="#424769")
        self.account_no_label.place(x=50, y=110)

        self.password_label = CTkEntry(master=self.frame, width=220, placeholder_text="Password", fg_color="#424769",
                                       show="●")
        self.password_label.place(x=50, y=175)

        self.login_button = CTkButton(master=self.frame, width=220, text='Login', corner_radius=6,
                                      bg_color=main_theme[1], fg_color=main_theme[2], command=self.check_password)
        self.login_button.place(x=50, y=250)

        self.label_wrong_accountnumber = CTkLabel(master=self.frame, text="Incorrect Account number", font=(fonts, 16),
                                                  text_color="red")

        self.forget_button = CTkButton(master=self.frame, text="Forgot password", font=(fonts, 12), text_color="white",
                                       fg_color=main_theme[1], hover=(main_theme[1]), command=self.open_sq_page)
        self.forget_button.place(x=150, y=202)

    def login(self):
        global accno
        accno = self.account_no_label.get()
        global password
        password = self.password_label.get()
        if not accno.isdigit():
            messagebox.showerror("ERROR", "Please enter the correct Account Number")
        else:
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "INSERT INTO login (accno, password) VALUES (%s, %s)"
                val = (accno, password)
                cursor.execute(sql, val)
                db.commit()

                messagebox.showinfo("Success", "Account created successfully.")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error: {e}")

        # def signup(self):
        #     self.destroy()
        #     signup_window = adddetails.AddDetails()
        #
        #     self.signup_button.after(1000,adddetails.AddDetails.mainloop(self))

        def check_password(self):
            username = self.account_no_label.get()
            password = self.password_label.get()

            try:
                if username.isdigit() is not True:
                    messagebox.showerror("Error", "Account Number should be a number")
                db = connection.Connection().get_connection()

                cursor = db.cursor()

                cursor.execute("SELECT password FROM login WHERE accno = %s", (username,))
                global user_record

                user_record = cursor.fetchone()

                if user_record:
                    db_password = user_record[0]

                    if password == db_password:
                        messagebox.showinfo("Success", "Username and password match. Logging in...")
                        self.destroy()
                        import dashboard
                        dashboard = dashboard.Dashboard(username=username, password=password)
                        dashboard.mainloop()

                    else:
                        messagebox.showerror("Error", "Incorrect password. Please try again.")
                else:
                    messagebox.showerror("Error", "User does not exist. Please check your username.")

                db.close()
                return user_record
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error: {e}")

    def open_signup_page(self):
        self.destroy()
        signup_page = AddDetails()
        signup_page.mainloop()

    def open_sq_page(self):
        self.destroy()
        sq_page = Security_questions()
        sq_page.mainloop()


if __name__ == "__main__":
    app = Login()
    app.mainloop()
