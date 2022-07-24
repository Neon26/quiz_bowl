#from urllib import response
from urllib import response
import requests
#from getpass import getpass
#mport time
import json
import base64
#rom quiz_bowl_api import login
#from wrapper import *

url = 'https://cae-bootstore.herokuapp.com/'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_question = "/question"
endpoint_question_all = "/question/all"
endpoint_question_id = "/question/<id>"


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
    
shayne_payload={
    "email":"shaynehakuna26@gmail.com",
    "first_name":"Shayne",
    "last_name":"Hakuna",
    "password":"123"
}

register_user(shayne_payload)

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
login_user('shaynehakuna26@gmail.com','123')
Shayne=login_user('shaynehakuna26@gmail.com','123')
print(Shayne['token'])


response = requests.get(url+endpoint_question_all)
print(response.status_code )

def get_questions_all():
    question_all = requests.get(url+endpoint_question_all)
    return question_all.json()['questions']
question_all = get_questions_all()
question_all

def post_question(token, payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json',        
        'Authorization':'Bearer' + token
    }
    response = requests.post(
        url + endpoint_question,
        data = payload_json_string,
        headers = headers
    )
    return response.text
    
    
def create_question(self):
    question = input('Enter your question:\n')
    answer = input('Enter your answer:\n')

    question_dict={
        'question': question,
        'answer': answer
    }
    return post_question(self.user['token'], question_dict)  
    
question_payload={
    "question":"What country produces the most coffee in the world?",
    "answer":"Brazil"
}

post_question(Shayne['token'], question_payload)

def get_questions():
    questions = requests.get(url+endpoint_question)
    return questions.json()['questions']
questions = get_questions()
questions
