from django.urls import path
from . import views

app_name = "Patient"

urlpatterns = [
    path('pres/', views.myPres_details, name = "myPres_details"),
    path('pres/details/<int:pres_id>/', views.pres_details, name="pres_details"),
    path('details/<int:patient_roll>', views.pres_details, name='pat_details'),
    path('add_files/', views.create_file, name="create_file")
]
