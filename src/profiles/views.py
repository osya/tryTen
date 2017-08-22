from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from profiles.forms import UserForm


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profiles/profile_detail.html'
    form_class = UserForm

    def get_object(self):
        user = get_user_model().objects.get(pk=self.request.session['_auth_user_id'])
        return UserForm(instance=user)
