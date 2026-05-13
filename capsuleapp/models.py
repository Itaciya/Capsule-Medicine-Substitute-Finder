from django.db import models

class Generic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    brand_name = models.CharField(max_length=255)
    generic = models.ForeignKey(Generic, on_delete=models.CASCADE)
    strength = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.brand_name