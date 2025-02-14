from django.urls import path
from doctor import views


app_name = 'doctor'

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('appointment/',views.appointment, name='appointment'),
    path('appointment/<appointment_id>/',views.appointment_detail, name='appointment_detail'),
]
