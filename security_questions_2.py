import json
import mysql.connector
import customtkinter
from customtkinter import *

colors = ["#070F2B", "#1B1A55", "#535C91"]
fonts = 'Century Gothic'

class Security_questions_2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SECURITY QUESTIONS")
        self.config(bg="Black")
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

        self.Accno = CTkEntry(master=self, width=150, placeholder_text="Account number", fg_color="#424769")
        self.Accno.place(x=230, y=150)

        self.Accno_label = CTkLabel(master=self, text="Account number")
        self.Accno_label.place(x=10, y=150)

        self.submit_button = CTkButton(master=self, text="Submit", font=(fonts, 12), command=self.submit_answers)
        self.submit_button.grid(row=len(self.questions), columnspan=2, pady=40)

    def submit_answers(self):
        id = self.Accno.get()
        user_answers = {}
        for question_id, answer_entry in self.answers.items():
            user_answers[question_id] = answer_entry.get()

        print("Account Number:", id)
        print("User Answers:", user_answers)

        user_answer = json.dumps(user_answers)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="9321985498",
                database="Bankingsys"
            )
            cursor = conn.cursor()
            # Execute SQL query to insert or update user_answers
            cursor.execute("INSERT INTO answer (id, user_answer) VALUES (%s, %s)",(id, user_answer))

            conn.commit()
            conn.close()
            print("User answers saved in the database successfully.")
        except mysql.connector.Error as err:
            print("Error:", err)

if __name__ == '__main__':
    App = Security_questions_2()
    App.mainloop()
