#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'
