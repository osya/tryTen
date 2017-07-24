#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class AboutPageView(generic.TemplateView):
    template_name = 'about.html'
