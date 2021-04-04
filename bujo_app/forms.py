from django import forms
from .models import *


class UsernameForm(forms.Form):
    name = forms.CharField(label='', max_length=25)

class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ['nickname', 'bio']

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ['profile_pic']
        labels = {
            "profile_pic": ""
        }

class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['key_name', 'description']

class ThisWeekForm(forms.ModelForm):
    class Meta:
        model = ThisWeekItems
        fields = ['chosen_item_type', 'item_details']

class TodayForm(forms.ModelForm):
    class Meta:
        model = TodayItems
        fields = ['chosen_item_type', 'item_details']


