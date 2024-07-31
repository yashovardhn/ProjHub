from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 'short_info', 'profile_image', 'social_github', 'social_website', 'social_twitter', 'social_linkedin']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description'] 

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'email', 'subject', 'body']