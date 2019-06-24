from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('healthcalc', views.Calc.as_view(), name = "calc"),
    path('contact_us', views.Contact.as_view(), name = "contact"),
    path('profile', views.Profile.as_view(), name = "profile" )
]
