from django.shortcuts import render
from django.http import HttpResponse

from .forms import UsernameForm


def home(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
			# return HttpResponse(
			# 	'Hello, {}! Today is going to be a great day!'.format(
			# 		form.cleaned_data['name'],
			# 	)
			# )

            greeting = form.cleaned_data['name']
            return render(request, "home.html", {'output': greeting})
        else:
            render(request, "home.html", {'form': form})
    else:
        form = UsernameForm()
    return render(request, "home.html", {'form': form})

def profile(request):
    return render(request, 'profile.html')

def key(request):
    return render(request, 'key.html')

def this_week(request):
    return render(request, 'this_week.html')

def today(request):
    return render(request, 'today.html')