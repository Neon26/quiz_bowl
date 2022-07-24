from unicodedata import name
import requests
from urllib import response
import time
import json
import base64
#from wrapper import *
#from wrapper2 import *
#from quiz_bowl_api import *

#Allow Users to Rester an account
#Login a user with Basic Auth
url = 'https://cae-bootstore.herokuapp.com/'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_question = "/question"
endpoint_question_all = "/question/all"
endpoint_question_id = "/question/<id>"


def do_login_register():
    while True:
        #clear_output()
        print("Welcome to the Quiz Bowl!")
        email = input("Type your email to login or Type `register` to Register: ")
        if email == 'register':
            success_register=register()                
            if success_register:
                print("You have successfully registered")               

                return
        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                login(email)
                return
            except:
                print("Invalid Username/Password combo")
                time.sleep(2)
                continue

def login(email):
    #clear_output()
    password=input("Password: ")
    return login_user(email, password) 
    

def login_user(email, password):
    auth_string = email + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    return user_data.json()
def register():
    #clear_output()
    print("Registration:")
    email = input("Email: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = input("Password: ")
    
    payload={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    }
    

    return register_user(payload)
def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text


#If the user is anyone but you (doesn't has your google-classroom email address) then
#You should create a quiz with 10 random questions from the API from all users questions [Note the API isn't starting with 10 questions]
#After the question is completed you need to Award the user a score based on there correct or incorrect response


#If the User is you (has your google-classroom email address) The user should be prompted with extra prompts that each work properly:
#NOTE: They should also be able to take the quiz like a normal user
#Create Question
def create_question(self):
    question = input('Enter your question:\n')
    answer = input('Enter your answer:\n')

    question_dict={
        'question': question,
        'answer': answer
    }
    return create_question(self.user['token'], question_dict)
def create_question(token, payload):
    payload_json_string = json.dumps(payload)

    headers = {
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.post(
        url + endpoint_question,
        data = payload_json_string,
        headers = headers
    )
    return response.text 
#Edit Question
def edit_question(self):
    question = input('Enter your question:\n')
    answer = input('Enter your answer:\n')

    question_dict={
        'question': question,
        'answer': answer
    }
    return edit_question(self.user['token'], question_dict)
def edit_question(token, payload):
    payload_json_string = json.dumps(payload)

    headers={
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.put(
        url + endpoint_question_id,
        data=payload_json_string,
        headers=headers
    )
    return response.text



#Delete Question
def delete_question(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    
    response = requests.delete(
        url+endpoint_question_id,
        headers=headers
    )
    return response.text



#View My Questions
def get_questions_all():
    question_all = requests.get(url+endpoint_question_all)
    return question_all.json()['questions']



def main():
    do_login_register()
    login_user()
    

    while True:
        #clear_output()
        print("""
Welcome to the Quiz Bowl            
Would you like to:            
1. Take a quiz
2. Create a Question
3. Edit a Question
4. Delete a Question
5. View My Questions
6. Quit the application     
""")
        command = input("Select your Fate: ")
        if command == "1":
            pass
        elif command == "2":
            create_question()
            return
        elif command == "3":
            edit_question()
            return
        elif command == "4":
            delete_question()
            return
        elif command == "5":
            get_questions_all()
            return         
        elif command == "6":
            print("Goodbye")
            break
        else:
            print("Invalid Selection")
            time.sleep(2)
            continue
        break
main()