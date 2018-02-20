#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout
from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    class Meta:
        fields = (
            'username',
            'email',
            'description',
            'city',
            'website',
            'phone_number',
        )
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username', readonly=True),
            Field('email', readonly=True),
            Field('description', readonly=True),
            Field('city', readonly=True),
            Field('website', readonly=True),
            Field('phone_number', readonly=True),
        )


# TODO: Think is it possible to use UserChangeForm for ProfileForm
