import json
import tkinter
from tkinter import messagebox

import customtkinter
from customtkinter import *
import mysql.connector

import connection
from change_password import Change_password

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
        self.check_label = CTkLabel(master=self, text="FILL SECURITY QUESTIONS FOR YOUR VERIFICATION",
                                    font=(fonts, 18))
        self.check_label.place(x=50, y=10)

        self.frame = CTkFrame(master=self, width=1200, height=580, fg_color=colors[2], corner_radius=16,
                              border_color="#3E065F", bg_color=colors[0])
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        for i, question_data in enumerate(self.questions):
            question_label = CTkLabel(master=self.frame, text=question_data["question"], font=(fonts, 12), wraplength=500)
            question_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            answer_entry = CTkEntry(master=self.frame, font=(fonts, 12))
            answer_entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")

            self.answers[question_data["id"]] = answer_entry

        self.Accno_label = CTkLabel(master=self.frame, text="Account number: ")
        self.Accno_label.place(x=100, y=150)

        self.Accno = CTkEntry(master=self.frame, width=150, placeholder_text="Enter Account number", fg_color="#424769")
        self.Accno.place(x=230, y=150)

        self.submit_button = CTkButton(master=self.frame, text="Submit", font=(fonts, 12), command=self.submit_answers)
        self.submit_button.grid(row=len(self.questions), columnspan=2, pady=40)

    def submit_answers(self):
        account_number = self.Accno.get()
        user_answers = {}

        all_answers_filled = all(answer_entry.get() for answer_entry in self.answers.values())

        if not all_answers_filled:
            messagebox.showerror("Error", "Please answer all three security questions.")
            return
        elif not account_number:
            messagebox.showerror("Error", "Enter Your account number")
            return

        try:
            account_number = int(account_number)
        except ValueError:
            messagebox.showerror("Error", "Account Number should be a number")
            return
        for question_id, answer_entry in self.answers.items():
            user_answers[question_id] = answer_entry.get()

        print("User Answers:", user_answers)

        try:
            db = connection.Connection().get_connection()

            cursor = db.cursor()
            cursor.execute("SELECT user_answer FROM answer WHERE id = %s", (account_number,))
            result = cursor.fetchone()
            print(result[0])

            if result:
                user_answers = json.loads(result[0])
                if user_answers == user_answers:
                    print("User answers match the stored answers.")
                    change_password_page = Change_password(account_number = account_number)
                    change_password_page.mainloop()

                else:
                    print("User answers do not match the stored answers.")
            else:
                print("No user answers found for the provided account number.")

            db.close()

        except mysql.connector.Error as err:
            print("Error:", err)


if __name__ == '__main__':
    App = Security_questions()
    App.mainloop()
