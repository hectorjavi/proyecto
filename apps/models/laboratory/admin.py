from django.contrib import admin

from . import models


# Register your models here.
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sub_name", "descripcion", "created", "modified")
    list_per_page = 15
    ordering = ("-created", "-modified")
    date_hierarchy = "created"


admin.site.register(models.Laboratory, LaboratoryAdmin)
