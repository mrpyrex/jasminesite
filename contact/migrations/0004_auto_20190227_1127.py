# Generated by Django 2.1 on 2019-02-27 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190227_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]