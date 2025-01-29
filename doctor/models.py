from django.db import models
from django.utils import timezone

from userauths import models as userauths_models


NOTIFICATION_TYPE = (
    ('New Appointments', 'New Appointments'),
    ('Appointments Cancelled',  'Appointments Cancelled'),
)


class Doctor(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete= models.CASCADE)
    image = models.FileField(upload_to='images', blank=True , null=True)
    full_name = models.CharField(max_length=100, blank=True, null= True)
    mobile = models.CharField(max_length=100, blank=True, null= True)
    country = models.CharField(max_length=100, blank=True, null= True)
    bio = models.CharField(max_length=100, blank=True, null= True)
    specialization = models.CharField(max_length=100, blank=True, null= True)
    qualification = models.CharField(max_length=100, blank=True, null= True)
    years_of_experience = models.CharField(max_length=100, blank=True, null= True)
    next_available_appointment_date = models.CharField(max_length=100, blank=True, null= True)
    
    
    def __str__(self):
        return f"Dr. {self.full_name}"
    
    
    
class Notification(models.Model):
    doctor = models.ForeignKey( Doctor, on_delete=models.SET_NULL, null= True, blank=True)
    appointment = models.ForeignKey("base.Appointment", on_delete=models.CASCADE , null= True, blank=True , related_name="doctor_appointment_notification")
    type =  models.CharField(max_length=100 ,choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Notification'
        
    def __str__(self):
        return f"Dr {self.doctor.full_name} Notification"
