from django.db import models
from account.models import User
#from surdo.models import Consult
# Create your models here.
class Interpreter(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    cpf = models.BigIntegerField()
    librasFluence = models.IntegerField()
    cash = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = "interpreter"

#class RejectedConsults(models.Model):
    #consult = models.ForeignKey(Consult, on_delete=models.CASCADE)
    #interpreter = models.ForeignKey(Interpreter, on_delete=models.CASCADE)