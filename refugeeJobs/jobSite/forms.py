from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us something about yourself...'}))
    skills = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'List your skills...'}))
    language = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Languages you speak...'}))
    education = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Your educational background...'}))
    experience = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your work experience...'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'bio', 'skills', 'language', 'education', 'experience')
