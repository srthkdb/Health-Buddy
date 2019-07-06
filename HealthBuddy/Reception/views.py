from django.shortcuts import render, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment
from Doctor.models import Doctor
from Patient.models import Patient
import datetime
from django.views.generic import TemplateView
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
class reception_home(TemplateView):
    template_name = ""
    
def create_appointment(request, app_id=None):
    template_name = ""
    receptionist = request.user.reception
    if app_id == None:
        app_form = AppointmentForm(request.POST or None)
    else:
        app = get_object_or_404(Appointment, pk=app_id)
        app_form = AppointmentForm(request.POST or None, instance=app)

    if app_form.is_valid():
        if app_id == None:
            a = app_form.save(commit=False)
            a.reqApproval = True
            a.patient = Patient.objects.get(pk=a.patient_roll)
            a.receptionist = receptionist
            a.dateNtime = datetime.datetime.now()
            a.save()

            return render(request, template_name, {'error_message': 'Appointment confirmed'})

        else:
            a = app_form.save(commit=False)
            a.reqApproval = True
            a.dateNtime = datetime.datetime.now()
            a.save()

            return render(request, template_name, {'error_message': 'Appointment confirmed'})

    return render(request, template_name, {'app_form' : app_form, 'error_message': 'Invalid'})
