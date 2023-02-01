# Generated by Django 3.2 on 2023-01-29 21:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0127_alter_supportrequest_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScopeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_scope_item', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_scope_item', to='tracker.job')),
            ],
        ),
        migrations.AddField(
            model_name='userproperties',
            name='is_company_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_entry', models.TextField(blank=True, null=True)),
                ('loto', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sheet_signature', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScopeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.TextField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_scope_task', to=settings.AUTH_USER_MODEL)),
                ('task_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scope_item_task', to='tracker.scopeitem')),
            ],
        ),
        migrations.CreateModel(
            name='SafetySheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_safety_sheet', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_safety_sheet', to='tracker.job')),
            ],
        ),
        migrations.CreateModel(
            name='SafetyHazard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazard', models.TextField(blank=True, null=True)),
                ('danger_level', models.IntegerField(blank=True, null=True)),
                ('probability', models.IntegerField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_hazard', to=settings.AUTH_USER_MODEL)),
                ('safety_sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sheet_hazard', to='tracker.safetysheet')),
                ('scope_item', models.ManyToManyField(blank=True, related_name='scope_hazard', to='tracker.ScopeItem')),
            ],
        ),
        migrations.CreateModel(
            name='SafetyBoolean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField(blank=True, null=True)),
                ('safety_sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sheet_bool', to='tracker.safetysheet')),
            ],
        ),
        migrations.CreateModel(
            name='LotoDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ground_location', models.TextField(blank=True, null=True)),
                ('is_grounded', models.BooleanField(default=False)),
                ('safety_sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sheet_loto', to='tracker.safetysheet')),
            ],
        ),
    ]
