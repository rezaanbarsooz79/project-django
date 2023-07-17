from django.contrib import admin

from .models import Component,WaterConsumption,WinterWater,SoilAnalysis,Pest,Fertilizer,Harvest,Orchard

admin.site.register(Component)
admin.site.register(WaterConsumption)
admin.site.register(WinterWater)
admin.site.register(SoilAnalysis)
admin.site.register(Pest)
admin.site.register(Fertilizer)
admin.site.register(Harvest)
admin.site.register(Orchard)
