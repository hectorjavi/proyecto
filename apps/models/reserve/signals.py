from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Reserve


def validar_disponibilidad(current_reserve, date, start_time, end_time, laboratory):
    reservas_existentes = Reserve.objects.filter(
        date=date,
        laboratory=laboratory,
        end_time__gte=start_time,  # Verifica si la hora de finalización es después de la hora de inicio
    ).exclude(id=current_reserve.id)
    is_available_start_time = False
    is_available_end_time = False
    # Verifica si la hora de inicio y fin coincide con alguna reserva existente
    for reserva in reservas_existentes:
        is_available_start_time = reserva.start_time <= start_time <= reserva.end_time
        if is_available_start_time:
            return False
    for reserva in reservas_existentes:
        is_available_end_time = reserva.start_time <= end_time <= reserva.end_time
        if is_available_end_time:
            return False
    return True


@receiver(pre_save, sender=Reserve)
@transaction.atomic
def pre_save_reserve(sender, instance, **kwargs):
    is_save = validar_disponibilidad(
        current_reserve=instance,
        date=instance.date,
        start_time=instance.start_time,
        end_time=instance.end_time,
        laboratory=instance.laboratory,
    )

    if not is_save:
        raise ValidationError(
            "¡Error! La reserva no puede ser creada debido a conflictos de horarios."
        )
