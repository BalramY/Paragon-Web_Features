# Generated by Django 3.0.6 on 2021-05-13 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0094_typeteststandards_ts_standard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeteststandards',
            old_name='ts_text',
            new_name='ts_description',
        ),
    ]
