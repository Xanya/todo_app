# Generated by Django 4.1.1 on 2023-02-19 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_task_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
