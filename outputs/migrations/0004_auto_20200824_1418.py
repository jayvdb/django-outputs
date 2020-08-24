# Generated by Django 2.2.9 on 2020-08-24 12:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0003_init_emails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduler',
            name='emails',
        ),
        migrations.AlterField(
            model_name='export',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), default=list, size=None),
        ),
    ]