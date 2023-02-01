# Generated by Django 3.0.6 on 2022-03-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0118_auto_20220314_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsheet',
            name='is_cable_shielded',
        ),
        migrations.AlterField(
            model_name='testsheet',
            name='cable_ending_point',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='testsheet',
            name='cable_insulation_thickness',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='testsheet',
            name='cable_size',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='testsheet',
            name='cable_starting_point',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='testsheet',
            name='cable_voltage_rating',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='testsheet',
            name='operating_cable_voltage',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=15, null=True),
        ),
    ]
