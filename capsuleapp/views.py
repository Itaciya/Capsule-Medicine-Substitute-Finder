# capsuleapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Medicine, PharmacyInventory, Favorite
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    popular = Medicine.objects.order_by('-popularity_score')[:8]
    return render(request, 'dashboard.html', {'popular': popular})

def medicine_detail(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, medicine=medicine).exists()
    return render(request, 'medicine_detail.html', {
        'medicine': medicine,
        'is_favorite': is_favorite
    })

def alternatives(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    alts = Medicine.objects.filter(
        generic_name=medicine.generic_name
    ).exclude(id=medicine.id)
    return render(request, 'alternatives.html', {
        'medicine': medicine,
        'alternatives': alts
    })

def compare_medicines(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    alts = Medicine.objects.filter(generic_name=medicine.generic_name).exclude(id=medicine.id)[:5]
    return render(request, 'compare.html', {
        'original': medicine,
        'alternatives': alts
    })

@login_required
def nearby_pharmacies(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    inventory = PharmacyInventory.objects.filter(medicine=medicine).select_related('pharmacy')
    return render(request, 'pharmacies.html', {
        'medicine': medicine,
        'inventory': inventory
    })

def search_medicines(request):
    query = request.GET.get('q', '')
    results = Medicine.objects.none()
    if query:
        results = Medicine.objects.filter(
            Q(name__icontains=query) |
            Q(generic_name__icontains=query) |
            Q(manufacturer__icontains=query)
        )
    return render(request, 'search_results.html', {'results': results, 'query': query})

@login_required
def toggle_favorite(request, med_id):
    medicine = get_object_or_404(Medicine, id=med_id)
    fav, created = Favorite.objects.get_or_create(user=request.user, medicine=medicine)
    if not created:
        fav.delete()
    return redirect('medicine_detail', slug=medicine.slug)

@login_required
def dashboard(request):
    popular = Medicine.objects.order_by('-popularity_score')[:8]
    return render(request, 'dashboard.html', {'popular': popular})

def medicine_detail(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, medicine=medicine).exists()
    return render(request, 'medicine_detail.html', {
        'medicine': medicine,
        'is_favorite': is_favorite
    })

def alternatives(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    alts = Medicine.objects.filter(
        generic_name=medicine.generic_name
    ).exclude(id=medicine.id)
    return render(request, 'alternatives.html', {
        'medicine': medicine,
        'alternatives': alts
    })

def compare_medicines(request, slug):
    medicine = get_object_or_404(Medicine, slug=slug)
    alts = Medicine.objects.filter(generic_name=medicine.generic_name).exclude(id=medicine.id)[:5]
    return render(request, 'compare.html', {
        'original': medicine,
        'alternatives': alts
    })