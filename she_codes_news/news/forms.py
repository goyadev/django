# Django classes we need
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Comment

# Form for submitting a story
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            ),
        }

# Form for submitting a comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'date_added': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            ),
        }