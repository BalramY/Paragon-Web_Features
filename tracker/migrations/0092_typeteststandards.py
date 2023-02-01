# Generated by Django 3.0.6 on 2021-05-13 22:05

from django.db import migrations, models
import django.db.models.deletion
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0091_modelnotes_typenotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTestStandards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_file', models.FileField(blank=True, max_length=500, null=True, upload_to=tracker.models.type_ts_path)),
                ('ts_name', models.CharField(blank=True, max_length=256, null=True)),
                ('ts_url', models.URLField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ts_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eq_type_standards', to='tracker.Type')),
            ],
        ),
    ]
