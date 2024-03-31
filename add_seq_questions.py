import json
import tkinter
from tkinter import messagebox

import mysql.connector
import customtkinter
from customtkinter import *

import connection

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'

class Security_questions_2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SECURITY QUESTIONS")
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
        self.config(bg=colors[0])

        self.check_label = CTkLabel(master=self, text = "FILL SECURITY QUESTIONS FOR YOUR PASSWORD RECOVERY" ,font=(fonts, 18))
        self.check_label.place(x=50, y=10)

        self.frame = CTkFrame(master=self, width=1200, height=580, fg_color=colors[2], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        for i, question_data in enumerate(self.questions):
            question_label = CTkLabel(master=self.frame, text=question_data["question"], font=(fonts, 16), wraplength=500)
            question_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            answer_entry = CTkEntry(master=self.frame, font=(fonts, 12))
            answer_entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")

            self.answers[question_data["id"]] = answer_entry

        self.submit_button = CTkButton(master=self.frame, text="Submit", font=(fonts, 16), command=self.submit_answers)
        self.submit_button.grid(row=len(self.questions), columnspan=2, pady=40)

    def submit_answers(self):
        user_answers = {}

        all_answers_filled = all(answer_entry.get() for answer_entry in self.answers.values())

        if not all_answers_filled:
            messagebox.showerror("Error", "Please answer all three security questions.")
            return

        if not id:
            messagebox.showerror("Error", "Enter Your account number")
            return

        for question_id, answer_entry in self.answers.items():
            user_answers[question_id] = answer_entry.get()

        print("User Answers:", user_answers)

        user_answer = json.dumps(user_answers)

        try:
            db = connection.Connection().get_connection()

            cursor = db.cursor()
            cursor.execute("INSERT INTO answer (id, user_answer) VALUES (NULL, %s)", (user_answer,))

            db.commit()
            db.close()
            print("User answers saved in the database successfully.")
        except mysql.connector.Error as err:
            print("Error:", err)


if __name__ == '__main__':
    App = Security_questions_2()
    App.mainloop()
