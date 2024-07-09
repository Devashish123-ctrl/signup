from django.urls import path
from .views import signup_doctor,signup_patient, login_view, dashboard,check,logouts

urlpatterns = [
    path('signup/',check, name='signup'),
    path('login/', login_view, name='login'),
      path('logout/', logouts, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/doctor',signup_doctor, name='doctor'),
    path('signup/patient',signup_patient,name='patient')
]
