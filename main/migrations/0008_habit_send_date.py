# Generated by Django 4.2.3 on 2023-08-04 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_habit_related_habit'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='send_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата выполнения'),
        ),
    ]
