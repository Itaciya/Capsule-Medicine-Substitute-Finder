# capsuleapp/admin.py
from django.contrib import admin
from .models import Medicine, Pharmacy, PharmacyInventory, Favorite

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'generic_name', 'manufacturer', 'price', 'strength')
    list_filter = ('category', 'manufacturer')
    search_fields = ('name', 'generic_name')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Pharmacy)
admin.site.register(PharmacyInventory)
admin.site.register(Favorite)