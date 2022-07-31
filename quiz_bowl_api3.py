from time import sleep
from wrapper3 import *

class User():

    def __init__(self,user_info):
        self.user_info=user_info
        self.score=0
        self.quiz=[]
        self.name=user_info['first_name']+" "+user_info['last_name']
        self.token=self.user_info['token']
        self.all_questions=get_all_questions(self.token)
        self.missed=[]

    def take_quiz(self):
        n=1
        for q in self.quiz:
            missed={}
            print(f"Question {n}: {q['question']}")
            answer=input("Enter your answer:\n")
            if answer==q['answer']:
                self.score+=1
                print(f"Correct! Your score is {self.score}")
            else:
                missed['question']=q['question']
                missed['answer']=q['answer']
                missed['your_answer']=answer
                self.missed.append(missed)
                print(f"Incorrect! Your score is {self.score}")
            n+=1
            sleep(1)
        print(f"Your score is {self.score}")
        print(f"You missed {len(self.missed)} questions")
    
    def get_total_questions(self):
        self.all_questions=get_all_questions(self.token)
        return len(self.all_questions)
    
    def set_quiz(self):
        self.quiz=[]
        for i in range(0,self.get_total_questions()):
            self.quiz.append(self.all_questions[i])
        return self.quiz

    def display_score(self):
        print(f"Your score is {self.score}")
        print(f"You missed {len(self.missed)} questions")
        for i in self.missed:
            print(f"Question: {i['question']}")
            print(f"Answer: {i['answer']}")
            print(f"Your answer: {i['your_answer']}")
            print("\n")

class Admin(User):

    def __init__(self, user_info):
        super().__init__(user_info)
        self.token=self.user_info['token']
        self.all_questions=get_all_questions(self.token)
        self.missed=[]
        self.score=0

    def my_questions(self):
        return get_all_admin_questions(self.token)

    def create_question(self):
        question = input('Enter your question:\n')
        answer = input('Enter your answer:\n')
        payload = {
            "question": question,
            "answer": answer
        }
        response = create_a_question(self.token, payload)        
        print("Question created!")
        return response
    

    def edit_question(self):
            self.display_questions()
            question_id = input("Enter the question ID you want to edit:\n")
            if question_id.isdigit():
                question = input("Enter your question:\n")
                answer = input("Enter your answer:\n")
                payload = {
                    "question": question,
                    "answer": answer
                }
                edit_question(self.token, payload, question_id)
                print("Question edited!")
            else:
                print("Invalid question ID")
    def delete_question(self):
        self.display_questions()
        question_id = input("Enter the question ID you want to delete:\n")
        if question_id.isdigit():
            delete_question(self.token, question_id)
            print("Question deleted!")
        else:
            print("Invalid question ID")

    def display_questions(self):
        for i in self.all_questions:
            print(f"Question ID: {i['id']}")
            print(f"Question: {i['question']}")
            print(f"Answer: {i['answer']}")
            print("\n")

class UI:

    def __init__(self):
        self.user_info=get_user_info()
        self.user=User(self.user_info)
        self.admin=Admin(self.user_info)
    
    def do_login_register():
        while True:
            #clear_output()
            print("Welcome to the Quiz Bowl!")
            email = input("Type your email to login or Type `register` to Register: ")
            if email == 'register':
                success_register=UI.register()                
                if success_register:
                    print("You have successfully registered")               

                    return
            elif email.lower() == "quit":
                print("Goodbye")
                break
            else:
                try:
                    UI.login(email)
                    return
                except:
                    print("Invalid Username/Password combo")
                    continue

    def login(self,email):
        password=input("Enter your password:\n")
        user=login_user(email,password)
        return user
    
    def register(self):
        print("Registering user...")
        email=input("Enter your email:\n")
        password=input("Enter your password:\n")
        first_name=input("Enter your first name:\n")
        last_name=input("Enter your last name:\n")
        payload={
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name
        }
        return register_user(payload)

    def main_menu(self):
        while True:
            print("Welcome to the Quiz Bowl API!")
            email= input("Login in with your email:\n or type 'register' to register:\n")
            if email=="register":
                UI.register()
                continue
            user=self.login(email)
            if user:
                print("Login successful!")
                self.user.set_quiz()
                self.user.take_quiz()
                self.user.display_score()
                break
            else:
                print("Login failed!")
                continue
        if user_info['is_admin']:
            print("You are an admin!")
            while True:
                print("Admin menu:")
                print("1. Create a question")
                print("2. Edit a question")
                print("3. Delete a question")
                print("4. Display all questions")
                print("5. Exit")
                choice=input("Enter your choice:\n")
                if choice=="1":
                    self.admin.create_question()
                elif choice=="2":
                    self.admin.edit_question()
                elif choice=="3":
                    self.admin.delete_question()
                elif choice=="4":
                    self.admin.display_questions()
                elif choice=="5":
                    break
                else:
                    print("Invalid choice")
                    continue
        

if __name__ == '__main__':
    UI.do_login_register()
    UI.main_menu()
        
