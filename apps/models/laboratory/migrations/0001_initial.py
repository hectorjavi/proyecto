# Generated by Django 4.1.3 on 2023-11-02 19:55

import uuid

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Laboratory",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    model_utils.fields.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("sub_name", models.CharField(max_length=10)),
                ("descripcion", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": 'Registro "Receta Alimentaria"',
                "verbose_name_plural": 'Tabla de registros "Receta Alimentaria"',
                "db_table": "laboratory",
            },
        ),
    ]