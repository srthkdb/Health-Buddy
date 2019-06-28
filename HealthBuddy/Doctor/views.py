from users.models import Type
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User 
from django.views.generic import View
from .forms import PrescriptionForm, PresMedicineForm
from django.views.generic import TemplateView
from Patient.models import Patient
import datetime

def add_med(request):
    temp_pres = request.user.doctor.temppres.prescription
    form_class_med = PresMedicineForm


def create_prescription(request, patient_id):
    form_class_pres = PrescriptionForm
    form_class_med = PresMedicineForm
    template_name = 'users/prescription_form.html'

    pres_form = self.form_class_pres(request.POST or None)
    med_form = self.form_class_med(request.POST or None)
    current_time = datetime.datetime.now()

    if form.is_valid():
        p = pres_form.save(commit=False)
        m = med_form.save(commit=False)
        p.date = current_time
        p.doctor = request.user.doctor
        p.patient = get_object_or_404(Patient, pk=patient_id)
        p.save()

        m.prescription = p
        m.save()

    return render(request, self.template_name, {'form': form})