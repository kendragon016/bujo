from django.contrib import admin

from .models import ProfileDetails, Key, ThisWeekItems, TodayItems


class ProfileAdmin(admin.ModelAdmin):
    model = ProfileDetails

class KeyAdmin(admin.ModelAdmin):
    model = Key

class ThisWeekAdmin(admin.ModelAdmin):
    model = ThisWeekItems

class TodayAdmin(admin.ModelAdmin):
    model = TodayItems

admin.site.register(ProfileDetails, ProfileAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(ThisWeekItems, ThisWeekAdmin)
admin.site.register(TodayItems, TodayAdmin)
