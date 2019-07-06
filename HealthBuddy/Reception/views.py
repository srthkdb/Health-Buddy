from django.shortcuts import render, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment
from Doctor.models import Doctor
from Patient.models import Patient
import datetime
# List available doctors

'''
    Start a session
        a form where you enter user's username/roll/pf/name/ccusername and confirm

        assign the user a doctor and put the user in waitinglist

        gets the status of each patient on waiting list

        waiting list will show list of patients and corresponding doctors
        with 3 booleans: Doctor, pharmacy, room no 7 ( showing visited or not )
        and when the user leaves, his/her session will end.


'''

def create_appointment(request, patient_roll, doc_name, app_id=None):
    patient = get_object_or_404(Patient, pk=patient_roll)
    user = get_object_or_404(User, username=doc_name)

    if user.doctor:
        doctor = user.doctor
    else:
        pass
    template_name = ""

    if app_id == None:
        app_form = AppointmentForm(request.POST or None)
    else:
        app = get_object_or_404(Appointment, pk=app_id)
        app_form = AppointmentForm(request.POST or None, instance=app)

    if app_form.is_valid():
        if app_id == None:
            a = app_form.save(commit=False)
            a.reqApproval = True
            a.patient = patient
            a.doctor = doctor
            a.save()

            app_form = AppointmentForm(None)

            return render(request, template_name, {'app_form' : app_form, 'patient' : patient, doctor: 'doctor', 'error_message': 'Appointment confirmed'})

        else:
            a = app_form.save(commit=False)
            a.save()
            app_form = AppointmentForm(None)

            return render(request, template_name, {'app_form' : app_form, 'patient' : patient, doctor: 'doctor', 'error_message': 'Appointment confirmed'})

    return render(request, template_name, {'app_form' : app_form, 'patient' : patient, doctor: 'doctor', 'error_message': 'Invalid'})
