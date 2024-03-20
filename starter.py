import tkinter as tk
import adddetails
import login
from Buttons import HoverButton

class Starter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banking System Application")
        self.geometry("800x600")
        self.configure(bg='#F0F0F0')

        self.image1 = tk.PhotoImage(file="Images/Banking_1.png")
        self.bank_image_label = tk.Label(self, image=self.image1)
        self.bank_image_label.place(x=0, y=0)

        self.login_button = HoverButton(self, text="LOGIN",bg='#FFFFFF', font=("Tahoma", 20, "bold"), fg="gray", command=self.open_login_page)
        self.login_button.place(x=370, y=400, width=100, height=50)

        self.signup_button = HoverButton(self, text="SIGN UP",bg='#FFFFFF', font=("Tahoma", 20, "bold"), fg="gray", command=self.open_add_details)
        self.signup_button.place(x=550, y=540, width=150, height=40)

        self.Label_2 = tk.Label(self, text="DON'T HAVE AN ACCOUNT? CREATE ONE NOW", font=("Tahoma", 16, "bold"), fg="gray", bg='#F0F0F0' )
        self.Label_2.place(x=30, y=550)



    def open_login_page(self):
        self.destroy()
        login.Login()

    def open_add_details(self):
        self.destroy()
        adddetails.AddDetails()

if __name__ == "__main__":
    app = Starter()
    app.mainloop()
