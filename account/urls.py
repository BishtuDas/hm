from django.urls import path
from . import views
app_name='account'
urlpatterns = [
    path('', views.singup, name='singup'),
    path('dentist/', views.dentist, name='dentist'),
    path('dashboard/', views.customer, name='customer'),
    path('website/', views.website, name='website'),
    path('patient-profile/', views.patient_profile, name='patient_profile'),
    path('patient-change-password/', views.patient_password, name='patient_password'),
] 
