# Generated by Django 5.0.6 on 2024-07-10 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_booking_booking_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='bm_id',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Suggestions',
        ),
    ]
