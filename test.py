import unittest
from main import User
# from main import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''Set up method to run before each test cases.
        '''
        self.new_user = User("Dorcas","Mary","0765432112","345@Snyder","Snyder@sm.com")#create user object

    def test_init(self):
        '''
        Test if the object is properly initialized
        '''
        self.assertEqual(self.new_user.first_name,"Dorcas")
        self.assertEqual(self.new_user.last_name,"Mary")
        self.assertEqual(self.new_user.phone_number,"0765432112")
        self.assertEqual(self.new_user.password,"345@Snyder")
        self.assertEqual(self.new_user.email,"Snyder@sm.com") 

    def test_save_user(self):
        '''
        Test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)
        



if __name__=='__main__':
    unittest.main()   