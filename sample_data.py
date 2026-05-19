import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capsule.settings')
django.setup()

from capsuleapp.models import Medicine, Pharmacy, PharmacyInventory

def create_sample_data():
    # Sample Medicines
    medicines = [
        {
            "name": "Napa", "generic_name": "Paracetamol", "manufacturer": "Beximco",
            "category": "Pain Relief", "strength": "500mg", "price": 2.50,
            "description": "Effective pain and fever reducer", "popularity_score": 95
        },
        {
            "name": "Seclo", "generic_name": "Omeprazole", "manufacturer": "Square",
            "category": "Gastric", "strength": "20mg", "price": 8.00,
            "description": "Reduces stomach acid", "popularity_score": 88
        },
        {
            "name": "Montair", "generic_name": "Montelukast", "manufacturer": "Incepta",
            "category": "Allergy", "strength": "10mg", "price": 15.00,
            "description": "For asthma and allergies", "popularity_score": 82
        },
        {
            "name": "Maxpro", "generic_name": "Esomeprazole", "manufacturer": "Square",
            "category": "Gastric", "strength": "40mg", "price": 12.00,
            "description": "Advanced acid reducer", "popularity_score": 85
        },
    ]

    for data in medicines:
        med, created = Medicine.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"✅ Added: {med.name}")
        else:
            print(f"Already exists: {med.name}")

    # Sample Pharmacies
    ph1 = Pharmacy.objects.create(name="Pharmacy One", address="Dhanmondi, Dhaka", latitude=23.746, longitude=90.374, contact="01711-123456")
    ph2 = Pharmacy.objects.create(name="Life Care Pharmacy", address="Gulshan, Dhaka", latitude=23.792, longitude=90.416, contact="01822-987654")

    # Link medicines to pharmacies
    for med in Medicine.objects.all():
        PharmacyInventory.objects.get_or_create(pharmacy=ph1, medicine=med, stock=100, price_at_pharmacy=med.price)
        PharmacyInventory.objects.get_or_create(pharmacy=ph2, medicine=med, stock=80, price_at_pharmacy=med.price+1)

    print("🎉 Sample data added successfully!")

if __name__ == "__main__":
    create_sample_data()