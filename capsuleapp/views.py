from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rapidfuzz import fuzz

from .models import Medicine
from .serializers import MedicineSerializer


# WEBSITE PAGES

def home(request):
    return render(request, 'capsuleapp/home.html')


def register(request):
    return render(request, 'capsuleapp/register.html')


def dashboard(request):
    return render(request, 'capsuleapp/dashboard.html')


# API

@api_view(['GET'])
def search_medicine(request):

    query = request.GET.get('q', '')

    medicines = Medicine.objects.all()

    matched = []

    for med in medicines:

        score = fuzz.ratio(
            query.lower(),
            med.brand_name.lower()
        )

        if query.lower() in med.brand_name.lower() or score > 60:
            matched.append(med)

    serializer = MedicineSerializer(matched, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def alternatives(request, medicine_id):

    medicine = Medicine.objects.get(id=medicine_id)

    alternatives = Medicine.objects.filter(
        generic=medicine.generic
    ).exclude(id=medicine.id)

    serializer = MedicineSerializer(
        alternatives,
        many=True
    )

    return Response({
        "searched_medicine": MedicineSerializer(medicine).data,
        "alternatives": serializer.data
    })