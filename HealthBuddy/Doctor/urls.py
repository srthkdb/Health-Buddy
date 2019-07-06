from django.urls import path
from . import views

app_name = "Doctor"

urlpatterns = [
    path('pres/<int:patient_roll>/', views.add_med, name="create_prescription"),
    path('pres/<int:patient_roll>/<int:pres_id>/', views.add_med, name="change_prescription"),
    path('pres/save/<int:patient_roll>/<int:pres_id>/', views.save_pres, name="save_pres"),
    path('pres/save/<int:patient_roll>/', views.save_pres, name="save_pres_new"),
    path('pres/<int:patient_roll>/<int:pres_id>/delete_med/<int:med_id>', views.delete_med, name="delete_med"),
    path('pres/save/<int:patient_roll>/<int:pres_id>/<int:end>/', views.save_pres, name="save_and_end"),
    path('pres/refer/<int:patient_roll>/<int:pres_id>/', views.create_pres_return, name="refer"),
    path('pres/refer/<int:patient_roll>/', views.create_pres_return, name="refer_new"),
    path('pres/create_reference/<int:patient_roll>/<int:pres_id>/', views.create_reference, name="create_reference"),
]
