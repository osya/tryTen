#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from .models import Good


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('name', 'description', 'category', 'in_stock', 'price',)

    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                'name', 'description', 'category', 'in_stock', 'price',
                ButtonHolder(
                        Submit('create', 'Create', css_class='btn btn-default')
                )
        )
