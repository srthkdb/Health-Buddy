from django.shortcuts import render, get_object_or_404, Http404
from Doctor.models import Prescription
from .models import Patient
from .forms import PatHistoryForm
import datetime

def myPres_details(request):
        prescriptions = Prescription.objects.filter(patient=request.user.patient)
        return render(request, 'Patient/myPrescriptions.html', {'prescriptions': prescriptions})

def pres_details(request, pres_id=None, patient_roll=None):
        if pres_id:
                pres = get_object_or_404(Prescription, pk=pres_id)
                patient = pres.patient
                med = pres.presmedicine_set.all()
                tests = pres.tests.all()
                return render(request, 'Patient/view_pres.html',
                              {'patient': patient, 'pres': pres, 'med': med, 'tests': tests})

        else:
                patient = get_object_or_404(Patient, rollNo=patient_roll)
                return render(request, 'Patient/view_pres.html', {'patient': patient})


def create_file(request):
        form = PatHistoryForm(request.POST or None, request.FILES or None)
        patient = request.user.patient
        if form.is_valid():
                file = form.save(commit=False)
                file.patient = patient
                file.file = request.FILES['file']
                file.file_url = file.file.url

                file.save()
                return render(request, 'Patient/view_pres.html', {'patient': patient, 'error_message': 'File saved successfully!'})

        return render(request, 'Patient/patHistory_form.html', {'form': form})

def requestAppointment(request):
    app_form = AppointmentRequestForm(request.POST or None)
    patient = request.user.patient
    user = get_object_or_404(User, username=pref_doc)
    template_name = ""

    if user.doctor:
        doctor = user.doctor
    else:
        return render(request, template_name, {})

    if app_form.is_valid():
        a = app_form.save(commit=False)
        a.patient = patient
        a.doctor = doctor
        a.dateNtime = datetime.datetime.now()
        a.save()

        return render(request, template_name, {})

    return render(request, template_name, {})
