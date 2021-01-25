from django.contrib import admin
from .models import Modules


class ModulesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fonction', 'eurorack', 'prix')
    search_fields = ['nom']

# Register your models here.
admin.site.register(Modules, ModulesAdmin)