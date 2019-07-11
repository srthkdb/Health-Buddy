from django.urls import path, include
from . import views

app_name = "Reception"
urlpatterns = [
    # path('', views.ReceptionHome.as_view(), name="reception_home"),
    path('create/<int:app_id>/', views.create_appointment, name="create_appointment" ),
    path('create/', views.create_appointment, name="create_appointment_new"),
    path('clear/', views.clearList, name="clear"),
]
