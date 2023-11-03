from django.apps import AppConfig


class ReserveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.models.reserve"

    def ready(self):
        __import__("apps.models.reserve.signals")
