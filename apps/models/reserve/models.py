from django.db import models

from apps.models import base_model
from apps.models.laboratory import models as laboratory
from apps.models.person import models as person

NAME_MODEL_ES = "Reservar Laboratorio"


class Reserve(base_model.BaseModel):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    laboratory = models.ForeignKey(
        laboratory.Laboratory,
        on_delete=models.CASCADE,
        related_name="laboratory_reserve",
        verbose_name=laboratory.NAME_MODEL_ES,
    )
    person = models.ManyToManyField(
        person.Person,
        related_name="person_reserve",
        verbose_name=person.NAME_MODEL_ES,
        blank=True,
    )

    def __str__(self):
        return f"{self.date}: {self.start_time}-{self.end_time}"

    class Meta:
        db_table = "reserve"
        verbose_name = base_model.VERBOSE_NAME % NAME_MODEL_ES
        verbose_name_plural = base_model.VERBOSE_NAME_PLURAL % NAME_MODEL_ES
