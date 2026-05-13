from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Availability(models.Model):

    medicine = models.CharField(max_length=200)

    pharmacy = models.ForeignKey(
        Pharmacy,
        on_delete=models.CASCADE
    )

    in_stock = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.medicine