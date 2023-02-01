# Generated by Django 3.0.6 on 2020-08-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0015_auto_20200813_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='dangerous_chemical_exposure',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='escort_considerations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='is_6ft_work',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_confined_space',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_live_work_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_safety_training_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='job',
            name='is_switching_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_ungaurded_holes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='live_work_voltage',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='permit_requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='restricted_items',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='safety_training_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='safety_training_time',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='switching_specifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]
