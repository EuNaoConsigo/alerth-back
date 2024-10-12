# Generated by Django 5.1.1 on 2024-10-03 21:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('serviceCategory_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceEntity',
            fields=[
                ('serviceEntity_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityCategory',
            fields=[
                ('entityCategory_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('serviceCategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.servicecategory')),
                ('serviceEntity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.serviceentity')),
            ],
        ),
    ]
