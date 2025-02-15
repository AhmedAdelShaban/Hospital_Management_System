from django.urls import path
from doctor import views


app_name = 'doctor'

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('appointment/',views.appointment, name='appointment'),
    path('appointment/<appointment_id>/',views.appointment_detail, name='appointment_detail'),
    
    
    path('cancel_appointment/<appointment_id>/',views.cancel_appointment, name='cancel_appointment'),
    path('activate_appointment/<appointment_id>/',views.activate_appointment, name='activate_appointment'),
    path('completed_appointment/<appointment_id>/',views.completed_appointment, name='completed_appointment'),
]
