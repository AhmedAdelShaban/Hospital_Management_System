from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from doctor import models as doctor_models
from base import models as base_models

# Create your views here.
@login_required
def dashboard(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)
    notifications = doctor_models.Notification.objects.filter(doctor=doctor)
    
    context ={
        'appointments': appointments,
        'notifications': notifications,
        'doctor':doctor
    }
    
    return render(request,'doctor/dashboard.html',context)



@login_required
def appointment(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)

    
    context ={
        'appointments': appointments,
    }
    
    return render(request,'doctor/appointment.html',context)

@login_required
def appointment_detail(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    medical_record = base_models.MedicalRecord.objects.filter(appointment_id=appointment_id)
    lab_test = base_models.LabTest.objects.filter(appointment_id=appointment_id)
    prescription = base_models.Prescription.objects.filter(appointment_id=appointment_id)

    
    context ={
        'appointment': appointment,
        'medical_record': medical_record,
        'lab_test': lab_test,
        'prescription': prescription,
    }
    
    return render(request,'doctor/appointment_detail.html',context)