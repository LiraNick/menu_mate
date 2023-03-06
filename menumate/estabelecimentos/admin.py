from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Estabelecimento)
admin.site.register(models.Mesa)
admin.site.register(models.Garcom)
admin.site.register(models.Reserva)
admin.site.register(models.Menu)
