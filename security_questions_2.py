import json
import pymysql
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

        self.Accno_label = CTkLabel(master=self, text="Account number")
        self.Accno_label.place(x=10, y=150)

        self.Accno = CTkEntry(master=self, width=150, placeholder_text="Enter Account number", fg_color="#424769")
        self.Accno.place(x=230, y=150)

        submit_button = CTkButton(master=self, text="Submit", font=(fonts, 12), command=self.submit_answers)
        submit_button.grid(row=len(self.questions), columnspan=2, pady=40)

    def submit_answers(self):
        user_answers = {}
        user_account_number = self.Accno.get()

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='9321985498',
                                     database='Bankingsys')

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM answer WHERE id = %s"
                cursor.execute(sql, (user_account_number,))
                db_answers = cursor.fetchall()

                if len(db_answers) == 0:
                    print("No answers found for the provided account number.")
                    return

                for db_answer in db_answers:
                    db_question_id = int(db_answer["id"])
                    db_answer_text = db_answer["answer"]
                    user_answer = user_answers.get(db_question_id)
                    if user_answer != db_answer_text:
                        print("Incorrect answer for question ID:", db_question_id)
                        break
                else:
                    print("All answers are correct.")

        finally:
            connection.close()

if __name__ == '__main__':
    App = Security_questions()
    App.mainloop()
