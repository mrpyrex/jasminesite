# Generated by Django 2.1 on 2019-03-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='theme',
            field=models.CharField(default='Batman', max_length=200),
            preserve_default=False,
        ),
    ]
