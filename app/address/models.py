from django.db import models

# Create your models here.
class Address(models.Model):

    street = models.CharField(max_length=255)
    vile = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipCode = models.IntegerField()
    complement = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "addresses"

