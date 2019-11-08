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