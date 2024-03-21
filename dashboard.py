import tkinter

import customtkinter
from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

email = "Jayesh Channe"

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'

class Dashboard(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.search_container = None
        self.geometry("856x645")
        self.resizable(0,0)


        # self.set_appearance_mode("dark-blue")

        self.sidebar_frame = CTkFrame(master=self, fg_color=colors[1],  width=176, height=650, corner_radius=16,bg_color=colors[0])
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        self.person_img_data = Image.open("Images/person_icon.png")
        self.person_img = CTkImage(dark_image=self.person_img_data, light_image=self.person_img_data)
        customtkinter.CTkButton(master=self.sidebar_frame, image=self.person_img,text_color=colors[2], text=f"Account\n{email.upper()}", fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="NW").pack(anchor="center", ipady=5, pady=(10, 0))

        self.analytics_img_data = Image.open("Images/analytics_icon.png")
        self.analytics_img = CTkImage(dark_image=self.analytics_img_data, light_image=self.analytics_img_data)
        customtkinter.CTkButton(master=self.sidebar_frame, image=self.analytics_img,text_color=colors[2], text="Transactions", fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w",command=self.transaction).pack(anchor="center", ipady=5, pady=(60, 0))

        self.package_img_data = Image.open("Images/package_icon.png")
        self.package_img = CTkImage(dark_image=self.package_img_data, light_image=self.package_img_data)

        CTkButton(master=self.sidebar_frame, image=self.package_img, text="Transaction\nHistory",text_color=colors[2], fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        self.list_img_data = Image.open("Images/list_icon.png")
        self.list_img = CTkImage(dark_image=self.list_img_data, light_image=self.list_img_data)
        CTkButton(master=self.sidebar_frame, image=self.list_img, text="Personal\nDetails",text_color=colors[2], fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        self.settings_img_data = Image.open("Images/settings_icon.png")
        self.settings_img = CTkImage(dark_image=self.settings_img_data, light_image=self.settings_img_data)
        CTkButton(master=self.sidebar_frame, image=self.settings_img, text="Settings",text_color=colors[2], fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        self.person_img_data = Image.open("Images/logout_1.png")
        self.person_img = CTkImage(dark_image=self.person_img_data, light_image=self.person_img_data)
        CTkButton(master=self.sidebar_frame, image=self.person_img,text_color="#B53939", text="logout", fg_color="transparent", font=("Arial Bold", 14), hover_color=colors[0], anchor="S").pack(anchor="center", ipady=15, pady=(200, 0))

        self.main_view = CTkFrame(master=self, fg_color=colors[0],  width=680, height=650, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text=f"Hey, Welcome {email} ", font=("Arial Black", 25), text_color=colors[2]).pack(anchor="nw", side="left")

        self.metrics_frame = CTkFrame(master=self.main_view, fg_color="transparent")
        self.metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

        self.account_metric = CTkFrame(master=self.metrics_frame, fg_color=colors[1], width=200, height=60)
        self.account_metric.grid_propagate(0)
        self.account_metric.pack(side="left")

        self.logitics_img_data = Image.open("Images/logistics_icon.png")
        self.logistics_img = CTkImage(light_image=self.logitics_img_data, dark_image=self.logitics_img_data, size=(43, 43))

        CTkLabel(master=self.account_metric, image=self.logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

        CTkLabel(master=self.account_metric, text="Account Type", text_color="white", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        CTkLabel(master=self.account_metric, text="Saving", text_color="#fff", font=("Arial Black", 17), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

        self.balance_metric = CTkFrame(master=self.metrics_frame, fg_color=colors[1], width=200, height=60)
        self.balance_metric.grid_propagate(0)
        self.balance_metric.pack(side="left",expand=True, anchor="center")

        self.shipping_img_data = Image.open("Images/shipping_icon.png")
        self.shipping_img = CTkImage(light_image=self.shipping_img_data, dark_image=self.shipping_img_data, size=(43, 43))

        CTkLabel(master=self.balance_metric, image=self.shipping_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

        CTkLabel(master=self.balance_metric, text="Balance", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
        CTkLabel(master=self.balance_metric, text="91", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    def transaction(self):

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


    # table_data = [
    #     ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
    #     ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
    #     ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
    #     ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
    #     ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
    #     ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
    #     ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
    #     ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
    #     ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
    #     ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
    #     ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
    #     ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
    #     ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
    #     ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
    #     ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
    #     ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
    #     ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
    #     ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
    #     ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']
    # ]
    #
    # table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    # table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    # table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
    # table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    # table.pack(expand=True)


if __name__ == '__main__':
    dashboard = Dashboard()
    dashboard.mainloop()