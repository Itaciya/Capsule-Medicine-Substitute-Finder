from django.db import models

# Create your models here.
class Medicine(models.Model):
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.brand_name

    def __str__(self):
        return self.generic_name