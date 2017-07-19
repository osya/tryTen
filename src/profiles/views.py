from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html', {})


def about(request):
    return render_to_response('about.html', {})


@login_required()
def user_profile(request):
    return render_to_response('profile.html', {'user': request.user})
