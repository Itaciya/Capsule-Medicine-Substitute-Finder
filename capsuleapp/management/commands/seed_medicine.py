from django.core.management.base import BaseCommand
from capsuleapp.models import Generic, Medicine

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        paracetamol, created = Generic.objects.get_or_create(
            name="Paracetamol"
        )

        medicines = [
            ("Napa", "500mg", "Beximco"),
            ("Ace", "500mg", "Square"),
            ("Reset", "500mg", "Opsonin"),
            ("Pyrol", "500mg", "Renata"),
        ]

        for brand, strength, manufacturer in medicines:

            Medicine.objects.get_or_create(
                brand_name=brand,
                generic=paracetamol,
                strength=strength,
                manufacturer=manufacturer
            )

        self.stdout.write(
            self.style.SUCCESS("Medicine data seeded successfully")
        )