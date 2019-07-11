from django.shortcuts import render, get_object_or_404, Http404,redirect
from Doctor.models import Prescription
from .models import Patient
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

@login_required(login_url = "/")
def create_file(request):
    form = PatHistoryForm(request.POST or None, request.FILES or None)
    patient = request.user.patient
    if form.is_valid():
            file = form.save(commit=False)
            file.patient = patient
            file.file = request.FILES['file']
            file.file_url = file.file.url

            file.save()
            return render(request, 'Patient/view_pres.html', {'patient': patient, 'form': form, 'error_message': 'File saved!'})
    return render(request, 'Patient/view_pres.html', {'patient': patient, 'form': form, 'error_message': 'Invalid form!'})


@login_required(login_url = "/")
def pres_details(request, pres_id=None):
    form = PatHistoryForm(request.POST or None, request.FILES or None)
    if pres_id:
        pres = get_object_or_404(Prescription, pk=pres_id)
        patient = pres.patient
        med = pres.presmedicine_set.all()
        tests = pres.tests.all()
        if request.POST:
            create_file(request)
        return render(request, 'Patient/view_pres.html',
                        {'patient': patient, 'pres': pres, 'med': med, 'tests': tests, 'form': form})

    else:
        if request.POST:
            create_file(request)
        patient = request.user.patient
        return render(request, 'Patient/view_pres.html', {'patient': patient, 'form': form})

@login_required(login_url = "/")
def requestAppointment(request, app_id=None):
    patient = request.user.patient
    template_name = "Patient/home_patient.html"
    if app_id == None:
        app_req_form = AppointmentRequestForm(request.POST or None)
    else:
        app = get_object_or_404(Appointment, pk=app_id)
        app_req_form = AppointmentRequestForm(request.POST or None, instance=app)
    if app_req_form.is_valid():
        if app_id:
            a = app_req_form.save(commit=False)
            a.dateNtime = datetime.datetime.now()
            a.reqApproved = False
            a.save()
        else:
            a = app_req_form.save(commit=False)
            a.patient = patient
            a.patient_roll = patient.rollNo
            a.dateNtime = datetime.datetime.now()
            a.reqApproved = False
            a.save()

        app_req_form = AppointmentRequestForm(None)
        return redirect('/home')
        
    app_req_form = AppointmentRequestForm(None)
        # return render(request, template_name, {'form' : app_req_form, 'error_message': "request sent"})
    return redirect('/home')
    # return render(request, template_name, {'form' : app_req_form, 'error_message' : "Invalid request"})

@login_required(login_url='/')
def Details(request, patient_roll):
    template_name = "Patient/profile.html"
    patient = get_object_or_404(Patient, pk=patient_roll)
    return render(request, template_name, {'patient' : patient})