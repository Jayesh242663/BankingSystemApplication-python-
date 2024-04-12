from tkinter import *
from PIL import Image
import customtkinter

colors = ["#070F2B", "#1B1A55", "#535C91"]


class Stater(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Banking Application")
        self.geometry("895x680+350+80")
        self.config(bg=colors[0])
        self.resizable(False, False)
        self.image = customtkinter.CTkImage(light_image=Image.open('Images/starter_logo.png'),
                                            dark_image=Image.open('Images/starter_logo.png'),
                                            size=(895, 640))
        self.label = customtkinter.CTkLabel(self, image=self.image, text="")
        self.label.pack()

        self.button = customtkinter.CTkButton(self, text="Get Started", width=140, height=28, corner_radius=16,
                                              bg_color=colors[0], fg_color=colors[0],
                                              font=("Century Gothic", 18, "underline"), hover=False,
                                              command=self.login)
        self.button.pack(anchor="center")

    def login(self):
        self.destroy()
        import login
        login = login.Login()
        login.mainloop()


if __name__ == '__main__':
    stater = Stater()
    stater.mainloop()
