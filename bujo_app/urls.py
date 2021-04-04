from django.urls import path

from . import views

# from .views import ThisWeekView

urlpatterns = [
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('profile/edit/<int:pk>', views.edit_profile, name='edit_profile'),
    path('profile_pic/edit/<int:pk>', views.edit_pic, name='edit_pic'),
    path('key', views.key, name='key'),
    path('this_week', views.this_week, name='this_week'),
    path('this_week/edit/<int:pk>', views.edit_week_item, name='edit_week_item'),
    path('this_week/delete/<int:pk>', views.delete_week_item, name='delete_week_item'),
    # path('this_week/done/<int:pk>', views.done_task, name='delete_item'),
    path('today', views.today, name='today'),
    path('today/edit/<int:pk>', views.edit_today_item, name='edit_today_item'),
    path('today/delete/<int:pk>', views.delete_today_item, name='delete_today_item'),
    # path('all_keys', KeyListView.as_view(), name="key_list")
]
