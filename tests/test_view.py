from django.test import TestCase
from django.urls import reverse
# Create your tests here.


"""create class to use TestCase
for landing page if write correct name of template, http status code
"""
class LandingPageTest(TestCase):
    """for status code, make a request to the url from LandingPage, if is ok => 200
    for template name if is correct name of html file"""
    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
        
           
"""for lead list view"""
class LeadListTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('leads'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_list.html")
        

 
        