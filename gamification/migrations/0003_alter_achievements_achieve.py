# Generated by Django 4.1.2 on 2022-10-08 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0002_achievements_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='achieve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.achievement', unique=True),
        ),
    ]
