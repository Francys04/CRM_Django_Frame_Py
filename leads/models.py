""" It contains the essential fields and behaviors of the data you’re storing"""
from django.db import models
"""for authentification"""
from django.contrib.auth import get_user_model
"""AbstractUser is a built-in Django model that provides a fully featured User model implementation"""
from django.contrib.auth.models import AbstractUser
"""post_save is called just after the Django model save() function has done its job"""
from django.db.models.signals import post_save
# User = get_user_model()


""" Create user class, allows to create it whith python shell cmd"""
class User(AbstractUser):
    pass

# representation of the db_schema

class Lead(models.Model):
    """Example of relationship between tables first value for storage in db and seconde name of source"""
    # SOURCE_CHOISES = (
    #     ('YT', 'YouTube'),
    #     ('Goo', 'Google'),
    #     ('Nl', 'Newsletter'),
    # )
    
    
    """create data.type, CharField create data column in db contain str"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    
    """foreignkey tells on_delete , django how to handle the table row on instance is deleted, CASCADE -> 
     delete the class Agent, delete from all of relationship between lead and agent class Fereignkey"""
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    # phoned = models.BooleanField(default=False)
    """source of the lead, how find""" 
    # source = models.CharField(choices=SOURCE_CHOISES, max_length=150)
    
    """blank = submiting in empty str and null=True -> no value in db"""
    # profile_picture = models.ImageField(blank=True, null=True)
    
    """locate for file source"""
    # special_files = models.FieldFile(blank=True, null=True)


    """ querysets and managers"""
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


"""create relationship tables"""
class Agent(models.Model):# user auth, create many agents for one user
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    
   
    user = models.OneToOneField(User, on_delete=models.CASCADE) # for querysets and managers
    """return in str"""
    def __str__(self):# from python shell
        return self.user.email
    
"""user profile associated with the built-in User model through a one-to-one relationship
allows you to extend the default user model with additional fields and information specific to each user"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username    
    
"""Category"""
class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

""" Python function post_user_created_signal appears to be a signal handler for a user creation event. 
It is designed to respond to a signal (e.g., a post_save signal) that is sent whenever a new user object is created. """
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

"""post_save.connect(post_user_created_signal, sender=User) is the code that connects the post_user_created_signal 
function to the post_save signal of the User model in Django. 
This connection ensures that the post_user_created_signal function will be called automatically 
every time a new User instance is saved (i.e., created or updated)."""
post_save.connect(post_user_created_signal, sender=User)