from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def user_profile(request):
    return render(request, 'profiles/profile.html', {'user': request.user})
