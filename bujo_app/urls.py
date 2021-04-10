from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/<int:pk>', views.edit_profile, name='edit_profile'),
    path('profile_pic/edit/<int:pk>', views.edit_pic, name='edit_pic'),
    path('key', views.key, name='key'),
    path('this_week', views.this_week, name='this_week'),
    path('this_week/edit/<int:pk>',
         views.edit_item,
         name='edit_week_item'),
    path('this_week/delete/<int:pk>',
         views.delete_item,
         name='delete_week_item'),
    path('this_week/done/<int:pk>',
         views.done_task,
         name='done_week_task'),
    path('today', views.today, name='today'),
    path('today/edit/<int:pk>', views.edit_item, name='edit_today_item'),
    path('today/delete/<int:pk>',
         views.delete_item,
         name='delete_today_item'),
    path('today/done/<int:pk>', views.done_task, name='done_today_task'),
]
