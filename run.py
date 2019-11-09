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

def rand_pass(size):
    '''
    a function that combines random letters and digits to generate new password
    '''
    return Credential.rand_pass(size)

def display_credentials(user_name):
    '''
    Aclass method that display all credentials of a given username.
    '''
    return Credentials.display_credentials(user_name)

def delete_credentials(credentials):
    '''
    Function to delete Credentials from credentials list
    '''
    credentials.delete_credentials()

def find_by_account_name(site_name):
    '''
    A function to search for an account using the credentials given
    '''
    return Credentials.find_by_account_name(account_name)

def copy_credentials(account_name):
    '''
    A method to enable copying credentials of a given account name.
    '''
    return Credentials.copy_credentials(account_name)
