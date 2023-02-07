import objects
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from inventory_manager.models import Objects


@login_required(login_url='/admin/login?next=/')
def qrcode(request, uidb64):
    objects = Objects.objects.all().filter(uuid=uidb64).first()
    objects.available = not objects.available
    objects.save()
    return redirect('index')
