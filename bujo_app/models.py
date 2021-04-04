from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileDetails(models.Model):
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    # models.ImageField from https://www.youtube.com/watch?v=ygzGr51dbsY&t=932s
    profile_pic = models.ImageField(default="/static/images/userpic.png", upload_to='images/')

    def __str__(self):
        return f'{self.nickname} Profile'

    # def get_absolute_url(self):
    #     return reverse('profiledetails_detail', args=[str(self.pk)])

    # @property
    # def is_tutorial(self):
    #     return self.bio == 1

class Key(models.Model):
    key_name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.key_name} {self.description}'

class ThisWeekItems(models.Model):
    item_types = [
        ('Task', 'Task'),
        ('Event', 'Event'),
        ('Note', 'Note')
    ]
    chosen_item_type = models.CharField(max_length=10, choices=item_types)
    item_details = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.chosen_item_type} {self.item_details}'

    def get_absolute_url(self):
        return reverse('edit_week_item', args=[str(self.pk)])


class TodayItems(models.Model):
    item_types = [
        ('Task', 'Task'),
        ('Event', 'Event'),
        ('Note', 'Note'),
    ]
    chosen_item_type = models.CharField(max_length=10, choices=item_types)
    item_details = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.chosen_item_type} {self.item_details}'

    def get_absolute_url(self):
        return reverse('edit_today_item', args=[str(self.pk)])