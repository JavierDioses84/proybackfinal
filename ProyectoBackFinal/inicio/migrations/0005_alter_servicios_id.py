# Generated by Django 5.1.5 on 2025-01-31 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_alter_servicios_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
