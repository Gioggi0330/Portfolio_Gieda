from django.urls import path
from . import views

urlpatterns = [
    path('aggiungi/', views.aggiungi_libro, name='aggiungi_libro'),
]
