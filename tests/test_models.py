"""Django testing framework that allows to write test cases for your Django application. """
from django.test import TestCase
"""Use for authentication and user-related functionalities."""
from django.contrib.auth import get_user_model
from leads.models import Agent, UserProfile, Category

"""Django test case for testing the str representation of an Agent model. 
It appears that the Agent model has a foreign key relationship with the custom user model returned by get_user_model()."""
class AgentModelTest(TestCase):
    def test_agent_str_representation(self):
        user = get_user_model().objects.create_user(username="agent_user", password="testpassword")
        agent = Agent.objects.create(user=user)
        self.assertEqual(str(agent), "")

"""Django test case for testing the str representation of a Category model. The Category model seems to have a field named name, 
and the test verifies that the str representation of the Category object returns the correct name."""
class CategoryModelTest(TestCase):
    def test_category_str_representation(self):
        category = Category.objects.create(name="New")
        self.assertEqual(str(category), "New")

"""UserProfile model in response to signals during user creation and user updating."""
class SignalTestCase(TestCase):
    def test_user_profile_created_on_user_creation(self):
        user = get_user_model().objects.create_user(username="test_user", password="testpassword")
        self.assertEqual(UserProfile.objects.filter(user=user).count(), 1)

    def test_user_profile_not_created_on_existing_user(self):
        user = get_user_model().objects.create_user(username="existing_user", password="testpassword")
        # Ensure that the UserProfile is not created again if the user is updated
        user.save()
        self.assertEqual(UserProfile.objects.filter(user=user).count(), 1)

