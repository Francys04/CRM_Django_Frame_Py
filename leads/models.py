from django.db import models
# for authentification
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User = get_user_model()
# Create your models here.

# create user class
class User(AbstractUser):
    pass



# representation of the db_schema

class Lead(models.Model):
    # relationship between tables
    
    # first value for storage in db and seconde name of source
    # SOURCE_CHOISES = (
    #     ('YT', 'YouTube'),
    #     ('Goo', 'Google'),
    #     ('Nl', 'Newsletter'),
    # )
    
    # create data.type, CharField create data column in db contain str
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    
    # foreignkey tells on_delete , django how to handle the table row on instance is deleted, CASCADE -> 
    # delete the class Agent, delete from all of
    # relationship between lead and agent class Fereignkey
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    # phoned = models.BooleanField(default=False)
    # # source of the lead, how find 
    # source = models.CharField(choices=SOURCE_CHOISES, max_length=150)
    # # blank = submiting in empty str and null=True -> no value in db
    # profile_picture = models.ImageField(blank=True, null=True)
    
    # # locate for file source
    # special_files = models.FieldFile(blank=True, null=True)


    # create relationship tables
class Agent(models.Model):
    # user auth, cretae many agents for one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
      
    