import unittest
from main import User
from main import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''Set up method to run before each test cases.
        '''
        self.new_user = User("Snyder","345@Snyder")#create user object

    def test_init(self):
        '''
        Test if the object is properly initialized
        '''
        self.assertEqual(self.new_user.user_name,"Snyder")
        self.assertEqual(self.new_user.user_password,"345@snyder") 

if __name__=='__main__':
    unittest.main()   