from django.db import models

from apps.models import base_model

NAME_MODEL_ES = "Persona"


class Person(base_model.BaseModel):
    full_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        db_table = "person"
        verbose_name = base_model.VERBOSE_NAME % NAME_MODEL_ES
        verbose_name_plural = base_model.VERBOSE_NAME_PLURAL % NAME_MODEL_ES
