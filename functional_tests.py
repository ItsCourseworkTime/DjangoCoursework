from selenium import webdriver
import unittest
import time

class CVTest(unittest.TestCase):  

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
        self.assertNotEqual('', statement)
    
        #Additionally, my education must be shown
        education = self.browser.find_element_by_id('education').text.lower()
        self.assertNotEqual('', education)
        self.assertIn('st ivo school', education)
        self.assertIn('university', education)
        
        #Other achievments must also be shown
        achievments = self.browser.find_element_by_id('achievments').text.lower()
        self.assertNotEqual('', achievments)
        
        #The work experience I have participated in must also be shown
        work = self.browser.find_element_by_id('wexperience').text.lower()
        self.assertNotEqual('', work)
    
    def test_cv_can_be_changed(self):    
        #To edit the CV the edit button must be clicked
        self.browser.get('http://localhost:8000/CV/')
        self.assertEqual('CV Home', self.browser.title)
        self.browser.find_element_by_id('edit').click()
        
        #This reroutes to the edit page
        time.sleep(1)
        self.assertEqual('CV Edit', self.browser.title)
        
        #The personal statement is changed
        psinput = self.browser.find_element_by_name('psinput')
        psstr = 'This is the new personal statement that is very cool'
        psinput.send_keys(psstr)
        
        #Education can be edited
        eduinput = self.browser.find_element_by_id('education')
        edustr = 'This is education details that are very cool'
        eduinput.send_keys(edustr);
        
        #The listed achievments can be changed
        achievinput = self.browser.find_element_by_name('achievinput')
        achievstr = 'I achieved this thing that is very cool'
        achievinput.send_keys(achievstr)
        
        #Work experiences can be changed
        workinput = self.browser.find_element_by_name('workinput')
        workstr = 'This is some work experience I did that is very cool'
        workinput.send_keys(workstr)
        
        #This is saved, rerouting the user back to the CV
        self.browser.find_element_by_id('save').click()
        time.sleep(1)
        self.assertEqual('CV Home', self.browser.title)
        
        #The CV should now include the items added above with university completed
        self.assertIn(psstr, self.browser.find_element_by_id('pstatement').text)
        self.assertIn(edustr, self.browser.find_element_by_id('education').text)
        self.assertIn(achievstr, self.browser.find_element_by_id('achievments').text)
        self.assertIn(workstr, self.browser.find_element_by_id('wexperience').text)
        
    

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  