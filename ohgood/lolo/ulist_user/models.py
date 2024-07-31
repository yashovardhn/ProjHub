from django.db import models
from django.contrib.auth.models import User
import uuid
# from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    short_info = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', blank=True, null=True)
    social_github = models.URLField(max_length=255, blank=True, null=True, verbose_name="GitHub Profile")
    social_twitter = models.URLField(max_length=255, blank=True, null=True, verbose_name="Twitter Profile")
    social_linkedin = models.URLField(max_length=255, blank=True, null=True, verbose_name="LinkedIn Profile")
    social_website = models.URLField(max_length=255, blank=True, null=True, verbose_name="Personal Website")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username or self.name or str(self.id)

    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='skills')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,related_name='messages')
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['-is_read', '-sent_at']







