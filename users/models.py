from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    dob = models.DateField(max_length=8, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    mob_no = models.IntegerField(null=True, blank=True)

    def get_age(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return delta.years