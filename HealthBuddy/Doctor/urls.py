from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "Doctor"

urlpatterns = [
    path('pres/<int:patient_roll>/', views.create_prescription, name = "create_prescription"),
    path('pres/<int:patient_roll>/<int:pres_id>/', views.create_prescription, name = "change_prescription"),
    #url(r'^pres/(?P<patient_roll>[0-9]+)/$', views.create_prescription, name="create_prescription"),
    #url(r'^pres/(?P<patient_roll>[0-9]+)/(?P<pres_id>[0-9]+)/$', views.create_prescription, name="change_prescription"),

]
