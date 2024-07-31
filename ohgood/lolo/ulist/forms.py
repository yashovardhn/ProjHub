from django import forms
from .models import Project, Review

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' # to select all models from all models
        fields = ['title', 'description', 'source_link', 'demo_link', 'featured_image', 'tag'] # to select only specific fields

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Vote',
            'body': 'Comment',
        }
        widgets = {
            'value': forms.Select(choices=Review.vote_type),
            'body': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Write your review here...'}),
        }
