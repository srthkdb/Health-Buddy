from users.models import Type
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User 
from django.views.generic import View
from .forms import PrescriptionForm, PresMedicineForm
from django.views.generic import TemplateView
from Patient.models import Patient
from .models import Prescription
import datetime

def create_prescription(request, patient_roll, pres_id=None):
    form_class_pres = PrescriptionForm
    form_class_med = PresMedicineForm
    template_name = 'doctor/prescription_form.html'
    patient = get_object_or_404(Patient, pk = patient_roll)

    if pres_id == None: 
        pres_form = form_class_pres(request.POST or None)
        med_form = form_class_med(request.POST or None)
    else:
        pres = get_object_or_404(Prescription, pk=pres_id)
        pres_form = form_class_pres(request.POST or None, instance=pres)
        med_form = form_class_med(request.POST or None)

    if request.POST and pres_form.is_valid() and med_form.is_valid():
        if pres_id == None:
            current_time = datetime.datetime.now()
            p = pres_form.save(commit=False)
            p.date = current_time
            p.doctor = request.user.doctor
            p.patient = patient
            p.med_added = True
            p.save()

            m = med_form.save(commit=False)
            m.prescription = p
            m.save()

            return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'pres': p, 'patient': patient})
        else:
            p = pres_form.save(commit=False)
            p.save()

            m = med_form.save(commit=False)
            m.prescription = p
            m.save()
            return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'pres': p, 'patient': patient})
        
        return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'patient': patient})
        
    return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'patient': patient})