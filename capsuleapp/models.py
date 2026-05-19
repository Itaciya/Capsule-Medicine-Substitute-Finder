# capsuleapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    generic_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    strength = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    uses = models.TextField(blank=True)
    dosage = models.TextField(blank=True)
    side_effects = models.TextField(blank=True)
    warnings = models.TextField(blank=True)
    storage = models.TextField(blank=True)
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)
    popularity_score = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.strength})"

class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PharmacyInventory(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    price_at_pharmacy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('pharmacy', 'medicine')

    def __str__(self):
        return f"{self.medicine.name} at {self.pharmacy.name}"

# Optional: User favorites
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'medicine')