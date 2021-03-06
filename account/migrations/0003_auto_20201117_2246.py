# Generated by Django 3.1.3 on 2020-11-18 01:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201116_0536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='task',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='ended_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
