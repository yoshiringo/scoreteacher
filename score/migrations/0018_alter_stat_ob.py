# Generated by Django 3.2.16 on 2023-02-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0017_auto_20230225_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='ob',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='OB数'),
        ),
    ]