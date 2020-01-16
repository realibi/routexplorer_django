from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('addresses/', views.addresses),
    path('multiroute/', views.multiroute),
    path('delivered/<int:address_id>', views.delivered)
]