from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from profiles.forms import ProfileForm


class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'profiles/profile_detail.html'
    form_class = ProfileForm

    def get_object(self):
        profile = get_user_model().objects.get(pk=self.request.session['_auth_user_id']).userprofile
        return ProfileForm(instance=profile)
