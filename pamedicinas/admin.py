from django.contrib import admin
from pamedicinas.models import Medicina, MedicinaAdmin, Notificacion, NotificacionAdmin

admin.site.register(Medicina, MedicinaAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
