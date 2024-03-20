import tkinter
import customtkinter
from customtkinter import *
from security_questions import Security_questions

colors =["#070F2B","#1B1A55","#535C91"]
fonts = 'Century Gothic'

class AddDetails(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add Details")
        self.config(bg=colors[0])
        self.geometry("1050x750")


        #name,number, email, addhar_number,
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

        self.security_questions = CTkLabel(master=self.frame, text="Security Questions", font=(fonts, 20))
        self.security_questions.place(x=10, y=290)

        self.security_questions_entry = CTkButton(master=self.frame, text="Provide Your Answers", font=(fonts, 20), command=self.open_security_questions)
        self.security_questions_entry.place(x=300, y=290)

    def open_security_questions(self):
        sq_page = Security_questions()
        sq_page.mainloop()



if __name__ == '__main__':
    details = AddDetails()
    details.mainloop()


