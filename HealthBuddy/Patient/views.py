from .models import Type
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.views.generic import View
from .forms import PatientRegForm
from django.http import HttpResponseRedirect

class PatientRegFormView(View):
    #Credits: code structure for this class is adapted from newboston django video tutorials.
    form_class = PatientRegForm
    template_name = 'users/pat_registration_form.html'

    #display blank form
    def get(self, request):
        if not request.user.is_authenticated:
            error_message = 'you are not autnenticated!'
            return render(request, 'users/registration_form.html', {'error_message': error_message})
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            if patient.is_dependent:
                if not patient.dependentUser:
                    error_message = 'please select a dependent user'
                    return return render(request, self.template_name, {'form': form, 'error_message': error_message})
                if not patient.dependentRelation:
                    error_message = 'please select a dependent relation'
                    return return render(request, self.template_name, {'form': form, 'error_message': error_message})
        #can fill rest of the data with student search
            patient.save()
            return render(request, 'users/patient_profile', {'patient': patient})
        return render(request, self.template_name, {'form': form})

