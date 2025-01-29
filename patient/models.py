from django.db import models
from django.utils import timezone

from userauths import models as userauths_models


NOTIFICATION_TYPE = (
    ('Appointments Scheduled ', 'Appointments Scheduled'),
    ('Appointments Cancelled',  'Appointments Cancelled'),
)


class Patient(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete= models.CASCADE)
    image = models.FileField(upload_to='images', blank=True , null=True)
    full_name = models.CharField(max_length=100, blank=True, null= True)
    email = models.CharField(max_length=100, blank=True, null= True)
    mobile  = models.CharField(max_length=100, blank=True, null= True)
    address= models.CharField(max_length=100, blank=True, null= True)
    gender = models.CharField(max_length=100, blank=True, null= True)
    blood_group = models.CharField(max_length=100, blank=True, null= True)
    dob = models.CharField(max_length=100, blank=True, null= True) 
    
    
    def __str__(self):
        return f"{self.full_name}"
    
    
    
class Notification(models.Model):
    patient = models.ForeignKey( Patient, on_delete=models.SET_NULL, null= True, blank=True)
    appointment = models.ForeignKey("base.Appointment", on_delete=models.CASCADE , null= True, blank=True , related_name="patient_appointment_notification")
    type =  models.CharField(max_length=100 ,choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Notification'
        
    def __str__(self):
        return f"{self.patient.full_name} Notification"