from model_utils.models import TimeStampedModel, UUIDModel

VERBOSE_NAME = 'Registro "%s"'
VERBOSE_NAME_PLURAL = 'Tabla de registros "%s"'


class BaseModel(UUIDModel, TimeStampedModel):
    class Meta:
        abstract = True
