from django.urls import path, include
from . import views

app_name = "Reception"
urlpatterns = [
    # path('', views.ReceptionHome.as_view(), name="reception_home"),
    path('create/<int:app_id>/', views.create_appointment, name="create_appointment" ),
    path('create/', views.create_appointment, name="create_appointment_new"),
    path('clear/', views.clearList, name="clear"),
    path('patient_search/', views.pat_list, name="pat_list"),
    path('student_search/', views.stud_list, name="stud_list"),
    path('approve/<int:app_id>/', views.approve, name="approve")
]
