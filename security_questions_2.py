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
        self.geometry("550x300")


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
        self.frame = CTkFrame(master=self, height=500, width=600, corner_radius=16 ,fg_color=colors[1], bg_color=colors[0])
        self.frame.place(x=35, y=20)

        self.Accno_label = CTkLabel(master=self.frame, text="Account number", font=(fonts, 18))
        self.Accno_label.place(x=10, y=150)

        self.Accno = CTkEntry(master=self.frame, width=150, placeholder_text="Enter Account number", fg_color="#424769")
        self.Accno.place(x=325, y=150)

        self.answers = {}
        for i, question_data in enumerate(self.questions):

            question_label = CTkLabel(master=self.frame, text=question_data["question"], font=(fonts, 18), wraplength=500)
            question_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            answer_entry = CTkEntry(master=self.frame, font=(fonts, 12))
            answer_entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")

            self.answers[question_data["id"]] = answer_entry


        submit_button = CTkButton(master=self.frame, text="Submit", font=(fonts, 12), command=self.submit_answers)
        submit_button.grid(row=len(self.questions), columnspan=3, pady=40)


    def back(self):
        import login
        login = login.Login()
        login.mainloop()
    def submit_answers(self):
        user_answers = {}
        user_account_number = self.Accno.get()

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='529374Channe@',
                                     database='Bankingsys')

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM answer WHERE id = %s"
                cursor.execute(sql, (user_account_number,))
                db_answers = cursor.fetchall()
                print(db_answers)

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
