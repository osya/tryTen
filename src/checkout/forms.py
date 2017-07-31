#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


class CheckoutForm(forms.Form):
    stripeToken = forms.CharField()
