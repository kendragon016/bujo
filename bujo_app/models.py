from django.db import models
from django.urls import reverse

class ProfileDetails(models.Model):
    nickname = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return 'Name: {}\nBio: {}'.format(self.nickname, self.bio)

    def get_absolute_url(self):
        return reverse('profiledetails_detail', args=[str(self.pk)])

    @property
    def is_tutorial(self):
        return self.bio == 1

class ProfilePic(models.Model):
    # models.ImageField from https://www.youtube.com/watch?v=ygzGr51dbsY&t=932s
    profile_pic = models.ImageField(null = True, blank = True, upload_to="../static/css/images/")

class Key(models.Model):
    key_name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.key_name} {self.description}'