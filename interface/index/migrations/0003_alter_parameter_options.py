# Generated by Django 3.2.3 on 2021-05-30 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210528_0532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parameter',
            options={'ordering': ('name',)},
        ),
    ]
