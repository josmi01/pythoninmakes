# Generated by Django 4.2 on 2023-05-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-08-20'),
            preserve_default=False,
        ),
    ]
