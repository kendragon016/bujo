from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import UpdateView
from django.views.generic.list import ListView

from .forms import UsernameForm, ProfileDetailsForm, ProfilePicForm, KeyForm, ThisWeekForm, TodayForm
from .models import ProfileDetails, Key, ThisWeekItems, TodayItems

asked_name = False
name = None
nickname = "Nickname: Your Nickname"
bio = "Bio: A short description about yourself."
key_name = ""
description = ""
chosen_item_type = ""
item_details = ""
profile_pic = None


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
    global nickname, bio, profile_pic
    profile_pic = ProfilePicForm()

    if request.GET.get('Edit') == 'Edit':
        print('edit1 button can be heard')
        form = ProfileDetailsForm()
        return render(request, "profile.html", {'form': form, 'nickname': nickname, 'bio': bio, 'profile_pic': profile_pic})

    elif request.method == 'POST':
        form = ProfileDetailsForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            nickname = form.cleaned_data['nickname']
            bio = form.cleaned_data['bio']
            return render(request, "profile.html", {'nickname': nickname, 'bio': bio, 'profile_pic': profile_pic})

        print("outside of request method is post if")
        render(request, "profile.html", {'nickname': nickname, 'bio': bio, 'profile_pic': profile_pic})

    print("outside of profile")
    return render(request, "profile.html", {'nickname': nickname, 'bio': bio, 'profile_pic': profile_pic})

# class KeyListView(View):
#     model = Key

def key(request):
    global key_name, description

    form = KeyForm()
    key_context = Key.objects.all()
    all_keys = {'key_context': key_context}
    keys_and_form = {'key_context': key_context, 'form': form}

    if request.method == 'POST':
        form = KeyForm(request.POST)
        if form.is_valid():
            form.save()
            key_name = form.cleaned_data['key_name']
            description = form.cleaned_data['description']
            return render(request, "key.html", all_keys)

        form = KeyForm()
        render(request, "key.html", keys_and_form)

    elif request.GET.get('Add Key') == 'Add Key':
        form = KeyForm()
        return render(request, "key.html", keys_and_form)

    form = KeyForm()
    return render(request, "key.html", all_keys)


def this_week(request):
    if request.method == 'POST':
        form = ThisWeekForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "this_week.html", {"this_week_context": ThisWeekItems.objects.all()})

        form = ThisWeekForm()
        return render(request, "this_week.html", {"this_week_context": ThisWeekItems.objects.all(), "form": form})

    elif request.GET.get('Add Item') == 'Add Item':
        form = ThisWeekForm()
        return render(request, "this_week.html", {"this_week_context": ThisWeekItems.objects.all(), "form": form})

    form = ThisWeekForm()
    return render(request, "this_week.html", {"this_week_context": ThisWeekItems.objects.all()})

def edit_week_item(request, pk):
    item = ThisWeekItems.objects.get(id=pk)
    edited_item_form = ThisWeekForm(instance=item)

    if request.method == "POST":
        edited_item_form = ThisWeekForm(request.POST, instance=item)
        if edited_item_form.is_valid():
            edited_item_form.save()
            return redirect("/this_week")

    return render(request, 'edit_item.html', {'edited_item_form': edited_item_form})

def delete_week_item(request, pk):
    item = ThisWeekItems.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("/this_week")

    return render(request, 'delete_week_item.html', {'item': item})


# def done_task(request, pk):
#     task = ThisWeekItems.objects.get(id=pk)
#     task.done = True
#     task.save()

def today(request):
    if request.method == 'POST':
        form = TodayForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "today.html", {"today_context": TodayItems.objects.all()})

        form = TodayForm()
        return render(request, "today.html", {"today_context": TodayItems.objects.all(), "form": form})

    elif request.GET.get('Add Item') == 'Add Item':
        form = TodayForm()
        return render(request, "today.html", {"today_context": TodayItems.objects.all(), "form": form})

    form = TodayForm()
    return render(request, "today.html", {"today_context": TodayItems.objects.all()})

def edit_today_item(request, pk):
    item = TodayItems.objects.get(id=pk)
    edited_item_form = TodayForm(instance=item)

    if request.method == "POST":
        edited_item_form = TodayForm(request.POST, instance=item)
        if edited_item_form.is_valid():
            edited_item_form.save()
            return redirect("/today")

    return render(request, 'edit_item.html', {'edited_item_form': edited_item_form})

def delete_today_item(request, pk):
    item = TodayItems.objects.get(id=pk)
    if request.method == "POST":
        print("delete item post")
        item.delete()
        return redirect("/today")

    return render(request, 'delete_today_item.html', {'item': item})
