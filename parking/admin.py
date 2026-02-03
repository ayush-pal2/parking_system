from django.contrib import admin
from .models import ParkingSlot

@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('slotNo', 'isCovered', 'isEVCharging', 'isOccupied')
    list_filter = ('isCovered', 'isEVCharging', 'isOccupied')
    search_fields = ('slotNo',)
    ordering = ('slotNo',)
