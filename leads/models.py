from django.db import models
# for authentification
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
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

    # querysets and managers
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # create relationship tables
class Agent(models.Model):
    # user auth, cretae many agents for one user
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    
    # for querysets and managers
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # from python shell
    def __str__(self):
        return self.user.email
    
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username    
    
# Category
class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)