# Generated by Django 5.1.1 on 2024-11-21 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.client'),
        ),
    ]
