# Generated by Django 4.1.1 on 2022-10-18 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_task_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
    ]
