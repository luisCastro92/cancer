from django.contrib import admin
from .models import TejidoMama
# Register your models here.

class TejidoMamaAdmin(admin.ModelAdmin):
    list_display = ('parteP','temp','color','inflamacion')
admin.site.register(TejidoMama, TejidoMamaAdmin)
