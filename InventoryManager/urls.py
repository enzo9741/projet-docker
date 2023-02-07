"""InventoryManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from inventory_manager.views.add import add
from inventory_manager.views.qrcode import qrcode

from inventory_manager.views.allqrcode import allqrcode
from inventory_manager.views.scan import scan
from inventory_manager.views.index import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('scan', scan, name='scan'),
    path('allqrcode', allqrcode, name='allqrcode'),
    path('add', add, name='add'),
    path('qrcode/<slug:uidb64>/', qrcode, name='qrcode'),
]
