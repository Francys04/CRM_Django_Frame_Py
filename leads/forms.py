"""forms for taking input from the user in some manner and using that information for logical operations on databases."""
from django import forms
"""This method will return the currently active user model – the custom user model if one is specified, or User otherwise."""
from django.contrib.auth import get_user_model
"""build-in user authentication system, build-in module inherits from the ModelForm class"""
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead

"""create a obj for active user model"""
User = get_user_model()

"""info about lead"""
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

"""when a user submits the form, it will be validated using the form's is_valid() method. 
If the form is valid, you can access the cleaned data (data that has been processed and converted to the appropriate 
Python data types) using the cleaned_data attribute of the form. 
Then you can take further actions with the submitted data, such as saving it to a database or performing other operations. 
If the form is not valid, you can handle the errors accordingly."""
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


"""for user creation"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}