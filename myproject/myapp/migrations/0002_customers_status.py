# Generated by Django 5.0.6 on 2024-07-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='Status',
            field=models.IntegerField(default=0, verbose_name='Status'),
        ),
    ]
