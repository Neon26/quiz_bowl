from nturl2path import url2pathname
import requests
import json
import base64
from random import choice

url = 'https://cae-bootstore.herokuapp.com/'
endpoint_login = "/login"
endpoint_user = "/user"
endpoint_question = "/question"
endpoint_question_all = "/question/all"
endpoint_question_id = "/question/<id>"

def register_user(payload):
    if payload['email'] == 'shaynehakuna26@gmail.com':
        payload['admin'] = True
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

def user_info(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    response = requests.get(
        url + endpoint_user,
        headers = headers
    )
    return response.json()

def get_user_info(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    response = requests.get(
        url + endpoint_user,
        headers = headers
    )
    return response.json()

def get_all_admin_questions():
    question_all = requests.get(url+endpoint_question_all)
    return question_all.json()['questions']

def get_all_questions():
    question_all = requests.get(url+endpoint_question_all)
    return question_all.json()['questions']

def get_quiz_questions(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    question_all = requests.get(url+endpoint_question_all, headers=headers)
    return question_all.json()['questions']

def get_quiz(token,):
    headers = {
        'Authorization':"Bearer " + token
    }
    questions = requests.get(url+endpoint_question_id+'/all', headers=headers)
    data = questions.json()['questions']
    quiz=[]
    n=0
    while n<10:
        q= choice(data)
        if q not in quiz:
            quiz.append(q)
            n+=1
    return quiz

def create_a_question(token, payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json',
        'Authorization':"Bearer " + token
    }
    response = requests.post(
        url + endpoint_question,
        data = payload_json_string,
        headers = headers
    )
    return response.text

def edit_question(token, id, payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json',
        'Authorization':"Bearer " + token
    }
    response = requests.put(
        url + endpoint_question_id.replace('<id>', str(id)),
        data = payload_json_string,
        headers = headers
    )
    return response.text

def delete_question(token, id):
    headers = {
        'Authorization':"Bearer " + token
    }
    response = requests.delete(
        url + endpoint_question_id.replace('<id>', str(id)),
        headers = headers
    )
    return response.text