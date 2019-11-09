import pyperclip
from main import User,Credentials

def create_user(first_name,last_name,phone_number,email,password):
    '''
    fuction to create a new user account
    '''
    new_user = User(first_name,last_name,phone_number,email,password)
    return new_user

def create_credntials(user_name,account_name,password):
    '''
    function to create new user account
    '''
    new_credential =Credentials(user_name,account_name,password):
    return new_credential
