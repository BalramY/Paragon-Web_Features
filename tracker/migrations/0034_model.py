# Generated by Django 3.0.6 on 2020-08-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0033_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('model_id', models.CharField(max_length=128)),
                ('manual_folder', models.URLField(blank=True, max_length=300, null=True)),
                ('model_test_sheet', models.URLField(blank=True, max_length=300, null=True)),
                ('model_folder', models.URLField(blank=True, max_length=300, null=True)),
                ('model_test_guide', models.URLField(blank=True, max_length=300, null=True)),
                ('model_notes', models.URLField(blank=True, max_length=300, null=True)),
                ('model_test_equipment', models.ManyToManyField(blank=True, related_name='model_test_equipment', to='tracker.TestEquipment')),
            ],
        ),
    ]
