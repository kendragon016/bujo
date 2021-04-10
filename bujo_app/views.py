from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import UpdateView
from django.views.generic.list import ListView

from .forms import *
from .models import *

asked_name = False
name = None
key_name = ''
description = ''
chosen_item_type = ''


def index(request):
    return redirect('/home')


def home(request):
    global asked_name, name

    if asked_name:
        return render(request, 'home.html', {'output': name})
    elif request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            asked_name = True
            name = form.cleaned_data['name']
            return render(request, 'home.html', {'output': name})

        render(request, 'home.html', {'form': form})

    form = UsernameForm()
    return render(request, 'home.html', {'form': form})


def profile(request):
    form = ProfileDetailsForm()

    if ProfileDetails.objects.count() == 0:
        obj = ProfileDetails.objects.create(
            nickname='Nickname: Your Nickname',
            bio='Bio: A short description about yourself.',
            profile_pic="images/defaultpic.png"
        )
        obj.save()
        return render(
            request,
            'profile.html',
            {'profile_context': ProfileDetails.objects.all()[:1].get()}
        )
    elif request.method == 'POST':
        form = ProfileDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'profile.html',
                {'profile_context': ProfileDetails.objects.all()[:1].get()}
            )
        form = ProfileDetailsForm()
        return render(
            request,
            'profile.html',
            {'profile_context': ProfileDetails.objects.all()[:1].get(),
             'form': form}
        )

    form = ProfileDetailsForm()
    return render(
        request,
        'profile.html',
        {'profile_context': ProfileDetails.objects.all()[:1].get()}
    )


def edit_profile(request, pk):
    info = ProfileDetails.objects.get(id=pk)
    form = ProfileDetailsForm(instance=info)
    pic_form = ProfilePicForm()

    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return render(
                request,
                'profile.html',
                {'profile_context': ProfileDetails.objects.all()[:1].get(),
                 'pic_form': pic_form}
            )

    return render(
        request,
        'edit_item.html',
        {'form': form}
    )


def edit_pic(request, pk):
    info = ProfileDetails.objects.get(id=pk)
    form = ProfilePicForm(instance=info)

    if request.method == 'POST':
        form = ProfilePicForm(
            request.POST, request.FILES,
            instance=info
        )
        if form.is_valid():
            form.save()
            return render(
                request,
                'profile.html',
                {'profile_context': ProfileDetails.objects.all()[:1].get()}
            )

    form = ProfilePicForm()
    return render(
        request,
        'edit_item.html',
        {'form': form}
    )


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
            return render(request, 'key.html', all_keys)

        form = KeyForm()
        render(request, 'key.html', keys_and_form)

    elif request.GET.get('Add Key') == 'Add Key':
        form = KeyForm()
        return render(request, 'key.html', keys_and_form)

    form = KeyForm()
    return render(request, 'key.html', all_keys)


def this_week(request):
    if request.method == 'POST':
        form = ThisWeekForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request,
                'this_week.html',
                {'this_week_context': ThisWeekItems.objects.all()}
            )

        form = ThisWeekForm()
        return render(
            request,
            'this_week.html',
            {'this_week_context': ThisWeekItems.objects.all(),
             'form': form}
        )

    elif request.GET.get('Add Item') == 'Add Item':
        form = ThisWeekForm()
        return render(
            request,
            'this_week.html',
            {'this_week_context': ThisWeekItems.objects.all(),
             'form': form}
        )

    form = ThisWeekForm()
    return render(
        request,
        'this_week.html',
        {'this_week_context': ThisWeekItems.objects.all()}
    )


def today(request):
    if request.method == 'POST':
        form = TodayForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request,
                'today.html',
                {'today_context': TodayItems.objects.all()}
            )

        form = TodayForm()
        return render(
            request,
            'today.html',
            {'today_context': TodayItems.objects.all(), 'form': form}
        )

    elif request.GET.get('Add Item') == 'Add Item':
        form = TodayForm()
        return render(
            request,
            'today.html',
            {'today_context': TodayItems.objects.all(),
             'form': form}
        )

    form = TodayForm()
    return render(
        request,
        'today.html',
        {'today_context': TodayItems.objects.all()}
    )


def edit_item(request, pk):
    page = request.path.rsplit('/', 3)[-3]

    if page == 'this_week':
        item = ThisWeekItems.objects.get(id=pk)
        form = ThisWeekForm(instance=item)

        if request.method == 'POST':
            form = ThisWeekForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/this_week')

    elif page == 'today':
        item = TodayItems.objects.get(id=pk)
        form = TodayForm(instance=item)

        if request.method == 'POST':
            form = TodayForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/today')

    return render(
        request,
        'edit_item.html',
        {'form': form}
    )


def delete_item(request, pk):
    page = request.path.rsplit('/', 3)[-3]

    if page == 'this_week':
        item = ThisWeekItems.objects.get(id=pk)

        if request.method == 'POST':
            item.delete()
            return redirect('/this_week')

    elif page == 'today':
        item = TodayItems.objects.get(id=pk)

        if request.method == 'POST':
            item.delete()
            return redirect('/today')

    return render(request, 'delete_item.html', {'item': item})


def done_task(request, pk):
    page = request.path.rsplit('/', 3)[-3]

    if page == 'this_week':
        item = ThisWeekItems.objects.filter(id=pk)
        item.update(chosen_item_type='Task Done')
        return redirect('/this_week')

    elif page == 'today':
        item = TodayItems.objects.filter(id=pk)
        item.update(chosen_item_type='Task Done')
        return redirect('/today')
