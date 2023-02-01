# Generated by Django 3.2 on 2022-12-10 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0123_supportsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportsession',
            name='requester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requester_session', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='supportsession',
            name='supporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supporter_session', to=settings.AUTH_USER_MODEL),
        ),
    ]
