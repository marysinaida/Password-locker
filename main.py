import string
import random
import pyperclip

class User:
    '''
    Class that generate new instances of users
    '''

    user_list = [] #empty user list

    def __init__(self,first_name,last_name,phone_number,password,email):

        '''__init method that helps defining properties for our objects.'''

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.password = password
        self.email = email

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saves user from the user_list
        '''

        User.user_list.remove(self)

class Credentials:
    '''
    Class that generate new instances of credentials
    '''

    credentials_list = [] #empty credential list
    user_credentials_list = []

    @classmethod
    def check_user(cls,username,password):
        '''
         method that confirms the user_list match with the keyed password and name.
        '''
        current_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user = user.username
                return current_user

     


    def __init__(self,user_name,account_name,password):
        
        '''__init method that helps defining properties for our objects.'''

        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials a funtion to delete user credentials
        '''
        Credentials.credentials_list.remove(self)


    @classmethod
    def rand_pass(cls,size):
        '''
        method to generate password that takes random choice from and ascii_letters and digits
        '''

        generate_pass =''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])

        return generate_pass

     

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method to find a given account type associated with given credentials.
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential 

    @classmethod
    def display_credentials(cls,user_name):
        '''
        method to display credentials list saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def copy_credentials(cls,account_name):
        '''
        A method that copies credentials information after account is entered.
        '''
        found_credential = cls.find_by_account_name(account_name)
        return pyperclip.copy(found_credential.password)


    