from django.contrib import admin

from .models import ProfileDetails, Key


class ProfileAdmin(admin.ModelAdmin):
    model = ProfileDetails

class KeyAdmin(admin.ModelAdmin):
    model = Key

admin.site.register(ProfileDetails, ProfileAdmin)
admin.site.register(Key, KeyAdmin)
