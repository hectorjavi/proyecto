from django.contrib import admin

from . import models


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "dni", "created", "modified")
    list_per_page = 15
    ordering = ("-created", "-modified")
    date_hierarchy = "created"


admin.site.register(models.Person, PersonAdmin)
