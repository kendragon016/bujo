from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileDetails(models.Model):
    nickname = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    # models.ImageField from https://www.youtube.com/watch?v=ygzGr51dbsY&t=932s
    profile_pic = models.ImageField(default="images/defaultpic.png",
                                    upload_to='images/')


class Key(models.Model):
    key_name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)


class ThisWeekItems(models.Model):
    # https://www.youtube.com/watch?v=u7MJxv_P2Pk&t=615s for dropdown fields
    item_types = [
        ('Task', 'Task'),
        ('Event', 'Event'),
        ('Note', 'Note')
    ]
    chosen_item_type = models.CharField(max_length=10, choices=item_types)
    item_details = models.CharField(max_length=100)

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

    def get_absolute_url(self):
        return reverse('edit_today_item', args=[str(self.pk)])
