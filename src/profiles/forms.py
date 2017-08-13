#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('user', 'description', 'city', 'website', 'phone_number',)
        model = UserProfile

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Field('name', readonly=True),
                Field('user', readonly=True),
                Field('description', readonly=True),
                Field('city', readonly=True),
                Field('website', readonly=True),
                Field('phone_number', readonly=True),
        )
# TODO: Think is it possible to use UserChangeForm for ProfileForm
