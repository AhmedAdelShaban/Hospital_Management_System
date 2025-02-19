from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    medical_records = base_models.MedicalRecord.objects.filter(appointment=appointment)
    lab_test = base_models.LabTest.objects.filter(appointment=appointment)
    prescription = base_models.Prescription.objects.filter(appointment=appointment)

    
    context ={
        'appointment': appointment,
        'medical_records': medical_records,
        'lab_test': lab_test,
        'prescription': prescription,
        
    }
    
    return render(request,'doctor/appointment_detail.html',context)

@login_required
def cancel_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)  
    
    appointment.status = 'Cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled successfully')
    
    return redirect('doctor:appointment_detail', appointment.appointment_id)  


@login_required
def activate_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)  
    
    appointment.status = 'Scheduled'
    appointment.save()
    messages.success(request, 'Appointment Re-Scheduled successfully')
    
    return redirect('doctor:appointment_detail', appointment.appointment_id) 

@login_required
def completed_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)  
    
    appointment.status = 'Completed'
    appointment.save()
    messages.success(request, 'Appointment Completed successfully')
    
    return redirect('doctor:appointment_detail', appointment.appointment_id) 

@login_required
def add_medical_report(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    
    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        treatment = request.POST.get('treatment')
        
        base_models.MedicalRecord.objects.create(appointment=appointment , diagnosis=diagnosis ,treatment=treatment)
    
    messages.success(request, 'Medical Report added successfully')
    return redirect('doctor:appointment_detail', appointment.appointment_id)     
        
@login_required
def edit_medical_report(request, appointment_id , medical_report_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    medical_report = base_models.MedicalRecord.objects.get(id=medical_report_id ,appointment=appointment)
    
    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        treatment = request.POST.get('treatment')
        
        medical_report.diagnosis = diagnosis
        medical_report.treatment = treatment
        medical_report.save()
        

    
    messages.success(request, 'Medical Report Updated successfully')
    return redirect('doctor:appointment_detail', appointment.appointment_id) 

@login_required
def add_lab_test(request,appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    
    
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        description = request.POST.get('description')
        result = request.POST.get('result')
        
        base_models.LabTest.objects.create(appointment=appointment , test_name=test_name , description=description ,result=result)
    
    
    messages.success(request, 'Lab report Added  successfully')
    return redirect('doctor:appointment_detail', appointment.appointment_id) 



@login_required
def edit_lab_test(request,appointment_id ,lab_test_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    lab_test = base_models.LabTest.objects.get(id=lab_test_id,appointment=appointment)
    
    
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        description = request.POST.get('description')
        result = request.POST.get('result')
        
        lab_test.test_name = test_name
        lab_test.description = description
        lab_test.result = result
        
        lab_test.save()
    
    
    messages.success(request, 'Lab report Updated  successfully')
    return redirect('doctor:appointment_detail', appointment.appointment_id) 


@login_required
def add_prescription(request,appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    
    if request.method == 'POST':
        medications = request.POST.get('medications')
        base_models.Prescription.objects.create(medications=medications , appointment=appointment)
    
    messages.success(request, 'Prescription Added  successfully')
    return redirect('doctor:appointment_detail', appointment.appointment_id)    

@login_required
def edit_prescription(request,appointment_id , prescription_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id ,doctor=doctor)
    prescription = base_models.Prescription.objects.get(id=prescription_id,appointment=appointment)
    if request.method == 'POST':
        medications = request.POST.get('medications')
        
        prescription.medications = medications
        prescription.save()
    
    messages.success(request, 'Prescription Updated  successfully')
    return redirect('doctor:appointment_detail', appointment.appointment_id) 

@login_required
def payments(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    payment = base_models.Billing.objects.filter(appointment__doctor=doctor)
    
    
    context={
        'payment': payment,
        'doctor':doctor
    }
    
    return render(request, 'doctor/payment.html', context)

@login_required
def notifications(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    notifications = doctor_models.Notification.objects.filter(doctor=doctor , seen=False)
    
    context ={
        'notifications': notifications,
       
    }
    
    return render(request, 'doctor/notifications.html', context)

@login_required
def mark_noti_seen(request , id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    notification = doctor_models.Notification.objects.get(doctor=doctor , id=id)
    notification.seen = True
    notification.save()
    
    messages.success(request, 'Notification Mark Seen')
    return redirect('doctor:notifications')

@login_required
def profile(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    formatted_next_available_appointment_date = doctor.next_available_appointment_date.strftime('%Y-%m-%d')    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        image = request.FILES.get('image')
        mobile = request.POST.get('mobile')
        country = request.POST.get('country')
        bio = request.POST.get('bio')
        specialization = request.POST.get('specialization')
        qualification = request.POST.get('qualification')
        years_of_experience = request.POST.get('years_of_experience')
        next_available_appointment_date = request.POST.get('next_available_appointment_date')
            
        doctor.full_name = full_name
        doctor.mobile = mobile
        doctor.country = country
        doctor.bio = bio
        doctor.specialization = specialization
        doctor.qualification = qualification
        doctor.years_of_experience = years_of_experience
        doctor.next_available_appointment_date = next_available_appointment_date
        
        if image != None:
            doctor.image = image
            
        doctor.save()
        messages.success(request,'Profile Updated Successfully')
        return redirect('doctor:profile')
    
    context ={
        'doctor':doctor,
        "formatted_next_available_appointment_date": formatted_next_available_appointment_date,
        
    }
    return render(request,'doctor/profile.html',context)