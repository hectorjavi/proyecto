from django.db import models

from apps.models import base_model

NAME_MODEL_ES = "Laboratorio"


class Laboratory(base_model.BaseModel):
    name = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "laboratory"
        # unique_together = ("title", "category")
        verbose_name = base_model.VERBOSE_NAME % NAME_MODEL_ES
        verbose_name_plural = base_model.VERBOSE_NAME_PLURAL % NAME_MODEL_ES
