from django.db import models
from account.models import User
from hospital.models import Hospital
from interpreter.models import Interpreter
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
    STATUS = [(0, 'PENDING'), (1, 'AWAITING_INTERPRETER'), (2, 'SCHEDULED'), (3, 'FINISHED'), (4, 'CANCELED')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date1 = models.DateField()
    date2 = models.DateField()
    date3 = models.DateField()
    modelity = models.IntegerField(choices = MODELITY_TYPES)
    status = models.IntegerField(choices= STATUS)
    observations = models.TextField(null = True)
    interpreter = models.ForeignKey(Interpreter, on_delete=models.CASCADE, null=True)
    confirmed_date = models.DateField(null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta():
        db_table = "consults"
    
    def getStringStatus(self):
        status = {
            0: "AGUARDANDO HOSPITAL",
            1: "AGUARDANDO INTERPRETE",
            2: "AGENDADA",
            3: "FINALIZADA",
            4: "CANCELADA"
        }
        return status[self.status]
    
    def getModelity(self):
        status = {
            0: "PRESENCIAL",
            1: "TELEMEDICINA"
        }
        return status[self.modelity]
