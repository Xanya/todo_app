# Generated by Django 4.1.1 on 2022-10-12 00:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_active_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]