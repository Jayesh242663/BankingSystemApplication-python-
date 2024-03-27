import itertools
import tkinter
import customtkinter
import mysql
from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import connection
import login
colors = ["#070F2B", "#1B1A55", "#535C91"]
# colors = ["#070F2B", "#1B1A55", "#535C91"]
# colors = ["#FF204E","#A0153E","#5D0E41"]
# colors = ["#FAF0E6","#B9B4C7","#5C5470"]
# colors = ["#9290C3", "#535C91", "#1B1A55"]
fonts = 'Century Gothic'

class Dashboard(customtkinter.CTk):
    def __init__(self, username):
        super().__init__()
        self.title("Dashboard")
        self.username = username
        print(self.username)
        self.search_container = None
        self.geometry("856x645")
        self.resizable(0,0)

        try:
            self.db = connection.Connection().get_connection()
            self.cursor = self.db.cursor()
            self.cursor.execute("select * from acc_details where accno = %s",(self.username,))
            self.result = self.cursor.fetchall()
            self.result = self.result[0]
            for i in self.result:
                print(i)
        except mysql.connector.Error as e:
            print(e)

        # self.set_appearance_mode("dark-blue")

        self.sidebar_frame = CTkFrame(master=self, fg_color=colors[1],  width=176, height=650, corner_radius=16,bg_color=colors[0])
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        self.person_img_data = Image.open("Images/person_icon.png")
        self.person_img = CTkImage(dark_image=self.person_img_data, light_image=self.person_img_data)
        customtkinter.CTkButton(master=self.sidebar_frame, image=self.person_img,text_color=colors[2], text=f"Account\n{self.result[1]}", fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="NW").pack(anchor="center", ipady=5, pady=(10, 0))

        self.analytics_img_data = Image.open("Images/analytics_icon.png")
        self.analytics_img = CTkImage(dark_image=self.analytics_img_data, light_image=self.analytics_img_data)
        customtkinter.CTkButton(master=self.sidebar_frame, image=self.analytics_img,text_color=colors[2], text="Transactions", fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w",command=self.transaction).pack(anchor="center", ipady=5, pady=(60, 0))

        self.package_img_data = Image.open("Images/package_icon.png")
        self.package_img = CTkImage(dark_image=self.package_img_data, light_image=self.package_img_data)

        CTkButton(master=self.sidebar_frame, image=self.package_img, text="Transaction\nHistory",text_color=colors[2], fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w", command=self.history).pack(anchor="center", ipady=5, pady=(16, 0))

        self.list_img_data = Image.open("Images/list_icon.png")
        self.list_img = CTkImage(dark_image=self.list_img_data, light_image=self.list_img_data)
        CTkButton(master=self.sidebar_frame, image=self.list_img, text="Personal\nDetails",text_color=colors[2], fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w", command=self.personal_details).pack(anchor="center", ipady=5, pady=(16, 0))

        self.settings_img_data = Image.open("Images/settings_icon.png")
        self.settings_img = CTkImage(dark_image=self.settings_img_data, light_image=self.settings_img_data)
        CTkButton(master=self.sidebar_frame, image=self.settings_img, text="Settings",text_color=colors[2], fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        self.person_img_data = Image.open("Images/logout_1.png")
        self.person_img = CTkImage(dark_image=self.person_img_data, light_image=self.person_img_data)
        CTkButton(master=self.sidebar_frame, image=self.person_img,text_color="#B53939", text="logout", fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="S", command=self.logout).pack(anchor="center", ipady=15, pady=(200, 0))

        self.main_view = CTkFrame(master=self, fg_color=colors[0],  width=680, height=650, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text=f"Hey, Welcome {self.result[1]} ", font=("Arial Black", 25), text_color=colors[2]).pack(anchor="nw", side="left")

        self.metrics_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

        self.account_metric = CTkFrame(master=self.metrics_frame, fg_color=colors[1], width=200, height=60)
        self.account_metric.grid_propagate(0)
        self.account_metric.pack(side="left")

        self.logitics_img_data = Image.open("Images/logistics_icon.png")
        self.logistics_img = CTkImage(light_image=self.logitics_img_data, dark_image=self.logitics_img_data, size=(43, 43))

        CTkLabel(master=self.account_metric, image=self.logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

        CTkLabel(master=self.account_metric, text="Account Type", text_color="white", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        CTkLabel(master=self.account_metric, text=f"{self.result[5]}", text_color="#fff", font=("Arial Black", 17), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

        self.balance_metric = CTkFrame(master=self.metrics_frame, fg_color=colors[1], width=200, height=60)
        self.balance_metric.grid_propagate(0)
        self.balance_metric.pack(side="left",expand=True, anchor="center")

        self.shipping_img_data = Image.open("Images/shipping_icon.png")
        self.shipping_img = CTkImage(light_image=self.shipping_img_data, dark_image=self.shipping_img_data, size=(43, 43))

        CTkLabel(master=self.balance_metric, image=self.shipping_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

        CTkLabel(master=self.balance_metric, text="Balance", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        CTkLabel(master=self.balance_metric, text=f"{self.result[6]}", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))
        self.window_count = 0

    def transaction(self):
        if self.window_count == 2:
            self.details_frame.destroy()
        elif self.window_count == 3:
            self.table_frame.destroy()
        self.window_count = 1
        self.transaction_frame = CTkFrame(master=self.main_view, height=400, fg_color=colors[1], corner_radius=16)
        self.transaction_frame.pack(fill="x", pady=(45, 0), padx=27)

        self.label_transaction = CTkLabel(master=self.transaction_frame, text_color=colors[2],
                                          text="Transactions\nTo Perfom any transaction.\nPlease fill the given details.",
                                          font=("Arial Black", 20))
        self.label_transaction.place(x=150, y=10)

        self.sender_label = CTkLabel(master=self.transaction_frame, text="Enter the Account number\nof the receiver",
                                     text_color=colors[2], font=("Arial Black", 17))
        self.sender_label.place(x=30, y=130)

        self.sender_entry = CTkEntry(master=self.transaction_frame, font=("Arial Black", 17), width=200)
        self.sender_entry.place(x=335, y=140)

        self.amount_label = CTkLabel(master=self.transaction_frame, text_color=colors[2], text="Amount to be Transferred",
                                     font=("Arial BLack", 17))
        self.amount_label.place(x=35, y=250)

        self.amount_entry = CTkEntry(master=self.transaction_frame, width=200, font=("Arial Black", 17))
        self.amount_entry.place(x=335, y=250)

        self.transfer_button = CTkButton(master=self.transaction_frame, text="Transfer", command=self.confirm_transaction)
        self.transfer_button.place(x=225, y=350)

    def confirm_transaction(self):
        acc_no = self.sender_entry.get()
        amt = self.amount_entry.get()

        self.amount_entry.delete(0,END)
        self.sender_entry.delete(0, END)

        self.password_of_account = CTkInputDialog(
            text=f"You are transfering money to {acc_no}\nAmount:{amt}\nPlease Enter your account password to confirm transfer",
            title="Confirm the transaction",
            fg_color=colors[1],
            button_fg_color=colors[0])

    def personal_details(self):
        if self.window_count == 1:
            self.transaction_frame.destroy()
        elif self.window_count == 3:
            self.table_frame.destroy()
        self.window_count = 2
        self.details_frame = CTkFrame(master=self.main_view, height=400, fg_color=colors[1], corner_radius=16)
        self.details_frame.pack(fill="x", pady=(45, 0), padx=27)

        self.name = self.result[1]
        self.email = self.result[5]

        self.acc_no = self.result[0]
        self.dob = self.result[2]
        self.gender = self.result[3]
        self.phone_no = self.result[4]
        self.address = self.result[6]

        self.title_label = CTkLabel(master=self.details_frame, text="Personal Details of the Account holder",
                                    text_color=colors[2], font=("Arial Black", 22))
        self.title_label.place(x=70, y=20)

        self.name_label = CTkLabel(master=self.details_frame, text=f"NAME:- {self.name}", text_color=colors[2],
                                   font=("Arial Black", 17))
        self.name_label.place(x=40, y=70)

        self.email_label = CTkLabel(master=self.details_frame, text=f"Email:- {self.email}",
                                    text_color=colors[2],
                                    font=("Arial Black", 17))
        self.email_label.place(x=250, y=120, anchor="e")

        self.dob_label = CTkLabel(master=self.details_frame, text=f"Date Of Birth:- {self.dob}", text_color=colors[2],
                                  font=("Arial Black", 17))
        self.dob_label.place(x=40, y=150)

        self.phone_no_label = CTkLabel(master=self.details_frame, text=f"Phone Number:- {self.phone_no}",
                                       text_color=colors[2],
                                       font=("Arial Black", 17))
        self.phone_no_label.place(x=40, y=190)

        self.gender_label = CTkLabel(master=self.details_frame, text=f"Gender:- {self.gender}", text_color=colors[2],
                                     font=("Arial Black", 17))
        self.gender_label.place(x=40, y=230)

        self.account_number_label = CTkLabel(master=self.details_frame, text=f"Account Number:- {self.acc_no}",
                                             text_color=colors[2],
                                             font=("Arial Black", 17))
        self.account_number_label.place(x=40, y=270)

        self.address_label = CTkLabel(master=self.details_frame, text=f"Address:- {self.address}", text_color=colors[2],
                                      font=("Arial Black", 17))
        self.address_label.place(x=40, y=310)


    def logout(self):
        self.destroy()
        import login
        login = login.Login()
        login.mainloop()

    def history(self):
        if self.window_count == 1:
            self.transaction_frame.destroy()
        elif self.window_count == 2:
            self.details_frame.destroy()
        try:
            self.db = connection.Connection().get_connection()
            self.cursor = self.db.cursor()
            self.cursor.execute("select sender_accno,name,amount,date,time,transaction_id from transaction where accno = %s", (1,))
            self.data = self.cursor.fetchall()
            for result in self.data:
                print(result)
        except mysql.connector.Error as e:
            print(e)

        self.table_data = [
            [("Account\nNumber", "Name", "Amount", "Date", "Time","Transaction\nID")]
        ]
        self.table_data.append(self.data)
        self.table_data = list(itertools.chain(*self.table_data))
        print(self.table_data)
        self.table_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        table = CTkTable(master=self.table_frame, values=self.table_data, colors=[colors[1], colors[2]], header_color=colors[1])
        table.edit_row(0, text_color="#fff")
        table.pack(expand=True)
        self.window_count = 3

if __name__ == '__main__':
    dashboard = Dashboard()
    dashboard.mainloop()