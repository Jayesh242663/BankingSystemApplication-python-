import tkinter as tk

class demo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry('340x440')
        self.config(bg='#333333')

        self.login_label = tk.Label(self,text='Login')
        self.username_label = tk.Label(
            self,text='Usrename',bg='#333333',fg='#FFFFFF', font=("Arial",30))
        self.username_entry = tk.Entry(self,)
        self.password_entry = tk.Entry(self,show="*",font=("Arial",16))
        self.password_label = tk.Label(
            self,text="Password",bg='#333333',fg='#FFFFFF',font=("Arial",16))
        self.login_button = tk.Button(
            self,text="login",bg='#FF3399',fg='#333333',font=("Arial",30))

        self.login_label.grid(row=0,column=0, columnspan=2,)
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1,column=1)
        self.password_label.grid(row=2,column=0)
        self.password_entry.grid(row=2,column=1)
        self.login_button.grid(row=3, column=0, columnspan=2)

if __name__ == '__main__':
    app = demo()
    app.mainloop()

