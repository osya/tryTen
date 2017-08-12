#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'user', 'description')
        model = UserProfile

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Field('name', readonly=True),
                Field('user', readonly=True),
                Field('description', readonly=True),
        )
