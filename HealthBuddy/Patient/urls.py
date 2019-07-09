from django.urls import path
from . import views

app_name = "Patient"

urlpatterns = [
    path('pres/details/<int:pres_id>/', views.pres_details, name="pres_details"),
    path('pres/', views.pres_details, name="pres_details_new"),
    path('details/<int:patient_roll>', views.pres_details, name='pat_details'),
    path('add_files/', views.create_file, name="create_file"),
    path('request/', views.requestAppointment, name = "request_new"),
    path('request/<int:app_id>', views.requestAppointment, name = "request"),
    # path('myprofile, views.')
]
