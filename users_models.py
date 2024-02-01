from django.db import models
from banks_models import Bank

class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    banks = models.ManyToManyField(Bank, related_name='users')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
