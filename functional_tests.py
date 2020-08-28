from selenium import webdriver
import unittest

class BlogTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()


    def test_cv_has_all_info(self):
        #Upon opening the site the title should explain the page
        self.browser.get('http://localhost:8000/CV/')
        self.assertIn('CV', self.browser.title)
    
        #The user must also be able to see who I am on the page
        details = self.browser.find_element_by_id('details').text
        self.assertIn('Daniel Newsham', details)
        self.assertIn('dxn824@student.bham.ac.uk', details)
    
        #The user must also see a personal statement
        statement = self.browser.find_element_by_id('pstatement').text
        assertNotEqual('', statement)
    
        #Additionally, my education must be shown
        education = self.browser.find_element_by_id('education').text.lower()
        assertNotEqual('', education)
        self.assertIn('st ivo school', details)
        self.assertIn('university', details)
        
        #Other achievments must also be shown
        achievments = self.browser.find_element_by_id('achievments').text.lower()
        assertNotEqual('', achievments)
        
        #The work experience I have participated in must also be shown
        work = self.browser.find_element_by_id('wexperience').text.lower()
        assertNotEqual('', work)
    
    def test_cv_can_be_changed(self):
        #TODO
        self.assertEquals(False, True)
    
    

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  