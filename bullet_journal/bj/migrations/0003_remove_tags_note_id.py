# Generated by Django 2.1.7 on 2019-03-22 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bj', '0002_auto_20190321_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='note_id',
        ),
    ]
