import tkinter as tk
import adddetails
import login
class Starter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banking System Application")
        self.geometry("1000x700")

        self.config(bg='black')
        self.image1 = tk.PhotoImage(file="./Images/Bankimg1.png")
        self.bank_image_label = tk.Label(self, image=self.image1)
        self.bank_image_label.place(x=0, y=0)

        self.login_button = tk.Button(self, text="LOGIN",bg='gray', font=("Helvetica", 20, "bold"), fg="white", command=self.open_login_page)
        self.login_button.place(x=370, y=400, width=100, height=50)
        self.signup_button = tk.Button(self, text="SIGN UP", font=("helvetica", 20, "bold"), fg="gray", command=self.open_add_details)
        self.signup_button.place(x=620, y=550, width=150, height=50)

        self.Label_2 = tk.Label(self, text="DON'T HAVE AN ACCOUNT? CREATE ONE NOW", font=("Tahoma", 20, "bold"), fg="gray" )
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
