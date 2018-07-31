from django import forms
from .models import Profile, Image


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['id', 'poster']
