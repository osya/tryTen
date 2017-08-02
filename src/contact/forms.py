#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, help_text='100 characters max', required=True)
    email = forms.EmailField(max_length=100, required=True)
    comment = forms.CharField(max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                'name',
                'email',
                'comment',
                ButtonHolder(Submit('submit', 'Submit', css_class='btn btn-default'))
        )
