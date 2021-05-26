from django.db import models
from account.models import User
from hospital.models import Hospital
# Create your models here.
class Deaf(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    cpf = models.BigIntegerField()
    health_plan = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = "deafs"
class Consult(models.Model):
    MODELITY_TYPES = [(0, 'LOCAL'), (1, 'VIRTUAL')]
    STATUS = [(0, 'PENDING'), (1, 'AWAITING_INTERPRETER'), (2, 'SCHEDULED'), (3, 'FINISHED')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date1 = models.DateField()
    date2 = models.DateField()
    date3 = models.DateField()
    modelity = models.IntegerField(choices = MODELITY_TYPES)
    status = models.IntegerField(choices= STATUS)
    observations = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta():
        db_table = "consults"