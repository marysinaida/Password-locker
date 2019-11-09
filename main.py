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

    @classMethod
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
        
 