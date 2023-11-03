from django.contrib import admin

from . import models


# Register your models here.
class ReserveAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "start_time", "end_time", "created", "modified")
    list_per_page = 15
    ordering = ("-created", "-modified")
    date_hierarchy = "created"


admin.site.register(models.Reserve, ReserveAdmin)
