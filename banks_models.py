from django.db import models
from users_models import User

class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=20)
    swift_bic = models.CharField(max_length=20)

    def __str__(self):
        return self.bank_name