"""Django testing framework that allows to write test cases for your Django application. """
from django.test import TestCase
"""get_user_model is a helper function provided by the django.contrib.auth module. 
It is used to retrieve the user model that is currently active"""
from django.contrib.auth import get_user_model
from leads.forms import LeadModelForm, LeadForm, CustomUserCreationForm

"""returns the user model class that is being used for authentication and user-related functionalities."""
User = get_user_model()

"""The purpose of these two test methods (test_lead_model_form_valid_data and test_lead_model_form_invalid_data) 
is to check the validation behavior of the LeadModelForm for both valid and invalid data."""
class LeadModelFormTest(TestCase):
    def test_lead_model_form_valid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30,
            'agent': None,  # Replace this with a valid Agent object if required
        }
        form = LeadModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_lead_model_form_invalid_data(self):
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'age': -5,
            'agent': None,  # Replace this with a valid Agent object if required
        }
        form = LeadModelForm(data=form_data)
        self.assertFalse(form.is_valid())

""" This class contains two test methods, test_lead_form_valid_data and test_lead_form_invalid_data, 
which are used to check the validation behavior of the LeadForm for both valid and invalid data."""
class LeadFormTest(TestCase):
    def test_lead_form_valid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30,
        }
        form = LeadForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_lead_form_invalid_data(self):
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'age': -5,
        }
        form = LeadForm(data=form_data)
        self.assertFalse(form.is_valid())


""" Check the validation behavior of the CustomUserCreationForm for both valid and invalid data."""
class CustomUserCreationFormTest(TestCase):
    def test_custom_user_creation_form_valid_data(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_data(self):
        form_data = {
            'username': '',
            'password1': 'testpassword123',
            'password2': 'testpassword456',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
