import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inventory_manager.models import Objects


@login_required(login_url='/admin/login?next=/')
def allqrcode(request):
    objects = Objects.objects.all().order_by('-available')
    uuid = []
    brand = []
    reference = []
    serial_number = []

    for obj in objects:
        uuid.append(obj.uuid)
        brand.append(obj.brand)
        reference.append(obj.reference)
        serial_number.append(obj.serial_number)

    return render(request, 'allqrcode.html', {'uuid': uuid, 'brand': brand, 'reference': reference, 'serial_number': serial_number})
