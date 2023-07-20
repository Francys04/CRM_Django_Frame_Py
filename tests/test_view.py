"""Client is a class provided by Django that allows you to simulate requests to your Django application during testing. 
It provides methods to perform HTTP requests, such as get, post, put, delete, etc., 
and returns the response that your application would generate if it received such requests during actual use."""
from django.test import TestCase, Client
"""obtaining the URL patterns of views by their names."""
from django.urls import reverse
from leads.models import User
from leads.forms import CustomUserCreationForm

"""includes two test methods, test_signup_view_get and test_signup_view_post, 
to verify the behavior of the view for both GET and POST requests."""
class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signup')

    def test_signup_view_get(self):
        # Test the GET request to the signup view
        response = self.client.get(self.url)
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'registration/signup.html')
        # Assert that the form in the response context is an instance of CustomUserCreationForm
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_signup_view_post(self):
        # Test the POST request to the signup view
        # Ensure that the User does not exist in the database before signup
        self.assertFalse(User.objects.filter(username='leads.User').exists())

        # Post data for signup
        data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }

        response = self.client.post(self.url, data)
        # Assert that the view redirects to the 'login' URL (status code 302) after successful signup
        self.assertRedirects(response, reverse('login'))

        # Ensure that the User is created in the database after signup
        self.assertTrue(User.objects.filter(username='testuser').exists())

"""Render the landing page of your website. 
It includes one test method, test_landing_page_view, to verify the behavior of the view for a GET request."""
class LandingPageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('landing-page')
        

    def test_landing_page_view(self):
        # Test the GET request to the landing page view
        response = self.client.get(self.url)
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'landing.html')
