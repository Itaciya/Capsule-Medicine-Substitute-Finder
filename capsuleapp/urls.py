# capsuleapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('medicine/<slug:slug>/', views.medicine_detail, name='medicine_detail'),
    path('alternatives/<slug:slug>/', views.alternatives, name='alternatives'),
    path('compare/<slug:slug>/', views.compare_medicines, name='compare'),
    path('pharmacies/<slug:slug>/', views.nearby_pharmacies, name='nearby_pharmacies'),

    path('search/', views.search_medicines, name='search'),
    path('favorite/<int:med_id>/', views.toggle_favorite, name='toggle_favorite'),
]