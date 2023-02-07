from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/admin/login?next=/')
def scan(request):
    return render(request, 'scan.html', {})
