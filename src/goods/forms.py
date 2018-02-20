#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FieldWithButtons, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout, Submit
from django import forms
from django.urls import reverse
from taggit_selectize.widgets import TagSelectize

from goods.models import Good


class SearchForm(forms.Form):
    query = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_action = reverse('goods:goods:list')
        self.helper.form_class = 'navbar-form navbar-left'
        self.helper.attrs = {'role': 'search'}
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(FieldWithButtons(Field('query', autofocus='autofocus'), Submit('', 'Search')))


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = (
            'name',
            'description',
            'category',
            'in_stock',
            'price',
            'tags',
        )
        widgets = {
            'tags': TagSelectize(),
        }

    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name', 'description', 'category', 'in_stock', 'price', 'tags',
            FormActions(
                Submit('submit', 'Submit'),
                HTML('<a href="{% url "goods:goods:list" %}{% query_builder request %}">Go Back</a>')))
