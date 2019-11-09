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

def save_user(user):
    '''
    function to save a new user account
    '''
    User.save_user(user)

def save_credentials(Credential):
    '''
    function to save a new user credentials
    '''
    Credentials.save_credentials(Credential)

def verify_user(user,password):
    '''
    a function that ensure the existanceof the user before creating credentials
    '''
    checking_user = Credentials.chek_user(username,password)
    return checking_user
