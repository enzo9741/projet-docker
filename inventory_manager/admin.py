from django.contrib import admin

from inventory_manager.models import SmartHdd, SmartSsd, Smart, Ram, Ssd, Hdd, Drive, Cpu, Cable, Amovible, \
    Historic, Objects

admin.site.register(Objects)
admin.site.register(Historic)
admin.site.register(Amovible)
admin.site.register(Cable)
admin.site.register(Cpu)
admin.site.register(Drive)
admin.site.register(Hdd)
admin.site.register(Ssd)
admin.site.register(Ram)
admin.site.register(Smart)
admin.site.register(SmartHdd)
admin.site.register(SmartSsd)


