from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import IndexCardForm


class HomePageView(View):
	def get(self, request):
		return HttpResponse('Hello World! This came from the index view.')


def index_card_view(request):
	if request.method == 'POST':
		form = IndexCardForm(request.POST)
		if form.is_valid():
			return HttpResponse(
				'You are from {} section {}'.format(
					form.cleaned_data['name'],
					form.cleaned_data['section']
				)
			)
		else:
			render(request, "index.html", {'form': form})
	else:
	    form = IndexCardForm()
	return render(request, "index.html", {'form': form})