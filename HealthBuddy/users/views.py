from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "users/base_home.html"

class Calc(TemplateView):
    template_name = "users/health_calc.html"

class Contact(TemplateView):
    template_name = "users/contact_us.html"

class Profile(TemplateView):
    template_name = "users/Profile.html"