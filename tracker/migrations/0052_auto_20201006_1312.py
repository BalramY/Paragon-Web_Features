# Generated by Django 3.0.6 on 2020-10-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0051_auto_20201005_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_fr_clothes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_hardhat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_safety_glasses',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_safety_gloves',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_safety_shoes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_safety_training_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_safety_vest',
            field=models.BooleanField(default=False),
        ),
    ]
