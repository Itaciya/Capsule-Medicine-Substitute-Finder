from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    generic_name = serializers.CharField(source='generic.name')

    class Meta:
        model = Medicine
        fields = [
            'id',
            'brand_name',
            'generic_name',
            'strength',
            'manufacturer'
        ]