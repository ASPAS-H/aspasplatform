from django.db import models
from account.models import User
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