# from urllib import response
# import requests
# from getpass import getpass
# import time
# import json
# import base64
# from wrapper import *
# from wrapper2 import *
# from quiz_bowl_api2 import *
# #from IPython.display import clear_output
# #from IPython.display import Image
# #from IPython.display import display

# def login(email):
#     #clear_output()
#     password=input("Password: ")
#     user = login_user(email, password) 
#     return user

# def register():
#     #clear_output()
#     print("Registration:")
#     email = input("Email: ")
#     first_name = input("First Name: ")
#     last_name = input("Last Name: ")
#     password = input("Password: ")
    
#     payload={
#         "email":email,
#         "first_name":first_name,
#         "last_name":last_name,
#         "password":password
#     }
    

#     return register_user(payload)

# def register_user(payload):
#     payload_json_string = json.dumps(payload)
#     headers = {
#         'Content-Type':'application/json'
#     }
#     response = requests.post(
#         url + endpoint_user,
#         data = payload_json_string,
#         headers = headers
#     )
#     return response.text


# def do_login_register():
#     while True:
#         #clear_output()
#         print("Welcome to the Quiz Bowl!")
#         email = input("Type your email to login or Type `register` to Register: ")
#         if email == 'register':
#             success_register=register()                
#             if success_register:
#                 print("You have successfully registered")               

#                 return
#         elif email.lower() == "quit":
#             print("Goodbye")
#             break
#         else:
#             try:
#                 login(email)
#             except:
#                 print("Invalid Username/Password combo")
#                 time.sleep(2)
#                 continue

# def main():
#     do_login_register()
    
    

#     while True:
#         #clear_output()
#         print("""
# Welcome to the Quiz Bowl            
# Would you like to:            
# 1. Take a quiz
# 2. Create a Question
# 3. Edit a Question
# 4. Delete a Question
# 5. View My Questions
# 6. Quit the application     
# """)
#         command = input("Select your Fate: ")
#         if command == "1"or ("take a quiz").lower:
#             quiz_bowl()
#             pass
#         elif command == "2" or ("Creat a question").lower:
#             create_question()
#             return
#         elif command == "3" or ("Edit a Question").lower:
#             edit_question()
#             pass
#         elif command == "4" or ("Delete a Question").lower:
#             delete_question()
#             pass
#         elif command == "5" or ("View My Questions").lower:
#             get_questions_all()
#             pass         
#         elif command == "6" or ("Quit the application").lower:
#             print("Goodbye")
#             break
#         else:
#             print("Invalid Selection")
#             time.sleep(2)
#             continue
#         break
    


# main()
