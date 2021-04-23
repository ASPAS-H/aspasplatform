from django.db import models

# Create your models here.
class Deaf(models.Model):

    name = models.CharField(max_length=255)
    born_date = models.DateField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    address = models.IntegerField()
    phone = models.CharField(max_length=14)
    cpf = models.IntegerField()
    health_plan = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)