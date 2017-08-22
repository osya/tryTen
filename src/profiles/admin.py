from django.contrib import admin

from profiles.models import UserProfile, userStripe


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile


admin.site.register(UserProfile, ProfileAdmin)


class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe


admin.site.register(userStripe, userStripeAdmin)
