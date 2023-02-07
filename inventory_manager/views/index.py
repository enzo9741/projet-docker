from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inventory_manager.models import Objects, Ram, Cpu, Hdd, Ssd, Amovible, Cable


@login_required(login_url='/admin/login?next=/')
def index(request):
    #Variables
    objects = Objects.objects.all().order_by('-available')
    cpu = Cpu.objects.all().order_by('-uuid__available')
    ram = Ram.objects.all().order_by('-uuid__available')
    hdd = Hdd.objects.all().order_by('-uuid__uuid__available')
    ssd = Ssd.objects.all().order_by('-uuid__uuid__available')
    amovible = Amovible.objects.all().order_by('-uuid__available')
    cable = Cable.objects.all().order_by('-uuid__available')

    return render(request, 'index.html', {'objects': objects, 'cpu': cpu, 'ram': ram, 'hdd': hdd, 'ssd': ssd, 'amovible':
                                           amovible, 'cable': cable})
