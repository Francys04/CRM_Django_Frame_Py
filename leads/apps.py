"""App Config helps you manage settings for your application."""
from django.apps import AppConfig

"""create a class for config the Leads
BigAutoField that auto increments on every instance of that model is created when you run makemigrations on the project. 
"""
class LeadsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leads'
