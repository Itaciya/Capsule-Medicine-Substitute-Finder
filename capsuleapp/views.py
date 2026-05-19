from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Availability


@api_view(['GET'])
def compare_prices(request, medicine_name):

    medicines = Availability.objects.filter(
        medicine__iexact=medicine_name,
        in_stock=True,
        price__isnull=False
    ).select_related('pharmacy').order_by('price')

    if not medicines.exists():
        return Response({
            "message": "No price data found"
        })

    cheapest = medicines.first()

    result = []

    for item in medicines:
        result.append({
            "medicine": item.medicine,
            "pharmacy": item.pharmacy.name,
            "location": item.pharmacy.location,
            "price": float(item.price),
            "is_cheapest": item.id == cheapest.id
        })

    return Response({
        "medicine": medicine_name,
        "cheapest_price": float(cheapest.price),
        "cheapest_pharmacy": cheapest.pharmacy.name,
        "comparisons": result
    })