from django.test import TestCase
from django.urls import resolve
from blog.views import home
import CV.views

class CVTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home)  
        
    def test_cv_url_resolves_to_cv_home_view(self):
        found = resolve('/CV/')  
        self.assertEqual(found.func, CV.views.cvhome)  
        
    def test_cv_home_templates(self):
        response = self.client.get('/CV/')
        self.assertTemplateUsed(response, 'blog/base.html')
        self.assertTemplateUsed(response, 'CV/cvhome.html')

    def test_cv_edit_templates(self):
        response = self.client.get('/CV/edit/')
        self.assertTemplateUsed(response, 'blog/base.html')
        self.assertTemplateUsed(response, 'CV/cvedit.html')

    def test_can_save_a_POST_request(self):
        
        #Send POST
        
        pstatement = 'a cool personal statement'
        education = 'cool education'
        achievments = 'cool achievments'
        wexperience = 'cool work experiences'
        
        self.client.post('/CV/edit/', data={
            'pstatement': pstatement,
            'education': education,
            'achievments': achievments,
            'wexperience': wexperience
        })
        
        #Check is on CV
        
        response = self.client.get('/CV/')
        
        self.assertIn(pstatement, response.content.decode())
        self.assertIn(education, response.content.decode())
        self.assertIn(achievments, response.content.decode())
        self.assertIn(wexperience, response.content.decode())









