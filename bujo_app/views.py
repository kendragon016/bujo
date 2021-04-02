from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView

from .forms import UsernameForm, ProfileDetailsForm, ProfilePicForm, KeyForm
from .models import ProfileDetails, ProfilePic, Key

asked_name = False
saved_profile = False
name = None
nickname = "Nickname: Your Nickname"
bio = "Bio: A short description about yourself."
key_name = ""
description = ""

def home(request):
    global asked_name, name

    if asked_name:
        return render(request, "home.html", {'output': name})
    elif request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            asked_name = True
            name = form.cleaned_data['name']
            return render(request, "home.html", {'output': name})

        render(request, "home.html", {'form': form})

    form = UsernameForm()
    return render(request, "home.html", {'form': form})


def profile(request):
    global saved_profile, nickname, bio

    if request.GET.get('Edit1') == 'Edit1' or request.GET.get('Edit2') == 'Edit2':
        print('edit1 button can be heard')
        form = ProfileDetailsForm()
        return render(request, "profile.html", {'form': form, 'nickname': nickname, 'bio': bio})

    elif request.method == 'POST':
        form = ProfileDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data['nickname']
            bio = form.cleaned_data['bio']
            return render(request, "profile.html", {'nickname': nickname, 'bio': bio})

        render(request, "profile.html", {'nickname': nickname, 'bio': bio})

    profile_pic = ProfilePicForm()
    return render(request, "profile.html", {'nickname': nickname, 'bio': bio, 'profile_pic': profile_pic})


class KeyListView(View):
    model = Key


def key(request):
    global key_name, description

    form = KeyForm()
    key_context = Key.objects.all()
    all_keys = {'key_context': key_context}
    keys_and_form = {'key_context': key_context, 'form': form}

    if request.method == 'POST':
        print('request is a post')
        form = KeyForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            key_name = form.cleaned_data['key_name']
            print(key_name)
            description = form.cleaned_data['description']
            print(description)
            return render(request, "key.html", all_keys)

        form = KeyForm()
        render(request, "key.html", keys_and_form)

    elif request.GET.get('Add Key') == 'Add Key':
        print('add key button can be heard')
        form = KeyForm()
        return render(request, "key.html", keys_and_form)

    print("outside")
    form = KeyForm()
    return render(request, "key.html", all_keys)


def this_week(request):
    return render(request, 'this_week.html')


def today(request):
    return render(request, 'today.html')
