import json
import customtkinter
from customtkinter import *

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'

class Security_questions(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SECURITY QUESTIONS")
        self.config(bg=colors[0])
        self.geometry("600x400")

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
            question_label = CTkLabel(master=self, text=question_data["question"], font=(fonts, 12), wraplength=500)
            question_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            answer_entry = CTkEntry(master=self, font=(fonts, 12))
            answer_entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")

            self.answers[question_data["id"]] = answer_entry

        submit_button = CTkButton(master=self, text="Submit", font=(fonts, 12), command=self.submit_answers)
        submit_button.grid(row=len(self.questions), columnspan=2, pady=20)

    def submit_answers(self):
        user_answers = {}
        for question_id, answer_entry in self.answers.items():
            user_answers[question_id] = answer_entry.get()

        print("User Answers:", user_answers)

if __name__ == '__main__':
    App = Security_questions()
    App.mainloop()
