import json
import tkinter

import customtkinter
from customtkinter import *

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'

class Security_questions(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SECURITY QUESTIONS")
        self.config(bg=colors[0])
        self.geometry("700x500")
        self.frame = CTkFrame(master=self,height=650, width=650,corner_radius=16,fg_color=colors[1],bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor= tkinter.CENTER)
        self.label = CTkLabel(master=self, text="Security Questions",bg_color=colors[0],font=(fonts, 22))
        self.label.place(x=260,y=10)
        self.description_label = CTkLabel(master=self, text="In case you forget your Password.\nTo reset the password these questions are neccesary to fill",bg_color=colors[0],font=(fonts,18))
        self.description_label.place(x=95,y=50)
        self.load_questions()

    def load_questions(self):
        try:
            with open("question.json", "r") as file:
                data = json.load(file)
                self.questions = data["questions"]
                self.create_question_widgets()
        except FileNotFoundError:
            print("Error: questions.json file not found.")

    def create_question_widgets(self):
        self.answers = {}
        for i, question_data in enumerate(self.questions):
            question_label = CTkLabel(master=self.frame, text=question_data["question"], font=(fonts, 18), wraplength=500)
            question_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            answer_entry = CTkEntry(master=self.frame, font=(fonts, 18))
            answer_entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")

            self.answers[question_data["id"]] = answer_entry

        submit_button = CTkButton(master=self.frame, text="Submit", font=(fonts, 18), command=self.submit_answers)
        submit_button.grid(row=len(self.questions), columnspan=2, pady=20)

    def submit_answers(self):
        user_answers = {}
        for question_id, answer_entry in self.answers.items():
            user_answers[question_id] = answer_entry.get()

        print("User Answers:", user_answers)

if __name__ == '__main__':
    App = Security_questions()
    App.mainloop()
