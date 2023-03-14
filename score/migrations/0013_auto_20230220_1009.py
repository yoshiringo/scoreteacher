# Generated by Django 3.2.16 on 2023-02-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0012_alter_stat_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='login_user',
        ),
        migrations.AddField(
            model_name='person',
            name='login_user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='fw',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='FWキープ率'),
        ),
    ]