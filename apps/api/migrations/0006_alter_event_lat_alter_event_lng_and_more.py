# Generated by Django 5.1.1 on 2024-10-27 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_client_total_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='event',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='reports_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]