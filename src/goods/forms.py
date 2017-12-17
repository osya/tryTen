#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Submit
from django import forms
from taggit_selectize.widgets import TagSelectize

from goods.models import Good


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
            FormActions(
                Submit('submit', 'Submit'),
                HTML('<a href="{% url "goods:goods:list" %}{% query_builder request %}">Go Back</a>')
            )
        )
