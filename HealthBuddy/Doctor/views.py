from django.shortcuts import render, get_object_or_404
from .forms import *
from Patient.models import Patient
from .models import *
from seven.models import TestList
import datetime
from Reception.models import Appointment

#saves pres and renders reference form
def create_pres_return(request, patient_roll, pres_id=None):
    form_class_pres = PrescriptionForm
    form_class_med = PresMedicineForm
    template_name = 'Doctor/prescription_form.html'
    patient = get_object_or_404(Patient, pk=patient_roll)
    app = Appointment.objects.filter(patient=patient)
    form_class = CreateReferForm
    form = form_class(None)

    if pres_id == None:
        pres_form = form_class_pres(request.POST or None)
        med_form = form_class_med(request.POST or None)
    else:
        pres = get_object_or_404(Prescription, pk=pres_id)
        pres_form = form_class_pres(request.POST or None, instance=pres)
        med_form = form_class_med(request.POST or None)

    if pres_form.is_valid():
        if pres_id == None:
            current_time = datetime.datetime.now()
            p = pres_form.save(commit=False)
            p.date = current_time
            p.doctor = request.user.doctor
            p.patient = patient
            p.med_added = True
            p.save()

            return render(request, 'Doctor/reference_form.html',{'form': form})
        else:
            p = pres_form.save(commit=False)
            p.save()

            return render(request, 'Doctor/reference_form.html',{'form': form})
    return render(request, template_name,{'pres_form': pres_form, 'med_form': med_form, 'patient': patient, 'error_message': 'Error: Invalid form submission, cannot create reference'})


#delete appointment by filtering from patient and not by using app_id
def save_pres(request, patient_roll, pres_id=None, end=None):
    form_class_pres = PrescriptionForm
    form_class_med = PresMedicineForm
    template_name = 'Doctor/prescription_form.html'
    patient = get_object_or_404(Patient, pk=patient_roll)
    app = Appointment.objects.filter(patient=patient)

    if pres_id == None:
        pres_form = form_class_pres(request.POST or None)
        med_form = form_class_med(request.POST or None)
    else:
        pres = get_object_or_404(Prescription, pk=pres_id)
        pres_form = form_class_pres(request.POST or None, instance=pres)
        med_form = form_class_med(request.POST or None)

    if pres_form.is_valid():
        if pres_id == None:
            current_time = datetime.datetime.now()
            p = pres_form.save(commit=False)
            p.date = current_time
            p.doctor = request.user.doctor
            p.patient = patient
            p.med_added = True

            p.save()

            med_form = form_class_med(None)
            pres_form = form_class_pres(None)
            if end:
                app.delete()
            return render(request, template_name,
                          {'pres_form': pres_form, 'med_form': med_form, 'patient': patient, 'error_message': 'form saved'})
        else:
            p = pres_form.save(commit=False)
            p.save()


            med_form = form_class_med(None)
            pres_form = form_class_pres(None)
            if end:
                app.delete()
            return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'patient': patient, 'error_message': 'form saved'})


    return render(request, template_name,{'pres_form': pres_form, 'med_form': med_form, 'patient': patient})

def delete_med(request, patient_roll, pres_id, med_id):
    patient = get_object_or_404(Patient, pk=patient_roll)
    pres = get_object_or_404(Prescription, pk=pres_id)
    form_class_pres = PrescriptionForm
    form_class_med = PresMedicineForm
    template_name = 'Doctor/prescription_form.html'
    pres_form = form_class_pres(request.POST or None, instance=pres)
    med_form = form_class_med(None)
    med = PresMedicine.objects.get(pk=med_id)
    med.delete()
    if pres_form.is_valid():
        p = pres_form.save(commit=False)
        p.save()
        return render(request, template_name,
                      {'pres_form': pres_form, 'med_form': med_form, 'pres': p, 'patient': patient,
                       'error_message': 'Medicine removed'})

    return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'pres': pres, 'patient': patient,
                                           'error_message': 'Medicine removed'})

def add_med(request, patient_roll, pres_id=None):
    form_class_pres = PrescriptionForm
    form_class_med = PresMedicineForm
    template_name = 'Doctor/prescription_form.html'
    patient = get_object_or_404(Patient, pk = patient_roll)

    if pres_id == None:
        pres_form = form_class_pres(request.POST or None)
        med_form = form_class_med(request.POST or None)
    else:
        pres = get_object_or_404(Prescription, pk=pres_id)
        pres_form = form_class_pres(request.POST or None, instance=pres)
        med_form = form_class_med(request.POST or None)

    if pres_form.is_valid() and med_form.is_valid():
        if pres_id == None:
            current_time = datetime.datetime.now()
            p = pres_form.save(commit=False)
            p.date = current_time
            p.doctor = request.user.doctor
            p.patient = patient
            p.med_added = True
            p.app
            p.save()

            m = med_form.save(commit=False)
            m.prescription = p
            m.save()
            med_form = form_class_med(None)

            return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'pres': p, 'patient': patient, 'error_message': 'medicine added'})
        else:
            p = pres_form.save(commit=False)
            p.save()

            m = med_form.save(commit=False)
            m.prescription = p
            m.save()
            med_form = form_class_med(None)

            return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'pres': p, 'patient': patient, 'error_message': 'medicine added'})

    return render(request, template_name, {'pres_form': pres_form, 'med_form': med_form, 'patient': patient})

def create_reference(request, patient_roll, pres_id=None):
    form_class = CreateReferForm
    template_name = 'Doctor/prescription_form.html'
    form = form_class(request.POST or None)
    doctor = request.user.doctor
    patient = get_object_or_404(Patient, pk=patient_roll)
    if pres_id:
        pres = create_pres_return(request, patient_roll, pres_id)
    else:
        pres = create_pres_return(request, patient_roll, pres_id=None)

    if form.is_valid():
        r = form.save(commit=False)
        r.from_doc = doctor
        r.prescription = pres
        r.save()
