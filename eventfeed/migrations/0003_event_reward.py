# Generated by Django 4.1.2 on 2022-10-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventfeed', '0002_alter_event_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reward',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
