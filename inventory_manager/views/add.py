import uuid as uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inventory_manager.forms.amovibleForm import AmovibleForm
from inventory_manager.forms.cableForm import CableForm
from inventory_manager.forms.cpuForm import CpuForm
from inventory_manager.forms.driveForm import DriveForm
from inventory_manager.forms.hddForm import HddForm
from inventory_manager.forms.objectsForm import ObjectsForm
from inventory_manager.forms.ramForm import RamForm
from inventory_manager.models import Objects, Amovible, Cable, Cpu, Ram, Drive, Hdd, Ssd


@login_required(login_url='/admin/login?next=/')
def add(request):
    if request.method == "POST":
        post = request.POST
        my_uuid = uuid.uuid4()
        available = 1 if 'available' in post else 0

        Objects(uuid=my_uuid, brand=post['brand'], reference=post['reference'], serial_number=post['serial_number'], available=available).save()
        obj = Objects.objects.all().filter(uuid=my_uuid).first()

        match post['selector'].lower():
            case 'amovible':
                Amovible(uuid=obj, capacity=post['capacity'], tech=post['tech']).save()
            case 'cable':
                Cable(uuid=obj, length=post['length'], start_type=post['start_type'], end_type=post['end_type']).save()
            case 'cpu':
                Cpu(uuid=obj, core=post['core'], threads=post['threads'], frequency=post['frequency']).save()
            case 'ram':
                Ram(uuid=obj, capacity=post['capacity'], type=post['type'], frequency=post['frequency']).save()
            case 'hdd':
                Drive(uuid=obj, capacity=post['capacity'], read_value=post['read_value'], write_value=post['write_value']).save()
                drive = Drive.objects.all().filter(uuid=my_uuid).first()
                Hdd(uuid=drive, rotation_speed=post['rotation_speed'], size=post['size']).save()
            case 'ssd':
                Drive(uuid=obj, capacity=post['capacity'], read_value=post['read_value'], write_value=post['write_value']).save()
                drive = Drive.objects.all().filter(uuid=my_uuid).first()
                Ssd(uuid=drive).save()

    objects_form = ObjectsForm()
    amovible_form = AmovibleForm()
    cable_form = CableForm()
    cpu_form = CpuForm()
    drive_form = DriveForm()
    hdd_form = HddForm()
    ram_form = RamForm()
    return render(request, 'add.html', {'objects': objects_form, 'amovible': amovible_form, 'cable': cable_form, 'cpu': cpu_form, 'drive': drive_form, 'hdd': hdd_form, 'ram': ram_form})
