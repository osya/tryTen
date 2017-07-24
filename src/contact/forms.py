#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email', 'comment')
        model = Contact

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Field('name', required=True),
                Field('email', required=True),
                Field('comment', required=True),
                ButtonHolder(Submit('submit', 'Submit', css_class='btn btn-success'))
        )
