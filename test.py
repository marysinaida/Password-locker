import unittest
from main import User, Credentials
import pyperclip

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

    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our contact_list
        '''
        self.new_user.save_user()
        test_user = User("Dorcas","Mary","0765432112","345@Snyder","Snyder@sm.com")#new user
        test_user.save_user()

        self.new_user.delete_user()#Deleting a user object
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    '''
    def setUp(self):
        '''Setup method to run before each test cases.'''
        self.new_credentials = Credentials("Snyder","Instagram","1234@dsm")
        #create credentials object

    def test_init(self):
        '''
        Test if the object is properly initialized
        '''
        self.assertEqual(self.new_credentials.user_name,"Snyder")
        self.assertEqual(self.new_credentials.account_name,"Instagram")
        self.assertEqual(self.new_credentials.password,"1234@dsm")

    def test_save_credentials(self):
        self.new_credentials.save_credentials() #saving the new credentials
        Instagram = Credentials('Snyder','Instagram','1234@dsm')
        Instagram.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        Instagram = Credentials('Snyder','Instagram','1234@dsm')
        Instagram.save_credentials()
        Instagram.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_by_account_name(self):
        '''
        Test to check if the test_find_by_account_name returns the correct credentials
        '''
        self.new_credentials.save_credentials()
        Instagram = Credentials('Snyder','Instagram','1234@dsm')
        Instagram.save_credentials()
        credential_found = Credentials.find_by_account_name('Instagram')
        self.assertEqual(credential_found.account_name,'Instagram') 

    def test_copy_credentials(self):
        '''
        A function to test to check if the copy of credentials method are the vaild
        '''
        self.new_credentials.save_credentials()
        Instagram = Credentials('Snyder','Instagram','1234@dsm')
        Instagram.save_credentials()
        found_credential = None
        for credential in Credentials.credentials_list:
            found_credential = Credentials.find_by_account_name(credential.account_name)
            return pyperclip.copy(found_credential.password)
            Credentials.copy_credentials(self.new_credential.account_name)
            self.assertEqual('1234@dsm',pyperclip.paste())



   






if __name__=='__main__':
    unittest.main()   