from django.contrib import admin
from .models import Profile, userStripe


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)


class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe


admin.site.register(userStripe, userStripeAdmin)
