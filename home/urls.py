from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coinPrice, name="coin"),
    path('coin/time', views.time, name="coin"),
]
