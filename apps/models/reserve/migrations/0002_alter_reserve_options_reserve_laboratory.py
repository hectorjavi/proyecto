# Generated by Django 4.1.3 on 2023-11-02 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("laboratory", "0002_alter_laboratory_options"),
        ("reserve", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reserve",
            options={
                "verbose_name": 'Registro "Reservar Laboratorio"',
                "verbose_name_plural": 'Tabla de registros "Reservar Laboratorio"',
            },
        ),
        migrations.AddField(
            model_name="reserve",
            name="laboratory",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="laboratory_reserve",
                to="laboratory.laboratory",
                verbose_name="Laboratorio",
            ),
            preserve_default=False,
        ),
    ]
