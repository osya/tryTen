from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


@login_required()
def user_profile(request):
    return render(request, 'profile.html', {'user': request.user})
