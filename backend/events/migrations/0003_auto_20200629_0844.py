# Generated by Django 3.0.7 on 2020-06-29 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_how_many_minutes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-creation_date']},
        ),
    ]
