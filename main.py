class User:
    '''
    Class that generate new instances of users
    '''

    user_list = [] #empty user list

    def __init__(self,first_name,last_name,phone_number,password,email):

        '''__init method that helps defining properties for our objects.'''

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.password = password
        self.email = email