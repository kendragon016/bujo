from django.urls import path

from . import views

from .views import KeyListView

urlpatterns = [
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('key', views.key, name='key'),
    path('this_week', views.this_week, name='this_week'),
    path('today', views.today, name='today'),
    path('all_keys', KeyListView.as_view(), name="key_list")
]
