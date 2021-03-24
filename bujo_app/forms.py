from django import forms


class UsernameForm(forms.Form):
    name = forms.CharField(label='', max_length=25)