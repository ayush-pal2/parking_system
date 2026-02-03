from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ParkingSlot
from django.http import JsonResponse

def index(request):
    """Main dashboard view"""
    slots = ParkingSlot.objects.all()
    total_slots = slots.count()
    occupied_slots = slots.filter(isOccupied=True).count()
    available_slots = total_slots - occupied_slots
    
    context = {
        'slots': slots,
        'total_slots': total_slots,
        'occupied_slots': occupied_slots,
        'available_slots': available_slots,
    }
    return render(request, 'parking/index.html', context)

def add_slot(request):
    """Add a new parking slot"""
    if request.method == 'POST':
        slot_no = request.POST.get('slotNo')
        is_covered = request.POST.get('isCovered') == 'on'
        is_ev_charging = request.POST.get('isEVCharging') == 'on'
        
        try:
            slot_no = int(slot_no)
            if ParkingSlot.objects.filter(slotNo=slot_no).exists():
                messages.error(request, f'Slot {slot_no} already exists!')
            else:
                ParkingSlot.objects.create(
                    slotNo=slot_no,
                    isCovered=is_covered,
                    isEVCharging=is_ev_charging,
                    isOccupied=False
                )
                messages.success(request, f'Slot {slot_no} added successfully!')
        except ValueError:
            messages.error(request, 'Invalid slot number!')
        
        return redirect('index')
    
    return render(request, 'parking/add_slot.html')

def park_vehicle(request):
    """Park a vehicle in the nearest available slot"""
    if request.method == 'POST':
        needs_ev = request.POST.get('needsEV') == 'on'
        needs_cover = request.POST.get('needsCover') == 'on'
        
        slot = ParkingSlot.park_vehicle(needs_ev, needs_cover)
        
        if slot:
            messages.success(request, f'Vehicle parked successfully in Slot {slot.slotNo}!')
        else:
            messages.error(request, 'No slot available matching your requirements!')
        
        return redirect('index')
    
    return render(request, 'parking/park_vehicle.html')

def remove_vehicle(request, slot_id):
    """Remove a vehicle from a parking slot"""
    slot = get_object_or_404(ParkingSlot, id=slot_id)
    
    if slot.isOccupied:
        slot.isOccupied = False
        slot.save()
        messages.success(request, f'Vehicle removed from Slot {slot.slotNo}!')
    else:
        messages.warning(request, f'Slot {slot.slotNo} is already empty!')
    
    return redirect('index')

def delete_slot(request, slot_id):
    """Delete a parking slot"""
    slot = get_object_or_404(ParkingSlot, id=slot_id)
    slot_no = slot.slotNo
    slot.delete()
    messages.success(request, f'Slot {slot_no} deleted successfully!')
    return redirect('index')
