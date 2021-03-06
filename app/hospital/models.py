from django.db import models
from account.models import User
from address.models import Address

# Create your models here.

class Hospital(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cnpj = models.BigIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = "hospitals"

class HospitalStaff(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "hospital_staff"