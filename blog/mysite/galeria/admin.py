from django.contrib import admin

from .models import Galeria

#admin.site.register(Galeria)

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    fields = ['foto', 'publicate_on']
    list_display = ['create_on', 'foto', 'publicate_on', 'publicate']
    pass