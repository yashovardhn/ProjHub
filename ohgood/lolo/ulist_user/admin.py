from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Profile)  # Registering the Profile model in admin panel.
admin.site.register(models.Skill) # Registering the Skill model in admin panel.
admin.site.register(models.Message) # Registering the message model in admin panel. 


