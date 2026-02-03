from django.db import models

class ParkingSlot(models.Model):
    slotNo = models.IntegerField(unique=True)
    isCovered = models.BooleanField(default=False)
    isEVCharging = models.BooleanField(default=False)
    isOccupied = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['slotNo']
    
    def __str__(self):
        return f"Slot {self.slotNo}"
    
    @staticmethod
    def park_vehicle(needs_ev, needs_cover):
        
        available_slots = ParkingSlot.objects.filter(isOccupied=False)
        
        if needs_ev:
            available_slots = available_slots.filter(isEVCharging=True)
        
        if needs_cover:
            available_slots = available_slots.filter(isCovered=True)
        
        slot = available_slots.order_by('slotNo').first()
        
        if slot:
            slot.isOccupied = True
            slot.save()
            return slot
        
        return None
