import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from tkinter import scrolledtext


class Deposit(tk.Tk):
    def __init__(self, accno):
        super().__init__()
        self.accno = accno
        self.title("Deposit")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.image5 = tk.PhotoImage(file="./Images/Bankimg2.png")
        self.banklabel_5 = tk.Label(self, image=self.image5)
        self.banklabel_5.place(x=0, y=0)

        self.sp1 = scrolledtext.ScrolledText(self, width=50, height=3, wrap=tk.WORD, font=("Tahoma", 14))
        self.sp1.place(x=150, y=200)

        self.l2 = tk.Label(self, text="ENTER AMOUNT TO DEPOSIT", font=("Tahoma", 14), fg="light gray")
        self.l2.place(x=280, y=380)

        self.amount_entry = tk.Entry(self, font=("Tahoma", 14))
        self.amount_entry.place(x=350, y=450, width=120)

        self.deposit_button = Button(self, text="DEPOSIT", command=self.deposit)
        self.deposit_button.place(x=500, y=480, width=200)

        self.back_button = Button(self, text="BACK", command=self.back)
        self.back_button.place(x=150, y=480, width=170)

    def deposit(self):
        if not self.amount_entry.get():
            messagebox.showinfo("Error", "Enter the amount you want to deposit.")
        else:
            try:
                amount = int(self.amount_entry.get())
                tempbalance = int(self.sp1.get(1.0, tk.END).split()[-1])  # Extracting balance from scrolledtext
                tempbalance += amount
                self.sp1.delete(1.0, tk.END)
                self.sp1.insert(tk.INSERT, f"Balance: {tempbalance}")
                messagebox.showinfo("Success", "Amount deposited successfully.")
            except Exception as e:
                messagebox.showinfo("Error", str(e))

    def back(self):
        self.destroy()
        import options
        options.Options()


if __name__ == "__main__":
    app = Deposit(accno="accno")
    app.mainloop()
