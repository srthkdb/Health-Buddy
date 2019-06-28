from .models import Type
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.views.generic import View
from .forms import PatientRegForm
from django.http import HttpResponseRedirect



