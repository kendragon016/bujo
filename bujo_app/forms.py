from django import forms
from .models import ProfileDetails, ProfilePic, Key


class UsernameForm(forms.Form):
    name = forms.CharField(label='', max_length=25)

class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ['nickname', 'bio']

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = ['profile_pic']
        labels = {
            "profile_pic": ""
        }

class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['key_name', 'description']

