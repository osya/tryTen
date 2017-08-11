#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from taggit_selectize.widgets import TagSelectize

from .models import Good


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('name', 'description', 'category', 'in_stock', 'price', 'tags',)
        widgets = {'tags': TagSelectize(), }

    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                'name', 'description', 'category', 'in_stock', 'price', 'tags',
                ButtonHolder(
                        Submit('submit', 'Submit', css_class='btn btn-default')
                )
        )
