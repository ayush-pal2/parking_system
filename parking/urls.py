from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-slot/', views.add_slot, name='add_slot'),
    path('park-vehicle/', views.park_vehicle, name='park_vehicle'),
    path('remove-vehicle/<int:slot_id>/', views.remove_vehicle, name='remove_vehicle'),
    path('delete-slot/<int:slot_id>/', views.delete_slot, name='delete_slot'),
]
