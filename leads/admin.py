"""use the Django Admin to add some data for user, leads and agents"""
from django.contrib import admin

# Register your models here.
from .models import User, Lead, Agent

"""Lead group with register -> CRUD user, lead and agent"""
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)